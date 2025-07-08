"""
Configuración centralizada para la aplicación de análisis de tarifas.
Incluye configuraciones de Azure AD y SharePoint.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Azure Configuration
AZURE_CONFIG = {
    'client_id': os.getenv("AZURE_CLIENT_ID"),
    'client_secret': os.getenv("AZURE_CLIENT_SECRET"),
    'tenant_id': os.getenv("AZURE_TENANT_ID"),
    'redirect_uri': os.getenv("AZURE_REDIRECT_URI"),
    'scope': "User.Read Sites.Read.All Files.Read.All offline_access"
}

# SharePoint Configuration
SHAREPOINT_CONFIG = {
    'site_id': "ruitoqueesp1.sharepoint.com,5336acc1-e942-418c-8982-91cfacd4ae9a,01a12f77-e104-450c-87d2-db9c56ad451e",
    'file_path': "Tarifas Reguladas/Tarifas comparativas.xlsm"
} 