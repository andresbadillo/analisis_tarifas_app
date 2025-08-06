"""Módulo para la comparación de tarifas entre comercializadores."""

import pandas as pd
from typing import Optional, Dict, Any, List
import streamlit as st

def comparar_cu(
    df_tarifas: pd.DataFrame,
    mercado_seleccionado: str,
    comercializador_seleccionado: str,
    nt_seleccionado: str,
    periodo_inicio: str = None,
    periodo_fin: str = None
) -> Optional[pd.DataFrame]:
    """
    Compara el CU de RUITOQUE frente a otro comercializador en un rango de periodos específico.
    
    Args:
        df_tarifas: DataFrame con los datos de tarifas.
        mercado_seleccionado: Mercado a analizar.
        comercializador_seleccionado: Comercializador para comparar.
        nt_seleccionado: Nivel de tensión.
        periodo_inicio: Periodo de inicio para la comparación (formato: YYYY-MM).
        periodo_fin: Periodo final para la comparación (formato: YYYY-MM).
    
    Returns:
        DataFrame con la comparación o None si hay error.
    """
    try:
        mensajes_analisis = []
        
        df = (
            df_tarifas
            .drop_duplicates(subset=["FECHA","COMERCIALIZADOR","MERCADO","NT","CU","G","C"])
            .dropna(subset=["FECHA","CU","G","C"])
        )
        
        df = df[(df["MERCADO"] == mercado_seleccionado) & (df["NT"] == nt_seleccionado)]
        df_rtq_full = df[df["COMERCIALIZADOR"] == "RUITOQUE"].copy()
        df_sel_full = df[df["COMERCIALIZADOR"] == comercializador_seleccionado].copy()

        if df_rtq_full.empty or df_sel_full.empty:
            mensajes_analisis.append("⚠️ No hay datos suficientes para comparar")
            return None

        suf = comercializador_seleccionado.replace(' ', '_')
        df_cmp = pd.merge(
            df_rtq_full,
            df_sel_full,
            on='FECHA',
            suffixes=('_RTQ', f'_{suf}')
        ).sort_values('FECHA', ascending=False).reset_index(drop=True)

        # Filtrar por rango de periodos si se especifica
        if periodo_inicio and periodo_fin:
            df_cmp = df_cmp[
                (df_cmp['FECHA'] >= periodo_inicio) & 
                (df_cmp['FECHA'] <= periodo_fin)
            ].sort_values('FECHA', ascending=False).reset_index(drop=True)
            
            if df_cmp.empty:
                mensajes_analisis.append(f"⚠️ No hay datos en el rango especificado ({periodo_inicio} a {periodo_fin})")
                return None
            
            mensajes_analisis.append(
                f"📅 Analizando periodos desde {periodo_inicio} hasta {periodo_fin} ({len(df_cmp)} periodos selecionados)"
            )
        else:
            mensajes_analisis.append(
                f"📅 Analizando todos los periodos disponibles ({len(df_cmp)} periodos)"
            )

        todos_periodos = []
        mensajes_analisis.append(
            f"🔄 Iniciando análisis desde {df_cmp['FECHA'].iloc[0]} hacia atrás"
        )

        for idx, row in df_cmp.iterrows():
            temp = pd.DataFrame(todos_periodos + [row])
            prom_rtq = temp['CU_RTQ'].mean()
            prom_sel = temp[f'CU_{suf}'].mean()

            if prom_rtq < prom_sel:
                todos_periodos.append(row)
                mensajes_analisis.append(
                    f"✅ {row['FECHA']} -> Exitoso (per. #{len(todos_periodos)}: PROM_RTQ={prom_rtq:.2f} < PROM_{suf}={prom_sel:.2f})"
                )
            else:
                todos_periodos.append(row)
                mensajes_analisis.append(
                    f"❌ {row['FECHA']} -> Atención! (per. #{len(todos_periodos)}: PROM_RTQ={prom_rtq:.2f} > PROM_{suf}={prom_sel:.2f})"
                )

        if not todos_periodos:
            mensajes_analisis.append("⚠️ No hay periodos disponibles para analizar")
            return None

        df_resultado = pd.DataFrame(todos_periodos).copy()
        df_resultado['NT'] = nt_seleccionado

        prom_rtq_final = df_resultado['CU_RTQ'].mean()
        prom_sel_final = df_resultado[f'CU_{suf}'].mean()

        # Agregar columna de estado (exitoso o no)
        df_resultado['ESTADO'] = df_resultado.apply(
            lambda row: '✅ Exitoso' if row['CU_RTQ'] < row[f'CU_{suf}'] else '❌ Atención', 
            axis=1
        )
        
        metrics = {
            'DIF_CU_$': df_resultado[f'CU_{suf}'] - df_resultado['CU_RTQ'],
            'DIF_CU_%': (df_resultado[f'CU_{suf}'] - df_resultado['CU_RTQ']) / df_resultado['CU_RTQ'] * 100,
            'DIF_G_$': df_resultado[f'G_{suf}'] - df_resultado['G_RTQ'],
            'DIF_G_%': (df_resultado[f'G_{suf}'] - df_resultado['G_RTQ']) / df_resultado['G_RTQ'] * 100,
            'DIF_C_$': df_resultado[f'C_{suf}'] - df_resultado['C_RTQ'],
            'DIF_C_%': (df_resultado[f'C_{suf}'] - df_resultado['C_RTQ']) / df_resultado['C_RTQ'] * 100,
            'PROM_CU_RTQ': prom_rtq_final,
            f'PROM_CU_{suf}': prom_sel_final,
            'DIF_PROM_CU_$': prom_sel_final - prom_rtq_final,
            'DIF_PROM_CU_%': (prom_sel_final - prom_rtq_final) / prom_rtq_final * 100
        }
        df_resultado = df_resultado.assign(**metrics)

        cols = [
            'FECHA',
            'NT',
            'ESTADO',
            'CU_RTQ',
            f'CU_{suf}',
            'DIF_CU_$',
            'DIF_CU_%',
            'G_RTQ',
            f'G_{suf}',
            'DIF_G_$',
            'DIF_G_%',
            'C_RTQ',
            f'C_{suf}',
            'DIF_C_$',
            'DIF_C_%',
            'PROM_CU_RTQ',
            f'PROM_CU_{suf}',
            'DIF_PROM_CU_$',
            'DIF_PROM_CU_%'
        ]
        df_resultado = df_resultado[cols]
        df_resultado = df_resultado.round(2)

        # Actualizar mensajes en el estado de la sesión
        st.session_state['mensajes_analisis'] = mensajes_analisis

        return df_resultado

    except Exception as e:
        st.error(f"❌ Error en la comparación: {str(e)}")
        return None


def calcular_promedios_periodo(df_resultado: pd.DataFrame, periodo_inicio: str = None, periodo_fin: str = None) -> dict:
    """
    Calcula los promedios de CU para RUITOQUE y el competidor en un rango de periodos específico.
    
    Args:
        df_resultado: DataFrame con los resultados de la comparación
        periodo_inicio: Periodo de inicio para filtrar (formato: YYYY-MM)
        periodo_fin: Periodo final para filtrar (formato: YYYY-MM)
    
    Returns:
        Diccionario con los promedios calculados
    """
    try:
        # Filtrar por rango de periodos si se especifica
        df_filtrado = df_resultado.copy()
        if periodo_inicio and periodo_fin:
            df_filtrado = df_filtrado[
                (df_filtrado['FECHA'] >= periodo_inicio) & 
                (df_filtrado['FECHA'] <= periodo_fin)
            ]
        
        if df_filtrado.empty:
            return {
                'promedio_rtq': 0,
                'promedio_competidor': 0,
                'diferencia_absoluta': 0,
                'diferencia_porcentual': 0,
                'periodos_analizados': 0
            }
        
        # Identificar la columna del competidor
        col_competidor = [col for col in df_filtrado.columns if col.startswith('CU_') and col != 'CU_RTQ'][0]
        comercializador = col_competidor.replace('CU_', '')
        
        # Calcular promedios
        promedio_rtq = df_filtrado['CU_RTQ'].mean()
        promedio_competidor = df_filtrado[col_competidor].mean()
        diferencia_absoluta = promedio_competidor - promedio_rtq
        diferencia_porcentual = (diferencia_absoluta / promedio_rtq * 100) if promedio_rtq > 0 else 0
        
        return {
            'promedio_rtq': round(promedio_rtq, 2),
            'promedio_competidor': round(promedio_competidor, 2),
            'diferencia_absoluta': round(diferencia_absoluta, 2),
            'diferencia_porcentual': round(diferencia_porcentual, 2),
            'periodos_analizados': len(df_filtrado),
            'comercializador': comercializador
        }
        
    except Exception as e:
        print(f"Error al calcular promedios: {str(e)}")
        return {
            'promedio_rtq': 0,
            'promedio_competidor': 0,
            'diferencia_absoluta': 0,
            'diferencia_porcentual': 0,
            'periodos_analizados': 0
        }


def filtrar_resultados_por_periodo(df_resultado: pd.DataFrame, periodo_inicio: str = None, periodo_fin: str = None) -> pd.DataFrame:
    """
    Filtra los resultados de comparación por un rango de periodos específico.
    
    Args:
        df_resultado: DataFrame con los resultados de la comparación
        periodo_inicio: Periodo de inicio para filtrar (formato: YYYY-MM)
        periodo_fin: Periodo final para filtrar (formato: YYYY-MM)
    
    Returns:
        DataFrame filtrado por el rango de periodos
    """
    try:
        df_filtrado = df_resultado.copy()
        
        if periodo_inicio and periodo_fin:
            df_filtrado = df_filtrado[
                (df_filtrado['FECHA'] >= periodo_inicio) & 
                (df_filtrado['FECHA'] <= periodo_fin)
            ]
        
        return df_filtrado
        
    except Exception as e:
        print(f"Error al filtrar resultados: {str(e)}")
        return df_resultado 