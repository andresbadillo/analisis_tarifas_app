"""
Script de prueba para verificar la conexión con Azure AD y SharePoint.
"""

import streamlit as st
from auth.azure_auth import AzureAuth
from auth.sharepoint import SharePointClient

st.title("🔧 Prueba de Conexión - Azure AD y SharePoint")

# Prueba de autenticación Azure
st.header("1. Autenticación Azure AD")
azure_auth = AzureAuth()
token = azure_auth.authenticate()

if token:
    st.success("✅ Autenticación con Azure AD exitosa")
    st.write(f"Token obtenido: {token[:50]}...")
    
    # Prueba de conexión SharePoint
    st.header("2. Conexión SharePoint")
    sharepoint_client = SharePointClient(token)
    
    if sharepoint_client.test_connection():
        st.success("✅ Conexión con SharePoint exitosa")
        
        # Prueba de descarga de archivo
        st.header("3. Descarga de Archivo")
        with st.spinner("Descargando archivo de prueba..."):
            archivo_bytes = sharepoint_client.download_file()
            
            if archivo_bytes:
                st.success(f"✅ Archivo descargado exitosamente ({len(archivo_bytes)} bytes)")
            else:
                st.error("❌ Error al descargar el archivo")
    else:
        st.error("❌ Error al conectar con SharePoint")
else:
    st.error("❌ Error en la autenticación con Azure AD") 