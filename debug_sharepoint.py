"""
Script para debuggear la conexión con SharePoint y mostrar solo el contenido de la carpeta 'Tarifas Reguladas' dentro de 'Documentos Compartidos'.
"""

import streamlit as st
import requests
from auth.azure_auth import AzureAuth
from config.settings import SHAREPOINT_CONFIG

st.title("🔍 Debug SharePoint - Solo 'Tarifas Reguladas' en 'Documentos Compartidos'")

# 1. Autenticación
st.header("1. Autenticación Azure AD")
azure_auth = AzureAuth()
token = azure_auth.authenticate()

if not token:
    st.error("❌ No se pudo obtener el token de Azure AD")
    st.stop()

st.success("✅ Token obtenido correctamente")
st.write(f"Token: {token[:50]}...")

# 2. Verificar conexión al sitio
st.header("2. Verificar Conexión al Sitio")
headers = {"Authorization": f"Bearer {token}"}
site_id = SHAREPOINT_CONFIG['site_id']

st.write(f"Site ID: {site_id}")

url_site = f"https://graph.microsoft.com/v1.0/sites/{site_id}"
response_site = requests.get(url_site, headers=headers)

if response_site.status_code == 200:
    site_info = response_site.json()
    st.success("✅ Conexión al sitio exitosa")
    st.write("Información del sitio:")
    st.json(site_info)
else:
    st.error(f"❌ Error al conectar al sitio: {response_site.status_code}")
    st.write("Respuesta:", response_site.text)
    st.stop()

# 3. Contenido de la carpeta 'Tarifas Reguladas' en la raíz
st.header("3. Contenido de la carpeta 'Tarifas Reguladas' en la raíz")

def get_folder_id_by_name(parent_id, folder_name):
    url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/items/{parent_id}/children"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        children = response.json().get('value', [])
        for item in children:
            if item.get('folder') and item.get('name') == folder_name:
                return item.get('id')
    return None

def show_folder_content(folder_id):
    url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/items/{folder_id}/children"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        children = response.json().get('value', [])
        st.write("**Contenido de la carpeta 'Tarifas Reguladas':**")
        for item in children:
            item_type = "📁 Carpeta" if item.get('folder') else "📄 Archivo"
            st.write(f"{item_type}: {item.get('name', 'Sin nombre')}")
    else:
        st.write(f"❌ Error al explorar: {response.status_code}")
        st.write(f"Respuesta: {response.text}")

drive_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root"
drive_response = requests.get(drive_url, headers=headers)
if drive_response.status_code == 200:
    root_info = drive_response.json()
    root_id = root_info['id']
    tarifas_reguladas_id = get_folder_id_by_name(root_id, "Tarifas Reguladas")
    if tarifas_reguladas_id:
        show_folder_content(tarifas_reguladas_id)
    else:
        st.warning("No se encontró la carpeta 'Tarifas Reguladas' en la raíz del drive.")
else:
    st.error(f"No se pudo obtener la raíz del drive: {drive_response.status_code}")
    st.write("Respuesta:", drive_response.text) 