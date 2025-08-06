# 📊 Manual de Usuario - Análisis de Tarifas de Energía
## Guía para Ejecutivos de Ventas

---

## 🎯 ¿Qué es esta aplicación?

La **Aplicación de Análisis de Tarifas de Energía** es una herramienta diseñada específicamente para que los ejecutivos de ventas de RUITOQUE puedan comparar nuestros precios (CU - Costo Unitario) con los de la competencia en diferentes mercados, niveles de tensión y periodos de tiempo.

### ¿Por qué es útil para ventas?

- **Análisis competitivo**: Compara directamente nuestros precios con la competencia
- **Identificación de oportunidades**: Detecta periodos donde RUITOQUE es más competitivo
- **Preparación de propuestas**: Obtén datos precisos para presentaciones comerciales
- **Seguimiento temporal**: Analiza tendencias de precios a lo largo del tiempo

---

## 🚀 Primeros Pasos

### 1. Acceso a la Aplicación

1. **Abrir el navegador** y dirigirse a la URL de la aplicación
2. **Iniciar sesión** con sus credenciales corporativas (Azure AD)
3. **Esperar** a que se cargue automáticamente el archivo de tarifas desde SharePoint

### 2. Pantalla Principal

Al cargar la aplicación verá:
- **Logo de RUITOQUE** en la parte superior
- **Título**: "Análisis de Tarifas de Energía"
- **Barra lateral izquierda** con información y instrucciones
- **Sección de carga de archivo** (se ejecuta automáticamente)

---

## 📋 Flujo de Trabajo Paso a Paso

### Paso 1: Carga Automática de Datos ✅

**¿Qué pasa?**
- La aplicación descarga automáticamente el archivo de tarifas desde SharePoint
- Procesa y organiza los datos para el análisis
- Muestra un resumen con estadísticas básicas

**¿Qué verá?**
```
Total Registros: [número]
Mercados: [número]
Comercializadores: [número]
Niveles de Tensión: [número]
```

**Vista previa de datos**: Las últimas 5 filas de información cargada

### Paso 2: Configuración de la Comparación ⚙️

#### 2.1 Selección de Mercado
- **¿Qué es?** El mercado energético donde opera el cliente
- **Opciones disponibles**: Se muestran todos los mercados con datos
- **Recomendación**: Seleccione el mercado donde está su cliente objetivo

#### 2.2 Selección de Comercializador
- **¿Qué es?** La empresa competidora que desea comparar
- **Opciones disponibles**: Todos los comercializadores excepto RUITOQUE
- **Recomendación**: Elija el competidor más relevante para su cliente

#### 2.3 Selección de Nivel de Tensión
- **¿Qué es?** El nivel de tensión eléctrica del cliente
- **Opciones disponibles**: Depende del mercado y comercializador seleccionados
- **Recomendación**: Use el nivel de tensión específico de su cliente

### Paso 3: Selección de Periodos 📅

#### 3.1 Periodo Inicial
- **¿Qué es?** La fecha desde donde comenzar el análisis
- **Por defecto**: Los últimos 12 meses disponibles
- **Recomendación**: 
  - Para análisis recientes: Últimos 6-12 meses
  - Para tendencias largas: Últimos 24 meses

#### 3.2 Periodo Final
- **¿Qué es?** La fecha hasta donde terminar el análisis
- **Por defecto**: El periodo más reciente disponible
- **Recomendación**: Mantenga el periodo más reciente para análisis actuales

### Paso 4: Ejecutar Comparación ▶️

1. **Verificar** que todos los campos estén seleccionados
2. **Hacer clic** en "Ejecutar Comparación"
3. **Esperar** a que se procese el análisis (puede tomar unos segundos)

---

## 📊 Interpretación de Resultados

### Análisis Periodo a Periodo

La aplicación muestra mensajes detallados para cada periodo analizado:

#### ✅ Periodos Exitosos
```
✅ 2024-01 -> Exitoso (per. #1: PROM_RTQ=150.25 < PROM_COMPETIDOR=155.30)
```
**Significado**: En este periodo, RUITOQUE fue más competitivo que la competencia

#### ❌ Periodos de Atención
```
❌ 2024-02 -> Atención! (per. #2: PROM_RTQ=152.40 > PROM_COMPETIDOR=150.80)
```
**Significado**: En este periodo, la competencia fue más competitiva que RUITOQUE

### Tabla de Resultados Detallados

La tabla muestra:
- **FECHA**: Periodo analizado
- **CU_RTQ**: Costo Unitario de RUITOQUE
- **CU_[COMPETIDOR]**: Costo Unitario del competidor
- **ESTADO**: ✅ Exitoso o ❌ Atención
- **G_RTQ/G_[COMPETIDOR]**: Componente de Generación
- **C_RTQ/C_[COMPETIDOR]**: Componente de Comercialización

### Indicadores de Promedio

Después de la tabla de resultados, encontrará indicadores que muestran:

- **Promedio RUITOQUE**: Costo Unitario promedio de RUITOQUE en el periodo seleccionado
- **Promedio [Competidor]**: Costo Unitario promedio del competidor en el periodo seleccionado
- **Diferencia Absoluta**: Diferencia en pesos y porcentaje entre los promedios
- **Periodos Analizados**: Número de periodos incluidos en el análisis actual

### Ajuste de Rango de Periodos

Puede ajustar el rango de periodos para el análisis usando el slider:

- **Slider de rango**: Arrastre los extremos del slider para seleccionar el periodo inicial y final
- **Visualización**: El slider muestra las fechas disponibles y el rango seleccionado
- **Información**: Se muestra automáticamente cuántos periodos están incluidos en el rango

Los indicadores y gráfico se actualizan automáticamente al mover el slider.

### Gráfico Interactivo

El gráfico muestra:
- **Línea verde**: Precios de RUITOQUE
- **Línea roja**: Precios del competidor
- **Marcadores X**: Periodos donde la competencia fue más competitiva
- **Interactividad**: Hover para ver valores exactos
- **Filtrado dinámico**: Se actualiza según el rango de periodos seleccionado

---

## 💼 Casos de Uso para Ventas

### 1. Preparación de Propuestas Comerciales

**Escenario**: Cliente actual considerando cambiar de proveedor

**Proceso**:
1. Seleccione el mercado y nivel de tensión del cliente
2. Compare con el proveedor actual del cliente
3. Analice los últimos 12 meses
4. Identifique periodos donde RUITOQUE fue más competitivo
5. Use estos datos en su presentación

**Ejemplo de argumento**:
*"En los últimos 12 meses, RUITOQUE ha sido más competitivo en 8 de los 12 periodos, ofreciendo un ahorro promedio del 3.2% en su facturación"*

### 2. Análisis de Competencia Específica

**Escenario**: Cliente menciona que otro proveedor le ofrece mejores precios

**Proceso**:
1. Seleccione el competidor mencionado
2. Analice un periodo más amplio (24 meses)
3. Identifique tendencias y patrones
4. Prepare contraargumentos basados en datos

### 3. Seguimiento de Tendencias de Mercado

**Escenario**: Necesita entender cómo evolucionan los precios

**Proceso**:
1. Compare con varios competidores principales
2. Analice periodos largos (24+ meses)
3. Use el slider para ajustar el rango y ver diferentes periodos
4. Observe cómo cambian los promedios al mover el rango
5. Identifique tendencias de mercado
6. Use esta información para estrategias de precios

### 4. Análisis Dinámico con Slider

**Escenario**: Cliente quiere ver el comportamiento en periodos específicos

**Proceso**:
1. Ejecute la comparación inicial
2. Use el slider de "Ajustar Rango de Periodos" para seleccionar el rango deseado
3. Observe cómo cambian los indicadores de promedio en tiempo real
4. Identifique el mejor periodo para mostrar a su cliente
5. Descargue los resultados filtrados para su presentación

---

## 📤 Exportación y Compartir Resultados

### Descargar Resultados

1. **Hacer clic** en "📥 Descargar Resultados"
2. **Se descarga** un archivo Excel con:
   - Todos los datos de la comparación
   - Formato profesional para presentaciones
   - Nombre automático con parámetros de la comparación

### Uso del Archivo Excel

El archivo descargado contiene:
- **Hoja "Comparacion"**: Datos del análisis para el rango de periodos seleccionado
- **Columnas organizadas**: Fácil de leer y presentar
- **Datos filtrados**: Solo incluye los periodos del rango ajustado con el slider
- **Nombre descriptivo**: Incluye información del mercado, competidor y rango de fechas

---

## 🔄 Realizar Nueva Comparación

Para analizar otro escenario:

1. **Hacer clic** en "🔄 Nueva Comparación"
2. **Se reinician** todos los selectores
3. **Seleccionar** nuevos parámetros
4. **Ejecutar** nueva comparación

---

## ⚠️ Consideraciones Importantes

### Limitaciones de Datos
- **Datos históricos**: La aplicación solo analiza datos disponibles
- **Actualización**: Los datos se actualizan según el archivo en SharePoint
- **Cobertura**: No todos los mercados/comercializadores pueden tener datos completos

### Interpretación Cuidadosa
- **Contexto**: Los precios son solo un factor en la decisión del cliente
- **Servicio**: RUITOQUE ofrece valor agregado más allá del precio
- **Relación**: La confianza y servicio al cliente son fundamentales

### Uso Ético
- **Transparencia**: Use los datos de manera honesta y transparente
- **Precisión**: No exagere las diferencias o ahorros
- **Contexto**: Siempre presente los datos en el contexto adecuado

---

## 🆘 Solución de Problemas

### Problema: No se cargan los datos
**Solución**:
- Verificar conexión a internet
- Contactar al administrador del sistema
- Verificar permisos de SharePoint

### Problema: No aparecen opciones en los selectores
**Solución**:
- Verificar que el archivo se cargó correctamente
- Revisar que hay datos para los criterios seleccionados
- Intentar con diferentes combinaciones de mercado/comercializador

### Problema: Error en la comparación
**Solución**:
- Verificar que todos los campos estén seleccionados
- Asegurar que el periodo inicial sea menor al final
- Contactar soporte técnico si persiste

---

## 📞 Soporte y Contacto

### Para Problemas Técnicos
- **Desarrollador**: [andresbadillo.co](https://www.andresbadillo.co/)
- **Versión**: 2.3.1
- **Última actualización**: Agosto 2025

### Para Consultas Comerciales
- Contactar al analista de ventas
- Consultar con el equipo de MEM
- Revisar políticas comerciales internas

---

## 🎯 Consejos para Ejecutivos de Ventas

### Antes de Usar la Aplicación
1. **Prepare su información**: Tenga claro el mercado, nivel de tensión y competidor
2. **Defina su objetivo**: ¿Qué quiere demostrar al cliente?
3. **Planifique su presentación**: Cómo usará los datos

### Durante el Análisis
1. **Sea selectivo**: No compare con todos los competidores a la vez
2. **Mantenga el foco**: En los datos más relevantes para su cliente
3. **Tome notas**: De los hallazgos más importantes

### Después del Análisis
1. **Prepare su argumento**: Basado en los datos obtenidos
2. **Anticipe objeciones**: Prepare respuestas para posibles contraargumentos
3. **Documente**: Guarde los resultados para seguimiento futuro

---

**¡Recuerde: Los datos son una herramienta poderosa, pero la relación con el cliente y el servicio de calidad son los factores que realmente cierran las ventas!** 