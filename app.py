"""Aplicación principal para el análisis de tarifas de energía."""

import streamlit as st
import pandas as pd
import warnings
from pathlib import Path
import io

from config.constants import PAGE_CONFIG, INITIAL_SESSION_STATE
from config.styles import CUSTOM_CSS
from auth.azure_auth import AzureAuth
from auth.sharepoint import SharePointClient
from utils.data_processing import cargar_tabla_desde_excel, procesar_df_tarifas
from utils.comparison import comparar_cu
from utils.visualization import crear_grafico_comparacion

# Ignorar advertencias
warnings.filterwarnings('ignore')

# Configuración de la página
st.set_page_config(**PAGE_CONFIG)

# Aplicar estilos CSS personalizados
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Título principal
st.markdown("<h1 class='titulo-principal'>📊 Análisis de Tarifas de Energía</h1>", unsafe_allow_html=True)

# Inicializar el estado de la sesión
for key, value in INITIAL_SESSION_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value

def reset_comparacion():
    """Reinicia el estado de la comparación."""
    st.session_state['mostrar_resultados'] = False
    st.session_state['df_resultado'] = None
    st.session_state['parametros_comparacion'] = {}
    st.session_state['mensajes_analisis'] = []

# --- AUTENTICACIÓN AZURE AD ---
azure_auth = AzureAuth()
token = azure_auth.get_token()

if not token:
    # Solo muestra el botón de login, sin error
    token = azure_auth.authenticate()
    st.stop()

# --- SIDEBAR CON INFORMACIÓN ---
with st.sidebar:
    # Logo de la compañía centrado
    col1, col2, col3 = st.columns([0.5,4,0.5])
    with col2:
        st.image("assets/path1310.png", width=200)
    
    st.markdown("---")
    
    st.header("ℹ️ Información")
    st.markdown("""
    Compara el CU de RUITOQUE frente a otro comercializador 
    recorriendo hasta 12 periodos desde el último periodo válido 
    hacia atrás.
    """)
    
    st.markdown("""
    ### Instrucciones
    1. El archivo se descarga automáticamente desde SharePoint
    2. Espera a que el archivo cargue y haga un análisis previo de los datos
    3. Seleccione el mercado a analizar
    4. Seleccione el comercializador para comparar
    5. Seleccione el nivel de tensión
    6. Ejecute la comparación
    7. Visualice los resultados y exporte si lo desea
    
    ### Notas
    - La ejecución entre paso y paso puede tardar algunos minutos
    - El archivo exportado contiene los periodos resultantes de la comparación
    """)
    
    st.markdown("---")
    
    # Información de versión y copyright
    st.markdown("""
    <div style='position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px;'>
    <small>v1.0.0 | © 2025 Ruitoque Energía</small>
    </div>
    """, unsafe_allow_html=True)

# --- SECCIÓN 1: CARGA DE ARCHIVO ---
st.header("1️⃣ Carga de Archivo")

if not st.session_state['archivo_cargado']:
    # Inicializar cliente de SharePoint
    sharepoint_client = SharePointClient(token)
    
    with st.spinner('Descargando archivo desde SharePoint y procesando datos...'):
        archivo_bytes = sharepoint_client.download_file()
        
        if archivo_bytes:
            archivo_stream = io.BytesIO(archivo_bytes)
            df = cargar_tabla_desde_excel(archivo_stream)
            
            if df is not None:
                with st.spinner('Aplicando transformaciones a los datos...'):
                    df_procesado = procesar_df_tarifas(df)
                    
                    if df_procesado is not None:
                        st.session_state['df_tarifas'] = df_procesado
                        st.session_state['archivo_cargado'] = True
                        st.rerun()
        else:
            st.error("No se pudo descargar el archivo. Verifica la conexión y permisos.")
            st.stop()
else:
    # Mostrar resumen de datos del archivo cargado
    df_procesado = st.session_state['df_tarifas']
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Registros", len(df_procesado))
    with col2:
        st.metric("Mercados", df_procesado['MERCADO'].nunique())
    with col3:
        st.metric("Comercializadores", df_procesado['COMERCIALIZADOR'].nunique())
    with col4:
        st.metric("Niveles de Tensión", df_procesado['NT'].nunique())
    
    # Vista previa de datos
    st.subheader("Vista previa de datos")
    st.caption("Mostrando las últimas 5 filas de los datos cargados (orden descendente)")
    st.dataframe(
        df_procesado.sort_values('FECHA', ascending=False).head(5),
        use_container_width=True,
        hide_index=True
    )

# --- SECCIÓN 2: COMPARACIÓN DE TARIFAS ---
if st.session_state['archivo_cargado']:
    st.markdown("---")
    st.header("2️⃣ Comparación de Tarifas")
    
    df_procesado = st.session_state['df_tarifas']
    
    if not st.session_state['mostrar_resultados']:
        # Widgets de selección
        col1, col2, col3 = st.columns(3)
        
        with col1:
            mercados = sorted([m for m in df_procesado['MERCADO'].unique() if pd.notna(m)])
            if mercados:
                mercado = st.selectbox('Mercado:', options=mercados, key='mercado_selector')
            else:
                st.error("No hay mercados disponibles en los datos")
                mercado = None
        
        with col2:
            if mercado:
                comercializadores = sorted([
                    c for c in df_procesado[df_procesado['MERCADO']==mercado]['COMERCIALIZADOR'].unique()
                    if pd.notna(c) and c != "RUITOQUE"
                ])
                if comercializadores:
                    comercializador = st.selectbox('Comercializador:', options=comercializadores, key='comercializador_selector')
                else:
                    st.error("No hay comercializadores disponibles para este mercado")
                    comercializador = None
            else:
                st.info("Seleccione primero un mercado")
                comercializador = None
        
        with col3:
            if mercado and comercializador:
                niveles_tension = sorted([
                    nt for nt in df_procesado[
                        (df_procesado['MERCADO']==mercado) & 
                        (df_procesado['COMERCIALIZADOR']==comercializador)
                    ]['NT'].unique()
                    if pd.notna(nt)
                ])
                if niveles_tension:
                    nt = st.selectbox('Nivel de Tensión:', options=niveles_tension, key='nt_selector')
                else:
                    st.error("No hay niveles de tensión disponibles para esta selección")
                    nt = None
            else:
                st.info("Seleccione primero un mercado y comercializador")
                nt = None
        
        if mercado and comercializador and nt:
            if st.button('▶️ Ejecutar Comparación', type='primary', key='ejecutar_btn'):
                with st.spinner('Ejecutando comparación de tarifas...'):
                    df_resultado = comparar_cu(df_procesado, mercado, comercializador, nt)
                    
                    if df_resultado is not None:
                        st.session_state['df_resultado'] = df_resultado
                        st.session_state['mostrar_resultados'] = True
                        st.session_state['parametros_comparacion'] = {
                            'mercado': mercado,
                            'comercializador': comercializador,
                            'nt': nt
                        }
                        st.rerun()
    else:
        # Mostrar parámetros de la comparación
        st.subheader("Parámetros de la comparación:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(f"🏢 Mercado: {st.session_state['parametros_comparacion']['mercado']}")
        with col2:
            st.info(f"🏪 Comercializador: {st.session_state['parametros_comparacion']['comercializador']}")
        with col3:
            st.info(f"⚡ Nivel de Tensión: {st.session_state['parametros_comparacion']['nt']}")

        # Mostrar mensajes del análisis
        st.subheader("📊 Análisis Periodo a Periodo")
        for mensaje in st.session_state['mensajes_analisis']:
            st.write(mensaje)

        # Mostrar resultados
        if st.session_state['df_resultado'] is not None:
            st.subheader("📈 Resultados Detallados")
            st.dataframe(st.session_state['df_resultado'])
            
            # Crear y mostrar gráfico
            fig = crear_grafico_comparacion(st.session_state['df_resultado'])
            if fig:
                st.plotly_chart(fig, use_container_width=True)
            
            # Botones de acción
            col1, col2 = st.columns(2)
            with col1:
                # Botón de descarga
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    st.session_state['df_resultado'].to_excel(writer, index=False, sheet_name="Comparacion")
                
                st.download_button(
                    label="📥 Descargar Resultados",
                    data=output.getvalue(),
                    file_name=f"comparacion_cu_{st.session_state['parametros_comparacion']['mercado']}_{st.session_state['parametros_comparacion']['comercializador']}_{st.session_state['parametros_comparacion']['nt']}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    key='descargar_btn'
                )
            
            with col2:
                if st.button('🔄 Nueva Comparación', key='nueva_comparacion'):
                    reset_comparacion()
                    st.rerun()

else:
    st.info("ℹ️ Por favor, primero carga el archivo de tarifas para realizar la comparación.")

# Pie de página
st.markdown("---")
st.markdown(
    "<div style='text-align: left;'>Desarrollado por: <a href='https://www.andresbadillo.co/' target='_blank'>andresbadillo.co</a></div>",
    unsafe_allow_html=True
) 