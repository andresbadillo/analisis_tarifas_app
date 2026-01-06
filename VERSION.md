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

## v2.3.2 (Agosto 2025)

### 🚫 Mejora en Manejo de Errores de Permisos
- **Mensajes de Error Amigables**: Reemplazados los mensajes técnicos por explicaciones claras y orientadas al usuario
- **Guía de Acción Específica**: Instrucciones claras sobre cómo contactar al Analista de Ventas para solicitar permisos
- **Información Contextual**: Explicación de las posibles causas del error de permisos

### 🔄 Funcionalidad de Reintento
- **Botón de Reintento Inteligente**: Botón "🔄 Reintentar Carga" solo aparece cuando hay un error de carga
- **Control de Estado**: Sistema de flags para controlar cuándo mostrar el botón de reintento
- **Limpieza Automática**: El flag de error se limpia automáticamente cuando la carga es exitosa
- **Experiencia Fluida**: No es necesario recargar toda la página para reintentar

### 📞 Información de Soporte Mejorada
- **Sección de Soporte en Sidebar**: Nueva sección con información de contacto y guía de solución de problemas
- **Instrucciones Claras**: Pasos específicos para solicitar acceso al archivo
- **Información Técnica Separada**: Detalles técnicos ocultos en expanders para no abrumar al usuario

### 🔧 Mejoras Técnicas en Manejo de Errores
- **Manejo Específico por Código de Error**: Diferentes mensajes para error 403 vs otros errores
- **Información Técnica para Administradores**: Detalles técnicos disponibles en expanders para debugging
- **Estructura de Mensajes Mejorada**: Uso de markdown para mejor formato y legibilidad

### 📋 Documentación de Troubleshooting
- **Nuevo Archivo TROUBLESHOOTING.md**: Guía completa de solución de problemas
- **Checklist de Verificación**: Lista de verificación antes de contactar soporte
- **Instrucciones para Administradores**: Guía para otorgar permisos en SharePoint y Azure AD
- **Contactos de Soporte**: Información de contacto organizada por tipo de usuario

### 🎯 Beneficios para Usuarios
- **Menos Confusión**: Mensajes claros sobre qué hacer cuando no tienen permisos
- **Proceso Claro**: Instrucciones paso a paso para obtener acceso
- **Menos Tiempo de Resolución**: Información específica sobre a quién contactar
- **Mejor Experiencia**: No se sienten perdidos cuando encuentran un error

### 🎯 Beneficios para Administradores
- **Información Técnica Disponible**: Detalles de debugging sin abrumar al usuario final
- **Guía de Resolución**: Instrucciones claras para otorgar permisos
- **Menos Tickets de Soporte**: Usuarios pueden resolver problemas comunes por sí mismos
- **Documentación Estructurada**: Guía de troubleshooting organizada y fácil de seguir

---

## v2.4.0 (Septiembre 2025)

### ✨ Nueva Funcionalidad: Análisis de Ahorro Económico
- **Cálculo de Beneficio Real**: Nueva funcionalidad que calcula el ahorro económico real que tendría un cliente al cambiar a RUITOQUE
- **Fórmula Matemática Completa**: Implementación de la fórmula Σ(CU_mes_n × Consumo_Promedio)_Competidor - Σ(CU_mes_n × Consumo_Promedio)_RUITOQUE
- **Input de Consumo del Cliente**: Campo para ingresar el consumo promedio mensual en kWh del cliente
- **Métricas de Ahorro**: Cálculo de ahorro total, mensual promedio y por kWh

### 📊 Visualización Detallada del Ahorro
- **Tabla de Detalle por Periodo**: Muestra costos mensuales para cada comercializador por periodo
- **Resumen de Sumatoria**: Visualización clara de las sumatorias totales y el resultado final
- **Explicación Matemática**: Fórmulas y cálculos paso a paso con valores numéricos
- **Manejo de Casos**: Diferencia entre ahorro (verde) y costo adicional (rojo)

### 🔧 Mejoras en la Arquitectura
- **Nuevo Módulo**: `utils/savings_analysis.py` para análisis de ahorro
- **Validación Robusta**: Compatibilidad con estructura de datos de sufijos (CU_RTQ, CU_COMPETIDOR)
- **Manejo Inteligente**: Identificación automática de competidores en diferentes formatos
- **Estado de Sesión Mejorado**: Nuevas variables para controlar el análisis de ahorro

### 📱 Reorganización de la Interfaz
- **Flujo Optimizado**: Botones de acción (Descargar/Nueva Comparación) después del gráfico
- **Análisis de Ahorro Opcional**: Paso adicional que no interrumpe el flujo principal
- **Información Contextual**: Explicación clara del propósito de cada sección
- **Botones Intuitivos**: Botones de calcular, reiniciar y visualizar resultados

### 🎯 Casos de Uso para Ventas
- **Propuesta de Cambio**: Cálculo preciso del beneficio económico para clientes actuales
- **Análisis por Consumo**: Comparación de beneficios para diferentes tipos de clientes
- **Justificación de Precios**: Demostración del valor a largo plazo vs periodos específicos
- **Presentaciones Comerciales**: Datos concretos para argumentos de venta

### 🐛 Correcciones Técnicas
- **Error de COMERCIALIZADOR**: Solucionado problema de compatibilidad con estructura de datos
- **Validación de Columnas**: Verificación robusta de la estructura del DataFrame
- **Manejo de Errores**: Mejor gestión de casos edge y datos inconsistentes

### 📋 Documentación Actualizada
- **README.md**: Actualizado con nueva funcionalidad y estructura del proyecto
- **MANUAL_USUARIO.md**: Guía completa del análisis de ahorro con casos de uso
- **Changelog**: Historial detallado de todas las mejoras y correcciones

### 🚀 Beneficios para Ejecutivos de Ventas
- **Argumentos Concretos**: Números precisos del beneficio económico para cada cliente
- **Análisis Personalizado**: Cálculos basados en el consumo real del cliente
- **Presentaciones Profesionales**: Datos detallados y visualizaciones claras
- **Toma de Decisiones**: Información completa para estrategias de precios

---

## v3.1.0 (Enero 2026)

### ✨ Nueva Funcionalidad: Comparación Múltiple de Comercializadores
- **Múltiples Comercializadores**: Ahora se pueden comparar hasta 3 comercializadores simultáneamente (1 obligatorio + 2 opcionales)
- **Selectores Opcionales**: Nuevos selectores para "Comercializador 2 (Opcional)" y "Comercializador 3 (Opcional)"
- **Validación Inteligente**: Los selectores opcionales excluyen automáticamente los comercializadores ya seleccionados
- **Fechas Disponibles**: La selección de periodos se basa en el comercializador principal, asegurando compatibilidad

### 🔀 Selector de Comercializador Activo
- **Visualización Dinámica**: Selector para cambiar entre comercializadores y ver el análisis periodo a periodo de cada uno
- **Resultados Detallados por Comercializador**: Cada comercializador muestra su propio análisis y resultados detallados
- **Ajuste de Rango Unificado**: El slider de periodos funciona igual para todos los comercializadores seleccionados

### 📊 Promedios del Periodo Seleccionado Mejorados
- **Múltiples Filas de Promedios**: Muestra una fila de promedios por cada comercializador seleccionado (1 a 3 filas)
- **Métricas Completas**: Cada fila incluye Promedio RUITOQUE, Promedio del Comercializador, Diferencia Absoluta y Periodos Analizados
- **Colores Correctos**: Los porcentajes negativos (cuando RUITOQUE es más caro) se muestran en rojo correctamente

### 📈 Gráfico de Comparación Múltiple
- **Visualización Unificada**: Nuevo gráfico que muestra RUITOQUE y todos los comercializadores seleccionados en la misma gráfica
- **Colores Distintivos**: Cada comercializador tiene un color único para fácil identificación
- **Leyenda Completa**: Leyenda clara que identifica cada línea del gráfico
- **Análisis Comparativo**: Permite comparar visualmente el comportamiento de múltiples comercializadores simultáneamente

### 📥 Descarga de Resultados Mejorada
- **Archivos Separados**: Genera un archivo Excel por cada comercializador seleccionado
- **Nombres Descriptivos**: Cada archivo incluye el nombre del comercializador en el nombre del archivo
- **Datos Filtrados**: Cada archivo contiene solo los datos del periodo seleccionado en el slider
- **Botones Organizados**: Todos los botones de descarga agrupados en una sección clara

### 💰 Análisis de Ahorro Mejorado
- **Selector de Comercializador**: Nuevo selector al inicio de la sección para elegir el comercializador a analizar
- **Layout Mejorado**: Todos los elementos (selector, input, botones) en 4 columnas del mismo ancho
- **Análisis por Comercializador**: El análisis se calcula específicamente para el comercializador seleccionado
- **Reinicio Inteligente**: Al reiniciar, se puede cambiar de comercializador sin perder la selección

### 🔧 Mejoras Técnicas en Comparación
- **Manejo de Duplicados**: Agrupación automática por FECHA para promediar valores cuando hay múltiples registros
- **Mensajes Informativos**: Información sobre periodos que solo están en un comercializador (no se incluyen)
- **Validación Mejorada**: Verificación de datos disponibles antes de ejecutar comparaciones
- **Estado de Sesión Expandido**: Nuevas variables para manejar múltiples resultados y comercializadores activos

### 🎨 Correcciones de Visualización
- **Colores de Porcentajes**: Corregida la lógica de colores para mostrar rojo cuando RUITOQUE es más caro (porcentaje negativo)
- **Consistencia Visual**: Todos los porcentajes negativos se muestran en rojo en toda la aplicación
- **Indicadores Claros**: Diferenciación visual clara entre ahorro (verde) y costo adicional (rojo)

### 🐛 Correcciones de Bugs
- **Selección de Periodos**: Corregido el cálculo de fechas disponibles para basarse solo en el comercializador principal
- **Periodos Omitidos**: Solucionado problema de periodos que se saltaban en el análisis por duplicados
- **Manejo de Errores**: Mejorado el manejo cuando comercializadores opcionales no tienen datos en el rango seleccionado

### 📋 Arquitectura Mejorada
- **Nuevas Funciones**: `crear_grafico_comparacion_multiple()` para gráficos con múltiples comercializadores
- **Estado de Sesión**: Estructura mejorada para manejar `resultados_comparacion` como diccionario
- **Mensajes de Análisis**: Almacenamiento de mensajes por comercializador para mejor organización
- **Código Modular**: Mejoras en la organización del código para soportar múltiples comparaciones

### 🎯 Beneficios para Ejecutivos de Ventas
- **Comparación Simultánea**: Pueden comparar RUITOQUE con múltiples competidores al mismo tiempo
- **Análisis Completo**: Visualización clara de cómo RUITOQUE se compara con varios comercializadores
- **Presentaciones Eficientes**: Un solo análisis muestra múltiples comparaciones
- **Análisis de Ahorro Flexible**: Pueden calcular el ahorro para diferentes comercializadores sin reiniciar todo

### 🚀 Experiencia de Usuario Mejorada
- **Interfaz Más Completa**: Opción de agregar comercializadores adicionales sin complicar el flujo principal
- **Navegación Intuitiva**: Selector claro para cambiar entre visualizaciones de diferentes comercializadores
- **Información Contextual**: Mensajes claros sobre qué periodos se están analizando y por qué
- **Flexibilidad**: Pueden agregar o quitar comercializadores opcionales según necesidad

---

**Desarrollado por**: [andresbadillo.co](https://www.andresbadillo.co/)  
**Mantenido por**: Equipo de Desarrollo Ruitoque Energía 