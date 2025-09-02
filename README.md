# 📊 Análisis de Tarifas de Energía

Aplicación web para el análisis de tarifas de energía que compara el CU (Costo Unitario) de RUITOQUE frente a otros comercializadores en un rango de periodos específico seleccionable por el usuario.

## 🏗️ Estructura del Proyecto

```
analisis_tarifas_app/
├── auth/                          # Módulo de autenticación
│   ├── __init__.py
│   ├── azure_auth.py             # Autenticación con Azure AD
│   └── sharepoint.py             # Cliente de SharePoint
├── config/                        # Configuración
│   ├── constants.py              # Constantes de la aplicación
│   ├── styles.py                 # Estilos CSS personalizados
│   └── settings.py               # Configuración centralizada
├── utils/                         # Utilidades
│   ├── data_processing.py        # Procesamiento de datos
│   ├── comparison.py             # Lógica de comparación
│   ├── visualization.py          # Visualización de datos
│   └── savings_analysis.py       # Análisis de ahorro económico
├── assets/                        # Recursos estáticos
│   ├── path1310.png
│   ├── Logo1.png
│   └── Isotipo.png
├── app.py                         # Aplicación principal
├── test_connection.py            # Script de prueba de conexión
├── requirements.txt              # Dependencias
├── .env                          # Variables de entorno
├── TROUBLESHOOTING.md            # Guía de solución de problemas
└── README.md                     # Este archivo
```

## 🔐 Autenticación

La aplicación utiliza **Azure AD** para la autenticación de usuarios empresariales y accede automáticamente a **SharePoint** para descargar los archivos de tarifas.

### Configuración Azure AD

1. Registra tu aplicación en [Azure Portal](https://portal.azure.com/)
2. Configura los permisos: `User.Read`, `Sites.Read.All`, `Files.Read.All`
3. Crea un archivo `.env` con las siguientes variables:

```env
AZURE_CLIENT_ID=tu_client_id
AZURE_CLIENT_SECRET=tu_client_secret
AZURE_TENANT_ID=tu_tenant_id
AZURE_REDIRECT_URI=http://localhost:8501/
```

## 🚀 Instalación y Uso

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Configurar variables de entorno
Crea un archivo `.env` con las credenciales de Azure AD.

### 3. Ejecutar la aplicación
```bash
streamlit run app.py
```

### 4. Probar conexión (opcional)
```bash
streamlit run test_connection.py
```

## 📋 Flujo de la Aplicación

1. **Autenticación**: Usuario inicia sesión con Azure AD
2. **Descarga Automática**: El archivo se descarga desde SharePoint
3. **Procesamiento**: Los datos se procesan y transforman
4. **Selección**: Usuario selecciona Mercado, Comercializador y Nivel de Tensión
5. **Selección de Periodos**: Usuario define el rango de periodos a analizar (inicio y final)
6. **Análisis**: Se ejecuta la comparación CU vs RUITOQUE en el rango especificado
7. **Resultados**: Visualización de gráficos y exportación de datos
8. **Análisis de Ahorro**: Cálculo del beneficio económico real para el cliente

## 🛠️ Características Técnicas

### Módulos Principales

#### `auth/azure_auth.py`
- Clase `AzureAuth` para manejar autenticación con Azure AD
- Integración con `streamlit-oauth`
- Manejo de tokens y sesiones

#### `auth/sharepoint.py`
- Clase `SharePointClient` para operaciones con SharePoint
- Descarga de archivos usando Microsoft Graph API
- Manejo robusto de errores y debugging

#### `config/settings.py`
- Configuración centralizada de Azure y SharePoint
- Variables de entorno organizadas
- Configuración de endpoints y permisos

#### `utils/savings_analysis.py`
- **NUEVO**: Análisis completo de ahorro económico
- Cálculo de beneficio real basado en consumo del cliente
- Fórmula: Σ(CU_mes_n × Consumo_Promedio)_Competidor - Σ(CU_mes_n × Consumo_Promedio)_RUITOQUE
- Visualización detallada de costos por periodo
- Métricas de ahorro total, mensual y por kWh

### Dependencias Principales

- `streamlit>=1.31.0`: Framework web
- `streamlit-oauth>=0.1.14`: Autenticación OAuth2
- `pandas>=2.0.0`: Procesamiento de datos
- `plotly>=5.18.0`: Visualización
- `requests>=2.31.0`: API calls
- `python-dotenv>=1.0.0`: Variables de entorno

## 🔧 Desarrollo

### Estructura Modular

La aplicación está diseñada con una arquitectura modular que separa:

- **Autenticación**: Módulo `auth/` independiente
- **Configuración**: Centralizada en `config/`
- **Lógica de Negocio**: En `utils/`
- **Interfaz de Usuario**: En `app.py`

### Beneficios de la Reestructuración

- **Legibilidad**: Código más limpio y organizado
- **Mantenibilidad**: Cambios aislados por módulo
- **Escalabilidad**: Fácil agregar nuevas funcionalidades
- **Testabilidad**: Módulos independientes para testing

## 📞 Soporte

### Problemas Comunes
Si encuentras problemas al usar la aplicación, consulta la [Guía de Solución de Problemas](TROUBLESHOOTING.md) para obtener ayuda.

### Contactos
- **Desarrollado por**: [andresbadillo.co](https://www.andresbadillo.co/)
- **Soporte Técnico**: Consulta la sección de contactos en TROUBLESHOOTING.md

## 📝 Changelog
- **Versiones**: Consulta la sección de version en VERSION.md

---

**Versión**: 2.4.0  
**Última actualización**: 2025 