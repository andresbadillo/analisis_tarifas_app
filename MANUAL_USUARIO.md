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
2. **Iniciar sesión** con sus credenciales corporativas (Microsoft - Azure AD)
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

#### 2.2 Selección de Comercializador(es)
- **Comercializador 1 (Obligatorio)**: La empresa competidora principal que desea comparar
- **Comercializador 2 (Opcional)**: Puede agregar un segundo competidor para comparación simultánea
- **Comercializador 3 (Opcional)**: Puede agregar un tercer competidor para comparación simultánea
- **Opciones disponibles**: Todos los comercializadores excepto RUITOQUE
- **Recomendación**: 
  - Para análisis simple: Use solo el Comercializador 1
  - Para comparación múltiple: Agregue 2 o 3 comercializadores para ver todos en un solo análisis
  - Los comercializadores opcionales se excluyen automáticamente de las opciones para evitar duplicados

#### 2.3 Selección de Nivel de Tensión
- **¿Qué es?** El nivel de tensión eléctrica del cliente
- **Opciones disponibles**: Depende del mercado y comercializador seleccionados
- **Recomendación**: Use el nivel de tensión específico de su cliente

### Paso 3: Selección de Periodos 📅

**Importante**: La selección de periodos se basa en el **Comercializador 1 (Obligatorio)**. Los comercializadores opcionales se validarán al ejecutar la comparación.

#### 3.1 Periodo Inicial
- **¿Qué es?** La fecha desde donde comenzar el análisis
- **Por defecto**: Los últimos 12 meses disponibles del comercializador principal
- **Recomendación**: 
  - Para análisis recientes: Últimos 6-12 meses
  - Para tendencias largas: Últimos 24 meses

#### 3.2 Periodo Final
- **¿Qué es?** La fecha hasta donde terminar el análisis
- **Por defecto**: El periodo más reciente disponible del comercializador principal
- **Recomendación**: Mantenga el periodo más reciente para análisis actuales

**Nota**: Si un comercializador opcional no tiene datos en el rango seleccionado, se mostrará una advertencia pero la comparación continuará con los comercializadores que sí tienen datos.

### Paso 4: Ejecutar Comparación ▶️

1. **Verificar** que todos los campos estén seleccionados
2. **Hacer clic** en "Ejecutar Comparación"
3. **Esperar** a que se procese el análisis (puede tomar unos segundos)

---

## 📊 Interpretación de Resultados

### Selector de Comercializador para Visualizar (NUEVO)

Si seleccionó múltiples comercializadores, verá un selector al inicio de los resultados:

- **Selector**: "Comercializador a visualizar"
- **Función**: Permite cambiar entre los comercializadores seleccionados para ver el análisis detallado de cada uno
- **Uso**: Seleccione el comercializador que desea analizar en detalle
- **Nota**: El análisis periodo a periodo y los resultados detallados cambian según el comercializador seleccionado

### Análisis Periodo a Periodo

La aplicación muestra mensajes detallados para cada periodo analizado del comercializador seleccionado:

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

La tabla muestra los resultados del comercializador actualmente seleccionado:
- **FECHA**: Periodo analizado
- **CU_RTQ**: Costo Unitario de RUITOQUE
- **CU_[COMPETIDOR]**: Costo Unitario del competidor seleccionado
- **ESTADO**: ✅ Exitoso o ❌ Atención
- **G_RTQ/G_[COMPETIDOR]**: Componente de Generación
- **C_RTQ/C_[COMPETIDOR]**: Componente de Comercialización

### Indicadores de Promedio (NUEVO - Múltiples Filas)

Después de la tabla de resultados, encontrará **una fila de indicadores por cada comercializador seleccionado** (1 a 3 filas):

Cada fila muestra:
- **Promedio RUITOQUE**: Costo Unitario promedio de RUITOQUE en el periodo seleccionado
- **Promedio [Competidor]**: Costo Unitario promedio del competidor en el periodo seleccionado
- **Diferencia Absoluta**: Diferencia en pesos y porcentaje entre los promedios
  - **Verde**: Cuando RUITOQUE es más competitivo (diferencia positiva)
  - **Rojo**: Cuando RUITOQUE es menos competitivo (diferencia negativa)
- **Periodos Analizados**: Número de periodos incluidos en el análisis actual

**Ventaja**: Puede comparar visualmente los promedios de todos los comercializadores seleccionados en un solo vistazo.

### Ajuste de Rango de Periodos

Puede ajustar el rango de periodos para el análisis usando el slider:

- **Slider de rango**: Arrastre los extremos del slider para seleccionar el periodo inicial y final
- **Visualización**: El slider muestra las fechas disponibles y el rango seleccionado
- **Información**: Se muestra automáticamente cuántos periodos están incluidos en el rango

Los indicadores y gráfico se actualizan automáticamente al mover el slider.

### Gráfico Interactivo (NUEVO - Comparación Múltiple)

El gráfico muestra **todos los comercializadores seleccionados simultáneamente**:

- **Línea verde**: Precios de RUITOQUE (siempre presente)
- **Líneas de colores**: Cada comercializador seleccionado tiene un color único
  - Comercializador 1: Rojo
  - Comercializador 2: Azul
  - Comercializador 3: Naranja
  - Y así sucesivamente con diferentes colores
- **Leyenda completa**: Identifica claramente cada línea del gráfico
- **Interactividad**: Hover para ver valores exactos de todos los comercializadores
- **Filtrado dinámico**: Se actualiza según el rango de periodos seleccionado
- **Comparación visual**: Permite comparar el comportamiento de múltiples competidores al mismo tiempo

**Ventaja**: Puede ver cómo RUITOQUE se compara con varios competidores simultáneamente en un solo gráfico.

### Botones de Acción

Después del gráfico encontrará:

#### Descargar Resultados (NUEVO - Múltiples Archivos)

Si seleccionó múltiples comercializadores, verá **un botón de descarga por cada comercializador**:

- **📥 Descargar [Comercializador 1]**: Descarga un archivo Excel con la comparación de RUITOQUE vs Comercializador 1
- **📥 Descargar [Comercializador 2]**: Descarga un archivo Excel con la comparación de RUITOQUE vs Comercializador 2
- **📥 Descargar [Comercializador 3]**: Descarga un archivo Excel con la comparación de RUITOQUE vs Comercializador 3

Cada archivo contiene:
- Los datos del periodo seleccionado en el slider
- Nombre descriptivo que incluye el comercializador correspondiente
- Formato profesional para presentaciones

**Ventaja**: Puede descargar comparaciones separadas para cada competidor y usarlas en diferentes presentaciones.

#### Nueva Comparación

- **🔄 Nueva Comparación**: Reinicia todo el proceso para analizar otro escenario

---

## 💰 Paso 5: Análisis de Ahorro Económico (NUEVO)

### ¿Qué es el Análisis de Ahorro?

Esta nueva funcionalidad calcula el **beneficio económico real** que tendría un cliente si cambia de su comercializador actual a RUITOQUE, basándose en su consumo promedio mensual y los precios del periodo seleccionado.

### Fórmula del Ahorro

```
Ahorro Total = Σ(CU_mes_n_COMERCIALIZADOR × Consumo_Promedio) - Σ(CU_mes_n_RUITOQUE × Consumo_Promedio)
```

Donde:
- **Σ** = Sumatoria de todos los periodos seleccionados en el slider
- **CU_mes_n** = Costo Unitario de cada mes específico
- **Consumo_Promedio** = Consumo promedio mensual del cliente en kWh

### Cómo Usar el Análisis de Ahorro

#### 5.1 Seleccionar Comercializador (NUEVO)
- **Selector**: "Comercializador" (primera columna)
- **Opciones**: Todos los comercializadores que fueron seleccionados en la comparación
- **Función**: El análisis se calculará específicamente para el comercializador seleccionado
- **Recomendación**: Seleccione el comercializador actual del cliente para calcular el ahorro real

#### 5.2 Ingresar Consumo del Cliente
- **Campo**: "Consumo promedio mensual del cliente (kWh)" (segunda columna)
- **Valor por defecto**: 1,000 kWh
- **Rango**: 1 kWh a 1,000,000 kWh
- **Recomendación**: Use el consumo real del cliente para cálculos precisos

#### 5.3 Calcular Ahorro
1. **Seleccione** el comercializador (si hay múltiples opciones)
2. **Ingrese** el consumo promedio mensual del cliente
3. **Haga clic** en "💰 Calcular Ahorro" (tercera columna)
4. **Espere** a que se procese el cálculo
5. **Visualice** los resultados detallados

#### 5.4 Reiniciar Análisis
- **Botón**: "🔄 Reiniciar Análisis" (cuarta columna)
- **Función**: Limpia los resultados del análisis de ahorro
- **Uso**: 
  - Cuando quiera calcular con un consumo diferente
  - Cuando quiera cambiar de comercializador y calcular un nuevo análisis
  - Puede cambiar el comercializador sin reiniciar, pero los resultados previos se limpiarán automáticamente

**Nota**: Todos los elementos (selector, input, botones) están en la misma fila con el mismo ancho para una mejor experiencia visual.

### Interpretación de Resultados del Ahorro

#### Métricas Principales
- **Ahorro Total**: Beneficio económico en todo el periodo analizado
- **Ahorro Mensual Promedio**: Beneficio promedio mensual
- **Ahorro por kWh**: Diferencia en el costo unitario por kWh
- **Periodos Analizados**: Número de meses incluidos en el análisis

#### Tabla de Detalle por Periodo
- **FECHA**: Mes del análisis
- **CU RUITOQUE**: Costo unitario de RUITOQUE en ese mes
- **CU [Competidor]**: Costo unitario del competidor en ese mes
- **Costo Mensual RUITOQUE**: CU × Consumo Promedio
- **Costo Mensual Competidor**: CU × Consumo Promedio
- **Diferencia Mensual**: Ahorro/costo adicional en ese mes específico

#### Resumen de la Sumatoria
- **Sumatoria del Competidor**: Total de todos los costos mensuales
- **Sumatoria de RUITOQUE**: Total de todos los costos mensuales
- **Resultado Final**: Diferencia entre ambas sumatorias
- **Promedio por Mes**: Resultado total dividido por el número de periodos

### Casos de Uso del Análisis de Ahorro

#### 1. Propuesta de Cambio de Proveedor
**Escenario**: Cliente actual considerando cambiar a RUITOQUE

**Proceso**:
1. Ejecute la comparación con el proveedor actual del cliente
2. Use el slider para seleccionar los últimos 12 meses
3. Ingrese el consumo promedio mensual del cliente
4. Calcule el ahorro total
5. Presente: *"Al cambiar a RUITOQUE, usted ahorraría $X en los próximos 12 meses"*

#### 2. Análisis de Beneficio por Consumo y Comercializador
**Escenario**: Diferentes clientes con diferentes consumos y diferentes proveedores actuales

**Proceso**:
1. Ejecute la comparación con múltiples comercializadores (si es necesario)
2. Seleccione el comercializador del Cliente A
3. Calcule el ahorro con el consumo del Cliente A
4. Reinicie el análisis
5. Seleccione el comercializador del Cliente B (si es diferente)
6. Calcule el ahorro con el consumo del Cliente B
7. Compare los beneficios para cada cliente

#### 3. Justificación de Precios
**Escenario**: Cliente cuestiona por qué RUITOQUE es más caro en algunos periodos

**Proceso**:
1. Analice un periodo más amplio (24+ meses)
2. Calcule el ahorro total en el periodo completo
3. Muestre que aunque en algunos meses RUITOQUE puede ser más caro, el beneficio total es positivo
4. Enfoque en el valor a largo plazo, no en periodos específicos

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

### 2. Análisis de Competencia Múltiple (NUEVO)

**Escenario**: Cliente menciona que otros proveedores le ofrecen mejores precios

**Proceso**:
1. Seleccione el competidor principal mencionado como Comercializador 1
2. Agregue otros competidores mencionados como Comercializador 2 y 3 (opcionales)
3. Analice un periodo más amplio (24 meses)
4. Use el gráfico múltiple para comparar visualmente todos los competidores
5. Revise los promedios de cada comercializador en las filas de indicadores
6. Identifique tendencias y patrones
7. Prepare contraargumentos basados en datos comparando con múltiples competidores

**Ventaja**: Puede demostrar que RUITOQUE es competitivo frente a varios competidores simultáneamente.

### 3. Seguimiento de Tendencias de Mercado (MEJORADO)

**Escenario**: Necesita entender cómo evolucionan los precios

**Proceso**:
1. Compare con varios competidores principales usando los selectores opcionales
2. Analice periodos largos (24+ meses)
3. Use el gráfico múltiple para ver las tendencias de todos los competidores simultáneamente
4. Use el slider para ajustar el rango y ver diferentes periodos
5. Observe cómo cambian los promedios de cada comercializador al mover el rango
6. Compare las múltiples filas de promedios para identificar qué competidor es más competitivo en cada periodo
7. Identifique tendencias de mercado
8. Use esta información para estrategias de precios

**Ventaja**: Puede analizar múltiples competidores en un solo análisis, ahorrando tiempo y proporcionando una visión más completa del mercado.

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

### Descargar Resultados (MEJORADO)

Si seleccionó un solo comercializador:
1. **Hacer clic** en "📥 Descargar Resultados"
2. **Se descarga** un archivo Excel con todos los datos de la comparación

Si seleccionó múltiples comercializadores:
1. **Verá múltiples botones**: Uno por cada comercializador seleccionado
2. **Hacer clic** en el botón del comercializador que desea descargar
3. **Se descarga** un archivo Excel específico para ese comercializador

### Uso del Archivo Excel

Cada archivo descargado contiene:
- **Hoja "Comparacion"**: Datos del análisis para el rango de periodos seleccionado
- **Columnas organizadas**: Fácil de leer y presentar
- **Datos filtrados**: Solo incluye los periodos del rango ajustado con el slider
- **Nombre descriptivo**: Incluye información del mercado, comercializador específico y rango de fechas

**Ventaja**: Puede descargar comparaciones separadas para cada competidor y usarlas en diferentes presentaciones o para diferentes clientes.

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
- **Versión**: 3.1.0
- **Última actualización**: Enero 2026

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
1. **Sea selectivo pero completo**: Compare con los competidores más relevantes (hasta 3) usando los selectores opcionales
2. **Use el gráfico múltiple**: Aproveche la visualización simultánea para comparar varios competidores
3. **Revise los promedios**: Compare las múltiples filas de promedios para identificar el mejor escenario
4. **Mantenga el foco**: En los datos más relevantes para su cliente
5. **Tome notas**: De los hallazgos más importantes
6. **Cambie de comercializador**: Use el selector para ver el análisis detallado de cada competidor

### Después del Análisis
1. **Prepare su argumento**: Basado en los datos obtenidos
2. **Anticipe objeciones**: Prepare respuestas para posibles contraargumentos
3. **Documente**: Guarde los resultados para seguimiento futuro

---

**¡Recuerde: Los datos son una herramienta poderosa, pero la relación con el cliente y el servicio de calidad son los factores que realmente cierran las ventas!** 