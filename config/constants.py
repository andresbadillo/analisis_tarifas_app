"""Módulo para las constantes de la aplicación."""

# Configuración de la página
PAGE_CONFIG = {
    "page_title": "Análisis de Tarifas - Ruitoque",
    "page_icon": "assets/Isotipo.png",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Estado inicial de la sesión
INITIAL_SESSION_STATE = {
    'archivo_cargado': False,
    'df_tarifas': None,
    'mostrar_resultados': False,
    'df_resultado': None,
    'parametros_comparacion': {},
    'mensajes_analisis': []
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