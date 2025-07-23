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

# Logo principal
col1, col2, col3 = st.columns([4, 2, 4])   # columnas laterales más angostas
with col2:
    st.image("assets/Logo1.png", width=200, use_container_width=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 class='titulo-principal'>Análisis de Tarifas de Energía</h1>", unsafe_allow_html=True)

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
    # Limpiar selectores de periodos
    if 'periodo_inicio_selector' in st.session_state:
        del st.session_state['periodo_inicio_selector']
    if 'periodo_fin_selector' in st.session_state:
        del st.session_state['periodo_fin_selector']

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
    en un rango de periodos específico que puedes seleccionar.
    """)
    
    st.markdown("""
    ### Instrucciones
    1. Espere a que se cargue archivo y la aplicación realice un análisis previo de los datos
    2. Seleccione el mercado, comercializador y nivel de tensión a comparar
    3. Seleccione los periodos inicial y final a comparar
    5. Ejecute la comparación
    6. Visualice los resultados y exporte en excel si lo desea
    
    ### Notas
    - El archivo exportado contiene los periodos resultantes de la comparación
    """)
    
    st.markdown("---")
    
    # Información de versión y copyright
    st.markdown("""
    <div style='position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px;'>
    <small>v2.2.1 | © 2025 Ruitoque Energía</small>
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
            # Selectores de periodos
            st.subheader("📅 Selección de Periodos")
            col1, col2 = st.columns(2)
            
            with col1:
                # Obtener fechas disponibles para este filtro (orden cronológico)
                fechas_disponibles = sorted(
                    df_procesado[
                        (df_procesado['MERCADO'] == mercado) & 
                        (df_procesado['COMERCIALIZADOR'] == comercializador) &
                        (df_procesado['NT'] == nt)
                    ]['FECHA'].unique()
                )
                
                if fechas_disponibles:
                    # Calcular el índice por defecto para los últimos 12 meses
                    # Si hay menos de 12 periodos, usar el primero disponible
                    if len(fechas_disponibles) >= 12:
                        # Para obtener exactamente 12 periodos: último periodo - 11 = primer periodo de los últimos 12
                        default_inicio_index = len(fechas_disponibles) - 12
                    else:
                        default_inicio_index = 0
                    
                    periodo_inicio = st.selectbox(
                        'Periodo inicial:',
                        options=fechas_disponibles,
                        index=default_inicio_index,
                        key='periodo_inicio_selector'
                    )
                else:
                    st.error("No hay fechas disponibles para esta selección")
                    periodo_inicio = None
            
            with col2:
                if fechas_disponibles:
                    # Mostrar todas las fechas disponibles para el periodo final
                    periodo_fin = st.selectbox(
                        'Periodo final:',
                        options=fechas_disponibles,
                        index=len(fechas_disponibles)-1,  # Último periodo disponible
                        key='periodo_fin_selector'
                    )
                else:
                    st.info("No hay fechas disponibles")
                    periodo_fin = None
            
            # Información sobre el rango seleccionado
            if periodo_inicio and periodo_fin:
                if periodo_inicio > periodo_fin:
                    st.warning("⚠️ El periodo de inicio debe ser menor o igual al periodo final")
                else:
                    # Calcular cuántos periodos hay en el rango seleccionado
                    fechas_rango = [fecha for fecha in fechas_disponibles if periodo_inicio <= fecha <= periodo_fin]
                    num_periodos = len(fechas_rango)
                    st.info(f"📊 Analizando periodos desde {periodo_inicio} hasta {periodo_fin} ({num_periodos} periodos seleccionados)")
            
            if st.button('▶️ Ejecutar Comparación', type='primary', key='ejecutar_btn'):
                if periodo_inicio and periodo_fin and periodo_inicio <= periodo_fin:
                    with st.spinner('Ejecutando comparación de tarifas...'):
                        df_resultado = comparar_cu(df_procesado, mercado, comercializador, nt, periodo_inicio, periodo_fin)
                    
                    if df_resultado is not None:
                        st.session_state['df_resultado'] = df_resultado
                        st.session_state['mostrar_resultados'] = True
                        st.session_state['parametros_comparacion'] = {
                            'mercado': mercado,
                            'comercializador': comercializador,
                            'nt': nt,
                            'periodo_inicio': periodo_inicio,
                            'periodo_fin': periodo_fin
                        }
                        st.rerun()
    else:
        # Mostrar parámetros de la comparación
        st.subheader("Parámetros de la comparación:")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.info(f"🏢 Mercado: {st.session_state['parametros_comparacion']['mercado']}")
        with col2:
            st.info(f"🏪 Comercializador: {st.session_state['parametros_comparacion']['comercializador']}")
        with col3:
            st.info(f"⚡ Nivel de Tensión: {st.session_state['parametros_comparacion']['nt']}")
        with col4:
            st.info(f"📅 Periodos: {st.session_state['parametros_comparacion']['periodo_inicio']} - {st.session_state['parametros_comparacion']['periodo_fin']}")

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
                st.session_state['df_resultado'].to_excel(output, index=False, sheet_name="Comparacion", engine='openpyxl')
                output.seek(0)
                
                st.download_button(
                    label="📥 Descargar Resultados",
                    data=output.getvalue(),
                    file_name=f"comparacion_cu_{st.session_state['parametros_comparacion']['mercado']}_{st.session_state['parametros_comparacion']['comercializador']}_{st.session_state['parametros_comparacion']['nt']}_{st.session_state['parametros_comparacion']['periodo_inicio']}_{st.session_state['parametros_comparacion']['periodo_fin']}.xlsx",
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