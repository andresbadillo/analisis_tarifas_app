"""Módulo para las constantes de la aplicación."""

# Configuración de la página
PAGE_CONFIG = {
    "page_title": "Análisis de Tarifas - Ruitoque Energía",
    "page_icon": "assets/Isotipo.png",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "menu_items": None
}

# Estado inicial de la sesión
INITIAL_SESSION_STATE = {
    'archivo_cargado': False,
    'df_tarifas': None,
    'mostrar_resultados': False,
    'df_resultado': None,
    'resultados_comparacion': {},  # Diccionario con resultados por comercializador
    'comercializador_activo': None,  # Comercializador actualmente visualizado
    'parametros_comparacion': {},
    'mensajes_analisis': {},
    'slider_periodo_inicio': None,
    'slider_periodo_fin': None,
    'df_resultado_filtrado': None,
    'error_carga': False,
    'mostrar_analisis_ahorro': False,
    'resultados_ahorro': None,
    'consumo_promedio_kwh': None,
    'comercializador_ahorro': None,
    'comercializador_ahorro_anterior': None
}

# Columnas necesarias para el análisis
REQUIRED_COLUMNS = {'MERCADO', 'AÑO', 'FECHA', 'COMERCIALIZADOR', 'NT', 'G', 'C', 'CU'}

# Orden de las columnas en el DataFrame
COLUMN_ORDER = ['AÑO', 'FECHA', 'MERCADO', 'COMERCIALIZADOR', 'NT', 'G', 'C', 'CU']

# Columnas numéricas que requieren conversión
NUMERIC_COLUMNS = ['G', 'C', 'CU']

# Colores para el gráfico
COLORS = {
    'RUITOQUE': '#64B43F',
    'OTROS': '#FF4B4B',
    'GRID': 'LightGray'
} 