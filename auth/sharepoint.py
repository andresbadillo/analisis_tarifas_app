"""
Módulo para interactuar con SharePoint usando Microsoft Graph API.
"""

import streamlit as st
import requests
from config.settings import SHAREPOINT_CONFIG


class SharePointClient:
    """
    Clase para manejar operaciones con SharePoint.
    """
    
    def __init__(self, token):
        """
        Inicializa el cliente de SharePoint.
        
        Args:
            token (str): Token de acceso de Azure AD.
        """
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}"
        }
    
    def download_file(self, site_id=None, file_path=None):
        """
        Descarga un archivo desde SharePoint.
        
        Args:
            site_id (str, optional): ID del sitio de SharePoint. 
                                   Si no se proporciona, usa el configurado por defecto.
            file_path (str, optional): Ruta del archivo en SharePoint.
                                     Si no se proporciona, usa el configurado por defecto.
        
        Returns:
            bytes or None: Contenido del archivo si la descarga es exitosa, None en caso contrario.
        """
        # Usar configuración por defecto si no se proporcionan parámetros
        site_id = site_id or SHAREPOINT_CONFIG['site_id']
        file_path = file_path or SHAREPOINT_CONFIG['file_path']
        
        # Debug: Mostrar información de la consulta
        # st.write("🔍 **Debug SharePoint:**")
        # st.write(f"Site ID: {site_id}")
        # st.write(f"File Path: {file_path}")
        st.write(f"Token válido: {'Sí' if self.token else 'No'}")
        # if self.token:
        #     st.write(f"Token (primeros 50 chars): {self.token[:50]}...")
        
        url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root:/{file_path}:/content"
        # st.write(f"URL completa: {url}")
        
        try:
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                st.success("✅ Archivo descargado exitosamente")
                return response.content
            else:
                self._handle_error(response, url)
                return None
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error de conexión al descargar archivo: {str(e)}")
            return None
    
    def _handle_error(self, response, url):
        """
        Maneja errores de la API de SharePoint.
        
        Args:
            response: Objeto de respuesta de requests.
            url (str): URL que se intentó consultar.
        """
        # Manejo específico para error de permisos (403)
        if response.status_code == 403:
            st.error("🚫 **Error de Permisos**")
            st.markdown("""
            **No tienes permisos para acceder al archivo de tarifas.**
            
            Esto puede deberse a:
            - Tu cuenta no tiene los permisos necesarios para acceder al archivo
            - El archivo requiere autorización específica
            - Tu rol en la organización no incluye acceso a este recurso
            
            **¿Qué hacer?**
            📞 **Contacta al Analista de Ventas** para que autorice tu acceso al archivo:
            - **"Tarifas comparativas.xlsm"** ubicado en **"Tarifas Reguladas"**
            - Proporciona tu nombre de usuario y el motivo del acceso
            - Una vez autorizado, podrás usar la aplicación normalmente
            
            **Información técnica para el administrador:**
            - Archivo: `Tarifas Reguladas/Tarifas comparativas.xlsm`
            - Error: 403 - Access Denied
            - Usuario: Autenticado correctamente, pero sin permisos de archivo
            """)
            
            # Mostrar información técnica solo en modo debug
            with st.expander("🔧 Información técnica (para administradores)"):
                st.write(f"**Código de error:** {response.status_code}")
                try:
                    error_data = response.json()
                    st.write("**Respuesta de error:**", error_data)
                except Exception:
                    st.write("**Respuesta de error (texto):**", response.text)
                st.write("**URL consultada:**", url)
                st.write("**Token (primeros 50 caracteres):**", self.token[:50] + "...")
        
        # Manejo para otros errores
        else:
            st.error(f"❌ **Error al descargar archivo**")
            st.markdown(f"""
            **No se pudo descargar el archivo de SharePoint.**
            
            **Código de error:** {response.status_code}
            
            **Posibles causas:**
            - Problema de conectividad con SharePoint
            - El archivo no existe o fue movido
            - Error temporal del servicio
            
            **Solución:**
            - Verifica tu conexión a internet
            - Intenta nuevamente en unos minutos
            - Si el problema persiste, contacta al administrador del sistema
            """)
            
            # Mostrar información técnica solo en modo debug
            with st.expander("🔧 Información técnica (para administradores)"):
                try:
                    error_data = response.json()
                    st.write("**Respuesta de error:**", error_data)
                except Exception:
                    st.write("**Respuesta de error (texto):**", response.text)
                st.write("**URL consultada:**", url)
                st.write("**Token (primeros 50 caracteres):**", self.token[:50] + "...")
    
    def test_connection(self):
        """
        Prueba la conexión con SharePoint.
        
        Returns:
            bool: True si la conexión es exitosa, False en caso contrario.
        """
        try:
            # Intentar obtener información del sitio
            site_id = SHAREPOINT_CONFIG['site_id']
            url = f"https://graph.microsoft.com/v1.0/sites/{site_id}"
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                return True
            else:
                st.error(f"Error al conectar con SharePoint. Código: {response.status_code}")
                return False
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error de conexión: {str(e)}")
            return False 