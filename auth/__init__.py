"""
Módulo de autenticación para la aplicación de análisis de tarifas.
Incluye autenticación con Azure AD y acceso a SharePoint.
"""

from .azure_auth import AzureAuth
from .sharepoint import SharePointClient

__all__ = ['AzureAuth', 'SharePointClient'] 