# 📋 Historial de Versiones

## v1.0.0 (Mayo 2024)

### 🎯 Lanzamiento Inicial
- **Concepto Base**: Aplicación para análisis de tarifas de energía
- **Funcionalidad Core**: Comparación de CU entre comercializadores
- **Interfaz Básica**: Interfaz web funcional con Streamlit
- **Procesamiento de Datos**: Carga y procesamiento de archivos Excel

### 📋 Características Iniciales
- Carga de archivos de tarifas
- Selección de parámetros de comparación
- Análisis básico de periodos
- Exportación de resultados

---

## v2.0.0 (Junio 2025)

### 🏗️ Refactorización Mayor
- **Arquitectura Modular**: Reestructuración completa del código en módulos especializados
- **Separación de Responsabilidades**: Autenticación, configuración, procesamiento y visualización separados

### 🔐 Seguridad
- **Autenticación Azure AD**: Integración completa con Azure Active Directory
- **Acceso SharePoint**: Conexión segura a SharePoint para descarga de archivos
- **Manejo de Tokens**: Gestión segura de tokens de autenticación

### 📊 Funcionalidades Core
- **Comparación Automática**: Algoritmo inteligente para comparar CU de RUITOQUE vs competencia
- **Análisis Progresivo**: Evaluación periodo a periodo con lógica de acumulación
- **Métricas Detalladas**: Cálculo de diferencias en pesos ($) y porcentajes (%)

### 📈 Visualización
- **Gráficos Interactivos**: Visualización con Plotly para comparaciones temporales
- **Tablas Dinámicas**: Presentación clara de resultados con métricas calculadas
- **Exportación**: Descarga de resultados en formato Excel

### 🛠️ Tecnologías
- **Streamlit**: Framework web para la interfaz de usuario
- **Pandas**: Procesamiento robusto de datos
- **Plotly**: Visualización interactiva
- **Microsoft Graph API**: Integración con servicios de Microsoft

---

## v2.1.0 (Julio 2025)

### ✨ Nuevas Funcionalidades
- **Selección Manual de Periodos**: Los usuarios ahora pueden seleccionar manualmente el rango de periodos a analizar
- **Valores por Defecto Inteligentes**: Periodo de inicio se establece automáticamente en 2024-01 y periodo final en el último disponible

### 🔧 Mejoras
- **Validación Mejorada**: Validación robusta de rangos de periodos con mensajes informativos
- **Orden Cronológico**: Los selectores de periodos muestran las fechas en orden cronológico correcto
- **Interfaz Mejorada**: Información clara sobre el rango de periodos seleccionado
- **Exportación Mejorada**: Nombres de archivo incluyen el rango de periodos analizado

### 🐛 Correcciones
- **Errores de Linter**: Corregidos errores de tipos en configuración de página
- **Exportación Excel**: Mejorada compatibilidad con versiones recientes de pandas
- **Lógica de Periodos**: Corregido el orden cronológico en toda la aplicación

### 📊 Impacto
- Mayor flexibilidad para análisis de periodos específicos
- Mejor experiencia de usuario con valores por defecto sensatos
- Código más robusto y mantenible

---

**Desarrollado por**: [andresbadillo.co](https://www.andresbadillo.co/)  
**Mantenido por**: Equipo de Desarrollo Ruitoque Energía 