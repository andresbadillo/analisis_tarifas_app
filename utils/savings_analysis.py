"""Módulo para el análisis de ahorro en tarifas de energía."""

import pandas as pd
import streamlit as st
from typing import Dict, Tuple, Optional

def calcular_ahorro_energia(
    df_resultado: pd.DataFrame,
    periodo_inicio: str,
    periodo_fin: str,
    consumo_promedio_kwh: float
) -> Optional[Dict]:
    """
    Calcula el ahorro total en energía comparando RUITOQUE vs otro comercializador.
    
    Args:
        df_resultado: DataFrame con los resultados de la comparación
        periodo_inicio: Periodo inicial del análisis (formato: YYYY-MM)
        periodo_fin: Periodo final del análisis (formato: YYYY-MM)
        consumo_promedio_kwh: Consumo promedio mensual del cliente en kWh
    
    Returns:
        Diccionario con los resultados del análisis de ahorro o None si hay error
    """
    try:
        # Filtrar datos por el rango de periodos seleccionado
        df_filtrado = df_resultado[
            (df_resultado['FECHA'] >= periodo_inicio) & 
            (df_resultado['FECHA'] <= periodo_fin)
        ].copy()
        
        if df_filtrado.empty:
            st.error("❌ No hay datos disponibles para el rango de periodos seleccionado")
            return None
        
        # Verificar que el DataFrame tiene la estructura esperada (columnas con sufijos)
        if 'CU_RTQ' not in df_filtrado.columns:
            st.error("❌ El DataFrame no tiene la estructura esperada. Falta la columna 'CU_RTQ'")
            return None
        
        # Identificar la columna del competidor
        columnas_cu = [col for col in df_filtrado.columns if col.startswith('CU_') and col != 'CU_RTQ']
        if not columnas_cu:
            st.error("❌ No se encontró la columna del competidor en los datos")
            return None
        
        col_competidor = columnas_cu[0]
        competidor = col_competidor.replace('CU_', '')
        
        # Calcular costos totales por comercializador (sumatoria de todos los periodos)
        # Fórmula: Σ(CU_mes_n × Consumo_Promedio) para cada comercializador
        costo_total_ruitoque = (df_filtrado['CU_RTQ'] * consumo_promedio_kwh).sum()
        costo_total_competidor = (df_filtrado[col_competidor] * consumo_promedio_kwh).sum()
        
        # Calcular ahorro total
        # Ahorro = Σ(CU_mes_n × Consumo_Promedio)_Competidor - Σ(CU_mes_n × Consumo_Promedio)_RUITOQUE
        ahorro_absoluto = costo_total_competidor - costo_total_ruitoque
        ahorro_porcentual = (ahorro_absoluto / costo_total_competidor) * 100 if costo_total_competidor > 0 else 0
        
        # Calcular costos promedio por kWh (para referencia)
        cu_promedio_ruitoque = df_filtrado['CU_RTQ'].mean()
        cu_promedio_competidor = df_filtrado[col_competidor].mean()
        
        # Calcular ahorro por kWh (diferencia promedio)
        ahorro_por_kwh = cu_promedio_competidor - cu_promedio_ruitoque
        
        # Calcular ahorro mensual promedio basado en la diferencia promedio
        ahorro_mensual_promedio = ahorro_por_kwh * consumo_promedio_kwh
        
        # Calcular número total de periodos analizados
        total_periodos = len(df_filtrado)
        
        # Preparar resultados
        resultados = {
            'periodo_inicio': periodo_inicio,
            'periodo_fin': periodo_fin,
            'periodos_analizados': len(df_filtrado['FECHA'].unique()),
            'total_periodos': total_periodos,
            'consumo_promedio_kwh': consumo_promedio_kwh,
            'competidor': competidor,
            'costo_total_ruitoque': costo_total_ruitoque,
            'costo_total_competidor': costo_total_competidor,
            'ahorro_absoluto': ahorro_absoluto,
            'ahorro_porcentual': ahorro_porcentual,
            'cu_promedio_ruitoque': cu_promedio_ruitoque,
            'cu_promedio_competidor': cu_promedio_competidor,
            'ahorro_por_kwh': ahorro_por_kwh,
            'ahorro_mensual_promedio': ahorro_mensual_promedio,
            'hay_ahorro': ahorro_absoluto > 0,
            'df_detalle': df_filtrado,
            'col_competidor': col_competidor
        }
        
        return resultados
        
    except Exception as e:
        st.error(f"❌ Error al calcular el ahorro: {str(e)}")
        return None

def mostrar_analisis_ahorro(resultados: Dict) -> None:
    """
    Muestra el análisis de ahorro en la interfaz de Streamlit.
    
    Args:
        resultados: Diccionario con los resultados del análisis de ahorro
    """
    if not resultados:
        return
    
    st.subheader("💰 Resumen del Ahorro")
    
    # Métricas principales en columnas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if resultados['hay_ahorro']:
            st.metric(
                "Ahorro Total", 
                f"${resultados['ahorro_absoluto']:,.2f}",
                delta=f"{resultados['ahorro_porcentual']:+.2f}%",
                delta_color="normal",
                help="Ahorro total en el periodo seleccionado (RUITOQUE más económico)"
            )
        else:
            st.metric(
                "Costo Adicional", 
                f"${abs(resultados['ahorro_absoluto']):,.2f}",
                delta=f"{resultados['ahorro_porcentual']:.2f}%",
                delta_color="inverse",
                help="Costo adicional en el periodo seleccionado (RUITOQUE menos económico)"
            )
    
    with col2:
        if resultados['hay_ahorro']:
            st.metric(
                "Ahorro Mensual Promedio", 
                f"${resultados['ahorro_mensual_promedio']:,.2f}",
                help="Ahorro promedio mensual basado en el consumo ingresado"
            )
        else:
            st.metric(
                "Costo Mensual Adicional", 
                f"${abs(resultados['ahorro_mensual_promedio']):,.2f}",
                help="Costo adicional promedio mensual basado en el consumo ingresado"
            )
    
    with col3:
        if resultados['hay_ahorro']:
            st.metric(
                "Ahorro por kWh", 
                f"${resultados['ahorro_por_kwh']:,.4f}",
                help="Diferencia en el costo unitario por kWh (RUITOQUE más económico)"
            )
        else:
            st.metric(
                "Costo Adicional por kWh", 
                f"${abs(resultados['ahorro_por_kwh']):,.4f}",
                help="Diferencia en el costo unitario por kWh (RUITOQUE menos económico)"
            )
    
    with col4:
        st.metric(
            "Periodos Analizados", 
            f"{resultados['periodos_analizados']}",
            help="Número de periodos incluidos en el análisis"
        )
    
    # Detalles del análisis
    st.subheader("📊 Detalles del Análisis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"**Consumo Promedio:** {resultados['consumo_promedio_kwh']:,.0f} kWh/mes")
        st.info(f"**Periodo Analizado:** {resultados['periodo_inicio']} a {resultados['periodo_fin']}")
        st.info(f"**Competidor:** {resultados['competidor']}")
    
    with col2:
        st.info(f"**Costo Total RUITOQUE:** ${resultados['costo_total_ruitoque']:,.2f}")
        st.info(f"**Costo Total {resultados['competidor']}:** ${resultados['costo_total_competidor']:,.2f}")
        st.info(f"**CU Promedio RUITOQUE:** ${resultados['cu_promedio_ruitoque']:,.4f}")
        st.info(f"**CU Promedio {resultados['competidor']}:** ${resultados['cu_promedio_competidor']:,.4f}")
    
    # Tabla de detalle por periodo
    st.subheader("📋 Detalle por Periodo")
    
    df_detalle = resultados['df_detalle'].copy()
    
    # Crear columnas para mostrar los costos mensuales
    df_detalle['Costo Mensual RUITOQUE'] = df_detalle['CU_RTQ'] * resultados['consumo_promedio_kwh']
    df_detalle['Costo Mensual Competidor'] = df_detalle[resultados['col_competidor']] * resultados['consumo_promedio_kwh']
    
    # Agregar columna de diferencia mensual
    df_detalle['Diferencia Mensual'] = df_detalle['Costo Mensual Competidor'] - df_detalle['Costo Mensual RUITOQUE']
    
    # Mostrar tabla con formato
    columnas_mostrar = ['FECHA', 'CU_RTQ', resultados['col_competidor'], 'Costo Mensual RUITOQUE', 'Costo Mensual Competidor', 'Diferencia Mensual']
    df_mostrar = df_detalle[columnas_mostrar].copy()
    
    # Renombrar columnas para mejor visualización
    df_mostrar.columns = ['FECHA', f'CU RUITOQUE', f'CU {resultados["competidor"]}', 'Costo Mensual RUITOQUE', 'Costo Mensual Competidor', 'Diferencia Mensual']
    
    # Formatear la columna de diferencia con colores
    st.dataframe(
        df_mostrar,
        use_container_width=True,
        hide_index=True
    )
    
    # Resumen de la sumatoria
    st.subheader("🧮 Resumen de la Sumatoria")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"""
        **📊 Sumatoria {resultados['competidor']}:**
        
        ```
        Σ(CU_mes_n × {resultados['consumo_promedio_kwh']:,.0f} kWh) = ${resultados['costo_total_competidor']:,.2f}
        ```
        
        **📊 Sumatoria RUITOQUE:**
        
        ```
        Σ(CU_mes_n × {resultados['consumo_promedio_kwh']:,.0f} kWh) = ${resultados['costo_total_ruitoque']:,.2f}
        ```
        """)
    
    with col2:
        if resultados['hay_ahorro']:
            st.success(f"""
            **✅ Ahorro Total:**
            
            ```
            ${resultados['costo_total_competidor']:,.2f} - ${resultados['costo_total_ruitoque']:,.2f} = ${resultados['ahorro_absoluto']:,.2f}
            ```
            
            **📈 Ahorro Promedio por Mes:**
            ```
            ${resultados['ahorro_absoluto']:,.2f} ÷ {resultados['total_periodos']} meses = ${resultados['ahorro_absoluto'] / resultados['total_periodos']:,.2f}
            ```
            """)
        else:
            st.warning(f"""
            **⚠️ Costo Adicional Total:**
            
            ```
            ${resultados['costo_total_ruitoque']:,.2f} - ${resultados['costo_total_competidor']:,.2f} = ${abs(resultados['ahorro_absoluto']):,.2f}
            ```
            
            **📈 Costo Promedio por Mes:**
            ```
            ${abs(resultados['ahorro_absoluto']):,.2f} ÷ {resultados['total_periodos']} meses = ${abs(resultados['ahorro_absoluto']) / resultados['total_periodos']:,.2f}
            ```
            """)
    
    # Explicación del cálculo
    st.subheader("🧮 Explicación del Cálculo")
    
    if resultados['hay_ahorro']:
        st.markdown(f"""
        **📊 Fórmula del Ahorro Total (Periodo Completo):**
        
        ```
        Ahorro Total = Σ(CU_mes_n × Consumo_Promedio)_{resultados['competidor']} - Σ(CU_mes_n × Consumo_Promedio)_RUITOQUE
        
        Donde Σ representa la sumatoria de todos los {resultados['total_periodos']} periodos seleccionados
        ```
        
        **🧮 Cálculo Detallado:**
        
        ```
        Costo Total {resultados['competidor']} = ${resultados['costo_total_competidor']:,.2f}
        Costo Total RUITOQUE = ${resultados['costo_total_ruitoque']:,.2f}
        
        Ahorro = ${resultados['costo_total_competidor']:,.2f} - ${resultados['costo_total_ruitoque']:,.2f} = ${resultados['ahorro_absoluto']:,.2f}
        ```
        
        **📈 Métricas Adicionales:**
        
        ```
        Ahorro por kWh (promedio) = CU Promedio {resultados['competidor']} - CU Promedio RUITOQUE
        Ahorro por kWh = ${resultados['cu_promedio_competidor']:,.4f} - ${resultados['cu_promedio_ruitoque']:,.4f} = ${resultados['ahorro_por_kwh']:,.4f}
        
        Ahorro Mensual Promedio = Ahorro por kWh × Consumo Promedio
        Ahorro Mensual = ${resultados['ahorro_por_kwh']:,.4f} × {resultados['consumo_promedio_kwh']:,.0f} kWh = ${resultados['ahorro_mensual_promedio']:,.2f}
        ```
        
        **✅ Resultado Final:** El cliente ahorraría **${resultados['ahorro_absoluto']:,.2f}** en el periodo completo analizado si cambia a RUITOQUE.
        """)
    else:
        st.markdown(f"""
        **📊 Fórmula del Costo Adicional (Periodo Completo):**
        
        ```
        Costo Adicional = Σ(CU_mes_n × Consumo_Promedio)_RUITOQUE - Σ(CU_mes_n × Consumo_Promedio)_{resultados['competidor']}
        
        Donde Σ representa la sumatoria de todos los {resultados['total_periodos']} periodos seleccionados
        ```
        
        **🧮 Cálculo Detallado:**
        
        ```
        Costo Total RUITOQUE = ${resultados['costo_total_ruitoque']:,.2f}
        Costo Total {resultados['competidor']} = ${resultados['costo_total_competidor']:,.2f}
        
        Costo Adicional = ${resultados['costo_total_ruitoque']:,.2f} - ${resultados['costo_total_competidor']:,.2f} = ${abs(resultados['ahorro_absoluto']):,.2f}
        ```
        
        **📈 Métricas Adicionales:**
        
        ```
        Costo por kWh (promedio) = CU Promedio RUITOQUE - CU Promedio {resultados['competidor']}
        Costo por kWh = ${resultados['cu_promedio_ruitoque']:,.4f} - ${resultados['cu_promedio_competidor']:,.4f} = ${abs(resultados['ahorro_por_kwh']):,.4f}
        
        Costo Mensual Promedio = Costo por kWh × Consumo Promedio
        Costo Mensual = ${abs(resultados['ahorro_por_kwh']):,.4f} × {resultados['consumo_promedio_kwh']:,.0f} kWh = ${abs(resultados['ahorro_mensual_promedio']):,.2f}
        ```
        
        **⚠️ Resultado Final:** El cliente tendría un costo adicional de **${abs(resultados['ahorro_absoluto']):,.2f}** en el periodo completo analizado si cambia a RUITOQUE.
        """)
