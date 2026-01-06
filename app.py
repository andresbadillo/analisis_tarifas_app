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
from utils.comparison import comparar_cu, calcular_promedios_periodo, filtrar_resultados_por_periodo
from utils.visualization import crear_grafico_comparacion, crear_grafico_comparacion_multiple
from utils.savings_analysis import calcular_ahorro_energia, mostrar_analisis_ahorro

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
    st.session_state['df_resultado_filtrado'] = None
    st.session_state['resultados_comparacion'] = {}
    st.session_state['comercializador_activo'] = None
    st.session_state['parametros_comparacion'] = {}
    st.session_state['mensajes_analisis'] = {}
    st.session_state['slider_periodo_inicio'] = None
    st.session_state['slider_periodo_fin'] = None
    st.session_state['mostrar_analisis_ahorro'] = False
    st.session_state['resultados_ahorro'] = None
    st.session_state['consumo_promedio_kwh'] = None
    st.session_state['comercializador_ahorro'] = None
    if 'comercializador_ahorro_anterior' in st.session_state:
        del st.session_state['comercializador_ahorro_anterior']
    # Limpiar flag de error de carga
    if 'error_carga' in st.session_state:
        del st.session_state['error_carga']
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
    4. Ejecute la comparación
    5. Visualice los resultados y gráfico de comparación
    6. Exporte los resultados en Excel si lo desea
    7. **Análisis de Ahorro**: Ingrese el consumo promedio del cliente para calcular el ahorro total
    
    ### Notas
    - El archivo exportado contiene los periodos resultantes de la comparación
    - El análisis de ahorro calcula el beneficio económico real para el cliente
    """)
    
    st.markdown("---")
    
    st.header("📞 Soporte")
    st.markdown("""
    ### ¿Problemas de acceso?
    Si tienes problemas para acceder al archivo de tarifas:
    
    **📧 Contacta al Analista de Ventas:**
    - Solicita acceso al archivo "Tarifas comparativas.xlsm"
    - Proporciona tu nombre de usuario
    - Indica el motivo del acceso
    
    **🔄 Reintenta la carga** una vez autorizado
    """)
    
    st.markdown("---")
    
    # Información de versión y copyright
    st.markdown("""
    <div style='position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px;'>
    <small>v3.1.0 | © 2026 Ruitoque Energía</small>
    </div>
    """, unsafe_allow_html=True)

# --- SECCIÓN 1: CARGA DE ARCHIVO ---
st.header("1️⃣ Carga de Archivo")

if not st.session_state['archivo_cargado']:
    # Inicializar cliente de SharePoint
    sharepoint_client = SharePointClient(token)
    
    # Variable para controlar si mostrar el botón de reintento
    mostrar_boton_reintento = 'error_carga' in st.session_state
    
    # Solo mostrar botón de reintento si hubo un error previo
    if mostrar_boton_reintento:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 Reintentar Carga", type="secondary", key="reintentar_carga"):
                # Limpiar el flag de error y reintentar
                if 'error_carga' in st.session_state:
                    del st.session_state['error_carga']
                st.rerun()
    
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
                        # Limpiar flag de error si existe
                        if 'error_carga' in st.session_state:
                            del st.session_state['error_carga']
                        st.rerun()
        else:
            # Marcar que hubo un error de carga
            st.session_state['error_carga'] = True
            
            # El error ya fue manejado en SharePointClient._handle_error()
            # Mostramos información adicional y opciones para el usuario
            st.markdown("---")
            st.markdown("""
            ### 📋 **Resumen del Problema**
            La aplicación no pudo acceder al archivo de tarifas debido a permisos insuficientes.
            
            ### 🎯 **Acciones Recomendadas**
            1. **Contacta al Analista de Ventas** para solicitar acceso
            2. **Espera la autorización** del administrador
            3. **Usa el botón "Reintentar Carga"** una vez autorizado
            """)
            
            # Botón de reintento más prominente
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.button("🔄 Reintentar Carga", type="primary", key="reintentar_carga_2")
            
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
    st.header("2️⃣ Comparación de Tarifas y Visualización")
    
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
                    comercializador = st.selectbox('Comercializador 1 (Obligatorio):', options=comercializadores, key='comercializador_selector')
                else:
                    st.error("No hay comercializadores disponibles para este mercado")
                    comercializador = None
            else:
                st.info("Seleccione primero un mercado")
                comercializador = None
        
        with col3:
            if mercado:
                # Obtener niveles de tensión del mercado (no solo del comercializador)
                niveles_tension = sorted([
                    nt for nt in df_procesado[df_procesado['MERCADO']==mercado]['NT'].unique()
                    if pd.notna(nt)
                ])
                if niveles_tension:
                    nt = st.selectbox('Nivel de Tensión:', options=niveles_tension, key='nt_selector')
                else:
                    st.error("No hay niveles de tensión disponibles para este mercado")
                    nt = None
            else:
                st.info("Seleccione primero un mercado")
                nt = None
        
        # Inicializar variables de comercializadores opcionales
        comercializador_2 = None
        comercializador_3 = None
        
        # Selectores de comercializadores opcionales
        if mercado and comercializador and nt:
            st.markdown("---")
            st.subheader("📊 Comercializadores Adicionales (Opcionales)")
            col1, col2 = st.columns(2)
            
            with col1:
                if mercado:
                    comercializadores_opcionales = sorted([
                        c for c in df_procesado[df_procesado['MERCADO']==mercado]['COMERCIALIZADOR'].unique()
                        if pd.notna(c) and c != "RUITOQUE" and c != comercializador
                    ])
                    # Agregar opción "Ninguno" al inicio
                    opciones_com2 = ["Ninguno"] + comercializadores_opcionales
                    comercializador_2 = st.selectbox(
                        'Comercializador 2 (Opcional):', 
                        options=opciones_com2, 
                        key='comercializador_2_selector',
                        index=0
                    )
                    if comercializador_2 == "Ninguno":
                        comercializador_2 = None
            
            with col2:
                if mercado:
                    # Excluir comercializador 1 y comercializador 2 de las opciones
                    excluir = [comercializador]
                    if comercializador_2:
                        excluir.append(comercializador_2)
                    comercializadores_opcionales_3 = sorted([
                        c for c in df_procesado[df_procesado['MERCADO']==mercado]['COMERCIALIZADOR'].unique()
                        if pd.notna(c) and c != "RUITOQUE" and c not in excluir
                    ])
                    # Agregar opción "Ninguno" al inicio
                    opciones_com3 = ["Ninguno"] + comercializadores_opcionales_3
                    comercializador_3 = st.selectbox(
                        'Comercializador 3 (Opcional):', 
                        options=opciones_com3, 
                        key='comercializador_3_selector',
                        index=0
                    )
                    if comercializador_3 == "Ninguno":
                        comercializador_3 = None
        
        if mercado and comercializador and nt:
            # Selectores de periodos
            st.subheader("📅 Selección de Periodos")
            
            # Obtener fechas disponibles solo del comercializador principal (obligatorio)
            # Calcular esto ANTES de las columnas para que esté disponible en ambas
            fechas_disponibles = sorted(
                df_procesado[
                    (df_procesado['MERCADO'] == mercado) & 
                    (df_procesado['COMERCIALIZADOR'] == comercializador) &
                    (df_procesado['NT'] == nt)
                ]['FECHA'].unique()
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
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
            if periodo_inicio and periodo_fin and fechas_disponibles:
                if periodo_inicio > periodo_fin:
                    st.warning("⚠️ El periodo de inicio debe ser menor o igual al periodo final")
                else:
                    # Calcular cuántos periodos hay en el rango seleccionado
                    fechas_rango = [fecha for fecha in fechas_disponibles if periodo_inicio <= fecha <= periodo_fin]
                    num_periodos = len(fechas_rango)
                    st.info(f"📊 Analizando periodos desde {periodo_inicio} hasta {periodo_fin} ({num_periodos} periodos seleccionados)")
            
            if st.button('▶️ Ejecutar Comparación', type='primary', key='ejecutar_btn'):
                if periodo_inicio and periodo_fin and periodo_inicio <= periodo_fin:
                    # Lista de comercializadores a comparar
                    comercializadores_a_comparar = [comercializador]
                    if comercializador_2:
                        comercializadores_a_comparar.append(comercializador_2)
                    if comercializador_3:
                        comercializadores_a_comparar.append(comercializador_3)
                    
                    with st.spinner(f'Ejecutando comparación de tarifas con {len(comercializadores_a_comparar)} comercializador(es)...'):
                        resultados_comparacion = {}
                        mensajes_analisis = {}
                        comercializadores_sin_datos = []
                        
                        # Ejecutar comparación para cada comercializador
                        for com in comercializadores_a_comparar:
                            df_resultado = comparar_cu(df_procesado, mercado, com, nt, periodo_inicio, periodo_fin)
                            if df_resultado is not None:
                                resultados_comparacion[com] = df_resultado
                                # Capturar mensajes inmediatamente después de la comparación
                                if 'mensajes_analisis' in st.session_state:
                                    mensajes_temp = st.session_state['mensajes_analisis']
                                    # Si es una lista (formato antiguo), guardarla directamente
                                    if isinstance(mensajes_temp, list):
                                        mensajes_analisis[com] = mensajes_temp.copy()
                                    else:
                                        # Si ya es un diccionario, tomar el valor para este comercializador
                                        mensajes_analisis[com] = mensajes_temp.get(com, [])
                                else:
                                    mensajes_analisis[com] = []
                            else:
                                # Si es un comercializador opcional, solo registrar que no tiene datos
                                if com != comercializador:
                                    comercializadores_sin_datos.append(com)
                    
                    # Validar que al menos el comercializador principal tenga resultados
                    if comercializador in resultados_comparacion:
                        if comercializadores_sin_datos:
                            st.warning(f"⚠️ Los siguientes comercializadores opcionales no tienen datos en el rango seleccionado: {', '.join(comercializadores_sin_datos)}")
                        
                        st.session_state['resultados_comparacion'] = resultados_comparacion
                        st.session_state['mensajes_analisis'] = mensajes_analisis
                        st.session_state['comercializador_activo'] = comercializador  # Por defecto el primero
                        st.session_state['df_resultado'] = resultados_comparacion[comercializador]  # Resultado por defecto
                        st.session_state['mostrar_resultados'] = True
                        st.session_state['parametros_comparacion'] = {
                            'mercado': mercado,
                            'comercializadores': list(resultados_comparacion.keys()),  # Solo los que tienen datos
                            'nt': nt,
                            'periodo_inicio': periodo_inicio,
                            'periodo_fin': periodo_fin
                        }
                        st.rerun()
                    else:
                        st.error("❌ No se pudo ejecutar la comparación con el comercializador principal. Verifique los datos y el rango de periodos seleccionado.")
    else:
        # Mostrar parámetros de la comparación
        st.subheader("Parámetros de la comparación:")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.info(f"🏢 Mercado: {st.session_state['parametros_comparacion']['mercado']}")
        with col2:
            comercializadores_str = ", ".join(st.session_state['parametros_comparacion']['comercializadores'])
            st.info(f"🏪 Comercializadores: {comercializadores_str}")
        with col3:
            st.info(f"⚡ Nivel de Tensión: {st.session_state['parametros_comparacion']['nt']}")
        with col4:
            st.info(f"📅 Periodos: {st.session_state['parametros_comparacion']['periodo_inicio']} - {st.session_state['parametros_comparacion']['periodo_fin']}")

        # Selector de comercializador activo
        if len(st.session_state['parametros_comparacion']['comercializadores']) > 1:
            st.markdown("---")
            st.subheader("🔀 Seleccionar Comercializador para Visualizar")
            comercializador_activo = st.selectbox(
                'Comercializador a visualizar:',
                options=st.session_state['parametros_comparacion']['comercializadores'],
                key='selector_comercializador_activo',
                index=st.session_state['parametros_comparacion']['comercializadores'].index(
                    st.session_state.get('comercializador_activo', st.session_state['parametros_comparacion']['comercializadores'][0])
                ) if st.session_state.get('comercializador_activo') in st.session_state['parametros_comparacion']['comercializadores'] else 0
            )
            # Verificar si cambió el comercializador activo
            comercializador_anterior = st.session_state.get('comercializador_activo')
            st.session_state['comercializador_activo'] = comercializador_activo
            
            # Si cambió el comercializador, limpiar el resultado filtrado
            if comercializador_anterior != comercializador_activo:
                st.session_state['df_resultado_filtrado'] = None
            
            # Actualizar df_resultado con el comercializador activo
            if comercializador_activo in st.session_state['resultados_comparacion']:
                st.session_state['df_resultado'] = st.session_state['resultados_comparacion'][comercializador_activo]
        else:
            st.session_state['comercializador_activo'] = st.session_state['parametros_comparacion']['comercializadores'][0]
            # Asegurar que df_resultado esté actualizado
            if st.session_state['comercializador_activo'] in st.session_state.get('resultados_comparacion', {}):
                st.session_state['df_resultado'] = st.session_state['resultados_comparacion'][st.session_state['comercializador_activo']]

        # Mostrar mensajes del análisis para el comercializador activo
        st.subheader("📊 Análisis Periodo a Periodo")
        comercializador_activo = st.session_state['comercializador_activo']
        if comercializador_activo in st.session_state.get('mensajes_analisis', {}):
            for mensaje in st.session_state['mensajes_analisis'][comercializador_activo]:
                st.write(mensaje)

        # Mostrar resultados
        if st.session_state['df_resultado'] is not None:
            st.subheader("📈 Resultados Detallados")
            st.dataframe(st.session_state['df_resultado'])
            
            # Obtener fechas disponibles para el slider
            fechas_disponibles = sorted(st.session_state['df_resultado']['FECHA'].unique())
            
            # Verificar que tenemos fechas válidas antes de continuar
            if not fechas_disponibles:
                st.error("❌ No hay fechas disponibles para mostrar en el slider")
                st.stop()
            
            # Inicializar valores del slider si no existen o si no están en las fechas disponibles
            if (st.session_state['slider_periodo_inicio'] is None or 
                st.session_state['slider_periodo_inicio'] not in fechas_disponibles):
                st.session_state['slider_periodo_inicio'] = fechas_disponibles[0]
            
            if (st.session_state['slider_periodo_fin'] is None or 
                st.session_state['slider_periodo_fin'] not in fechas_disponibles):
                st.session_state['slider_periodo_fin'] = fechas_disponibles[-1]
            
            # Slider para seleccionar rango de periodos
            st.subheader("🎛️ Ajustar Rango de Periodos")
            
            # Slider de rango con periodos como opciones
            slider_range = st.select_slider(
                'Seleccionar rango de periodos:',
                options=fechas_disponibles,
                value=(st.session_state['slider_periodo_inicio'], st.session_state['slider_periodo_fin']),
                key='periodo_slider'
            )
            
            # Extraer fechas del slider
            slider_inicio = slider_range[0]
            slider_fin = slider_range[1]
            
            # Mostrar información del rango seleccionado
            st.caption(f"📅 Periodo seleccionado: {slider_inicio} a {slider_fin} ({len([f for f in fechas_disponibles if slider_inicio <= f <= slider_fin])} periodos)")
            
            # Actualizar valores del slider
            st.session_state['slider_periodo_inicio'] = slider_inicio
            st.session_state['slider_periodo_fin'] = slider_fin
            
            # Calcular promedios para todos los comercializadores
            st.subheader("📊 Promedios del Periodo Seleccionado")
            
            # Calcular promedios para cada comercializador
            todos_promedios = {}
            for com in st.session_state['parametros_comparacion']['comercializadores']:
                if com in st.session_state['resultados_comparacion']:
                    df_com = st.session_state['resultados_comparacion'][com]
                    promedios = calcular_promedios_periodo(
                        df_com, 
                        st.session_state['slider_periodo_inicio'], 
                        st.session_state['slider_periodo_fin']
                    )
                    todos_promedios[com] = promedios
            
            # Mostrar una fila por cada comercializador
            for idx, com in enumerate(st.session_state['parametros_comparacion']['comercializadores']):
                if com in todos_promedios:
                    promedios = todos_promedios[com]
                    st.markdown(f"**{com}**")
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric(
                            f"Promedio RUITOQUE", 
                            f"${promedios['promedio_rtq']:,.2f}",
                            help="Promedio del Costo Unitario de RUITOQUE en el periodo seleccionado"
                        )
                    
                    with col2:
                        st.metric(
                            f"Promedio {promedios['comercializador']}", 
                            f"${promedios['promedio_competidor']:,.2f}",
                            help=f"Promedio del Costo Unitario de {promedios['comercializador']} en el periodo seleccionado"
                        )
                    
                    with col3:
                        # Lógica de colores:
                        # - diferencia_absoluta > 0: RUITOQUE es más barato → porcentaje positivo → verde ("normal")
                        # - diferencia_absoluta < 0: RUITOQUE es más caro → porcentaje negativo → rojo ("normal" muestra rojo para negativos)
                        # Streamlit: "normal" = verde para positivos, rojo para negativos
                        #           "inverse" = rojo para positivos, verde para negativos
                        # Como queremos: verde cuando RUITOQUE es mejor, rojo cuando es peor
                        # y el signo del porcentaje coincide con esto, usamos "normal"
                        diferencia_color = "normal"
                        
                        st.metric(
                            "Diferencia Absoluta", 
                            f"${promedios['diferencia_absoluta']:,.2f}",
                            delta=f"{promedios['diferencia_porcentual']:+.2f}%",
                            delta_color=diferencia_color,
                            help="Diferencia absoluta y porcentual entre promedios (positivo = RUITOQUE más competitivo, negativo = RUITOQUE menos competitivo)"
                        )
                    
                    with col4:
                        st.metric(
                            "Periodos Analizados", 
                            f"{promedios['periodos_analizados']}",
                            help="Número de periodos incluidos en el análisis actual"
                        )
                    
                    if idx < len(st.session_state['parametros_comparacion']['comercializadores']) - 1:
                        st.markdown("---")
            
            # Filtrar datos para el gráfico
            df_filtrado = filtrar_resultados_por_periodo(
                st.session_state['df_resultado'],
                st.session_state['slider_periodo_inicio'],
                st.session_state['slider_periodo_fin']
            )
            st.session_state['df_resultado_filtrado'] = df_filtrado
            
            # Crear y mostrar gráfico con todos los comercializadores
            fig = crear_grafico_comparacion_multiple(
                st.session_state['resultados_comparacion'],
                st.session_state['slider_periodo_inicio'],
                st.session_state['slider_periodo_fin']
            )
            if fig:
                st.plotly_chart(fig, use_container_width=True)
            
            # Botones de acción (después del gráfico)
            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                # Descargar archivos para cada comercializador
                st.subheader("📥 Descargar Resultados")
                
                for com in st.session_state['parametros_comparacion']['comercializadores']:
                    if com in st.session_state['resultados_comparacion']:
                        df_com = st.session_state['resultados_comparacion'][com]
                        
                        # Filtrar datos para el periodo seleccionado
                        df_filtrado_com = filtrar_resultados_por_periodo(
                            df_com,
                            st.session_state['slider_periodo_inicio'],
                            st.session_state['slider_periodo_fin']
                        )
                        
                        # Crear archivo Excel
                        output = io.BytesIO()
                        df_filtrado_com.to_excel(output, index=False, sheet_name="Comparacion", engine='openpyxl')
                        output.seek(0)
                        
                        # Generar nombre de archivo
                        nombre_archivo = f"comparacion_cu_{st.session_state['parametros_comparacion']['mercado']}_{com}_{st.session_state['parametros_comparacion']['nt']}_{st.session_state['slider_periodo_inicio']}_{st.session_state['slider_periodo_fin']}.xlsx"
                        
                        st.download_button(
                            label=f"📥 Descargar {com}",
                            data=output.getvalue(),
                            file_name=nombre_archivo,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            key=f'descargar_btn_{com}',
                            help=f"Descarga los resultados de la comparación con {com} para el periodo {st.session_state['slider_periodo_inicio']} a {st.session_state['slider_periodo_fin']}"
                        )
            
            with col2:
                if st.button('🔄 Nueva Comparación', key='nueva_comparacion'):
                    reset_comparacion()
                    st.rerun()
            
            # --- SECCIÓN 3: ANÁLISIS DE AHORRO ---
            st.markdown("---")
            st.header("3️⃣ Análisis de Ahorro")
            
            st.info("""
            **💡 ¿Qué hace esta sección?**
            
            Calcula el **ahorro económico real** que tendría un cliente si cambia de su comercializador actual a RUITOQUE, 
            basándose en su consumo promedio mensual y los precios del periodo seleccionado.
            
            **📊 Fórmula del Ahorro:**
            ```
            Ahorro Total = Σ(CU_mes_n_COMERCIALIZADOR × Consumo_Promedio) - Σ(CU_mes_n_RUITOQUE × Consumo_Promedio)
            ```
            """)
            
            # Selector de comercializador y inputs para análisis de ahorro
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                # Selector de comercializador para el análisis de ahorro
                comercializadores_disponibles = st.session_state['parametros_comparacion']['comercializadores']
                
                # Determinar el índice por defecto
                if st.session_state.get('comercializador_ahorro') in comercializadores_disponibles:
                    default_index = comercializadores_disponibles.index(st.session_state['comercializador_ahorro'])
                else:
                    default_index = 0
                
                comercializador_ahorro = st.selectbox(
                    'Comercializador:',
                    options=comercializadores_disponibles,
                    key='selector_comercializador_ahorro',
                    index=default_index,
                    help="Seleccione el comercializador para calcular el análisis de ahorro"
                )
                # Guardar el comercializador seleccionado
                comercializador_anterior = st.session_state.get('comercializador_ahorro')
                st.session_state['comercializador_ahorro'] = comercializador_ahorro
                
                # Si cambió el comercializador, limpiar resultados previos
                if comercializador_anterior and comercializador_anterior != comercializador_ahorro:
                    st.session_state['mostrar_analisis_ahorro'] = False
                    st.session_state['resultados_ahorro'] = None
            
            with col2:
                consumo_promedio = st.number_input(
                    'Consumo promedio mensual del cliente (kWh):',
                    min_value=1.0,
                    max_value=1000000.0,
                    value=st.session_state.get('consumo_promedio_kwh', 1000.0),
                    step=100.0,
                    help="Ingrese el consumo promedio mensual en kilowatt-hora del cliente"
                )
                st.session_state['consumo_promedio_kwh'] = consumo_promedio
            
            with col3:
                st.markdown("")
                st.markdown("")
                if st.button('💰 Calcular Ahorro', type='primary', key='calcular_ahorro_btn'):
                    # Obtener el DataFrame del comercializador seleccionado
                    if comercializador_ahorro in st.session_state['resultados_comparacion']:
                        df_resultado_ahorro = st.session_state['resultados_comparacion'][comercializador_ahorro]
                        
                        with st.spinner('Calculando análisis de ahorro...'):
                            resultados_ahorro = calcular_ahorro_energia(
                                df_resultado_ahorro,
                                st.session_state['slider_periodo_inicio'],
                                st.session_state['slider_periodo_fin'],
                                consumo_promedio
                            )
                            
                            if resultados_ahorro:
                                st.session_state['resultados_ahorro'] = resultados_ahorro
                                st.session_state['mostrar_analisis_ahorro'] = True
                                st.success("✅ Análisis de ahorro calculado exitosamente")
                                st.rerun()
                            else:
                                st.error("❌ No se pudo calcular el análisis de ahorro. Verifique los datos.")
                    else:
                        st.error(f"❌ No hay datos disponibles para {comercializador_ahorro}")
            
            with col4:
                st.markdown("")
                st.markdown("")
                if st.button('🔄 Reiniciar Análisis', key='reiniciar_ahorro_btn'):
                    st.session_state['mostrar_analisis_ahorro'] = False
                    st.session_state['resultados_ahorro'] = None
                    st.rerun()
            
            # Mostrar resultados del análisis de ahorro si están disponibles
            if st.session_state.get('mostrar_analisis_ahorro') and st.session_state.get('resultados_ahorro'):
                mostrar_analisis_ahorro(st.session_state['resultados_ahorro'])

else:
    st.info("ℹ️ Por favor, primero carga el archivo de tarifas para realizar la comparación.")

# Pie de página
st.markdown("---")
st.markdown(
    "<div style='text-align: left;'>Desarrollado por: <a href='https://github.com/andresbadillo' target='_blank'>andresbadillo.co</a></div>",
    unsafe_allow_html=True
) 