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

## v2.1.1 (Julio 2025)

### 🔧 Mejoras en Experiencia de Usuario
- **Periodo Inicial Inteligente**: El periodo inicial por defecto ahora se establece automáticamente en los últimos 12 meses disponibles
- **Cálculo Preciso**: Garantiza exactamente 12 periodos de análisis, no más ni menos
- **Flexibilidad**: Si hay menos de 12 periodos disponibles, usa todos los periodos existentes

### 📝 Mejoras en Interfaz
- **Texto Más Claro**: Cambio de "Periodo de inicio" a "Periodo inicial" para mayor claridad
- **Instrucciones Mejoradas**: Texto más descriptivo en las instrucciones de uso

### 🎯 Beneficios
- **Análisis Más Relevante**: Siempre analiza los datos más recientes disponibles
- **Consistencia**: Mantiene el periodo final como el más reciente
- **Eficiencia**: Reduce la necesidad de ajuste manual de periodos por parte del usuario

---

## v2.2.1 (Julio 2025)

### ✨ Nueva Funcionalidad de Análisis Completo
- **Análisis de Todos los Periodos**: Ahora incluye todos los periodos del rango seleccionado, no solo los exitosos
- **Transparencia Total**: Muestra tanto periodos donde RUITOQUE es competitivo como aquellos que requieren atención
- **Mensajes Detallados**: Nuevo formato de mensajes con `"❌ {fecha} -> Atención! (PROM_RTQ > PROM_competidor)"`

### 🔧 Mejoras en Resultados
- **Columna ESTADO**: Nueva columna que indica `"✅ Exitoso"` o `"❌ Atención"` para cada periodo
- **Exportación Completa**: Todos los periodos se incluyen en el archivo Excel de resultados
- **Métricas Completas**: Se calculan las diferencias para todos los periodos analizados

### 📊 Visualización Mejorada
- **Marcadores Especiales**: Los periodos de atención se marcan con "X" naranja en el gráfico
- **Leyenda Informativa**: Se muestra una leyenda separada para identificar periodos de atención
- **Análisis Visual**: Fácil identificación de periodos problemáticos en la gráfica

### 🎯 Beneficios del Análisis Completo
- **Toma de Decisiones Informada**: Información completa para estrategias de precios
- **Identificación de Tendencias**: Permite ver patrones de competitividad a lo largo del tiempo
- **Transparencia**: No oculta periodos desfavorables, proporciona visión completa
- **Análisis Estratégico**: Facilita la identificación de oportunidades y amenazas

---

## v2.3.1 (Agosto 2025)

### ✨ Nuevas Funcionalidades Interactivas
- **Indicadores de Promedio en Tiempo Real**: Nuevos indicadores visuales que muestran promedios del periodo seleccionado
- **Selector de Rango de Periodos**: Slider interactivo que permite ajustar el rango de análisis dinámicamente
- **Actualización Automática**: Los indicadores y gráficos se actualizan automáticamente al cambiar el rango

### 📊 Indicadores de Promedio
- **Promedio RUITOQUE**: Muestra el CU promedio de RUITOQUE en el periodo seleccionado
- **Promedio Competidor**: Muestra el CU promedio del competidor seleccionado
- **Diferencia Absoluta**: Calcula la diferencia en pesos y porcentaje entre promedios
- **Periodos Analizados**: Indica cuántos periodos están incluidos en el análisis actual

### 🎛️ Selector de Rango Mejorado
- **Slider Categórico**: Muestra directamente los periodos (YYYY-MM) en lugar de números
- **Selección Intuitiva**: Un solo clic para seleccionar periodo inicial y final
- **Información Clara**: Muestra el rango seleccionado y número de periodos incluidos
- **Interfaz Limpia**: Eliminada información redundante para mejor experiencia de usuario

### 📈 Visualización Dinámica
- **Gráfico Adaptativo**: El gráfico se filtra automáticamente según el rango seleccionado
- **Indicadores Reactivos**: Los promedios se recalculan en tiempo real
- **Exportación Filtrada**: El archivo Excel se descarga con solo los datos del rango seleccionado

### 🔧 Mejoras Técnicas
- **Estado de Sesión Mejorado**: Nuevos parámetros para manejar el slider y datos filtrados
- **Funciones Utilitarias**: Nuevas funciones para calcular promedios y filtrar resultados
- **Código Modular**: Mejor organización del código con funciones especializadas
- **Compatibilidad**: Mantiene compatibilidad con todas las funcionalidades existentes

### 📋 Manual de Usuario Actualizado
- **Documentación Completa**: Manual actualizado con todas las nuevas funcionalidades
- **Casos de Uso**: Nuevos ejemplos de uso para análisis dinámico
- **Instrucciones Detalladas**: Guía paso a paso para usar el slider y indicadores
- **Consejos Prácticos**: Recomendaciones para ejecutivos de ventas

### 🎯 Beneficios para Ejecutivos de Ventas
- **Análisis Granular**: Pueden enfocarse en periodos específicos relevantes para el cliente
- **Presentaciones Dinámicas**: Pueden ajustar el rango durante la presentación
- **Datos Precisos**: Exportan solo la información relevante para cada caso
- **Insights Rápidos**: Los promedios se calculan automáticamente para cualquier rango

### 🚀 Experiencia de Usuario Mejorada
- **Más Intuitivo**: El slider es más natural de usar que los selectores anteriores
- **Feedback Visual**: Ve inmediatamente el rango seleccionado y los resultados
- **Eficiencia**: Menos clics para ajustar el rango de análisis
- **Claridad**: Información contextual sobre el número de periodos

---

**Desarrollado por**: [andresbadillo.co](https://www.andresbadillo.co/)  
**Mantenido por**: Equipo de Desarrollo Ruitoque Energía 