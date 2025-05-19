"""Módulo para manejar los estilos CSS de la aplicación."""

CUSTOM_CSS = """
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        width: 100%;
    }
    .reportview-container {
        background: #f0f2f6
    }
    .titulo-principal {
        text-align: center;
        font-size: 2.5rem;
        padding: 1rem 0;
    }
    [data-testid="stSidebar"] {
        background-color: #133145;
    }
    [data-testid="stSidebar"] > div:first-child {
        background-color: #133145;
    }
    [data-testid="stSidebarNav"] {
        background-color: #133145;
    }
    .st-emotion-cache-1cypcdb {
        background-color: #133145;
        color: white;
    }
    .st-emotion-cache-1cypcdb a {
        color: white;
    }
    .st-emotion-cache-1cypcdb small {
        color: #e6e6e6;
    }
    /* Forzar color blanco en todo el texto del sidebar */
    section[data-testid="stSidebar"] * {
        color: #ff4 !important;
    }
    </style>
""" 