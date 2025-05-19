"""Módulo para la comparación de tarifas entre comercializadores."""

import pandas as pd
from typing import Optional, Dict, Any, List
import streamlit as st

def comparar_cu(
    df_tarifas: pd.DataFrame,
    mercado_seleccionado: str,
    comercializador_seleccionado: str,
    nt_seleccionado: str,
    max_periodos: int = 12
) -> Optional[pd.DataFrame]:
    """
    Compara el CU de RUITOQUE frente a otro comercializador.
    
    Args:
        df_tarifas: DataFrame con los datos de tarifas.
        mercado_seleccionado: Mercado a analizar.
        comercializador_seleccionado: Comercializador para comparar.
        nt_seleccionado: Nivel de tensión.
        max_periodos: Máximo número de periodos a analizar.
    
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

        acumulados = []
        mensajes_analisis.append(
            f"📅 Iniciando recorrido desde {df_cmp['FECHA'].iloc[0]} hacia atrás (hasta {max_periodos} periodos)"
        )

        for idx, row in df_cmp.iterrows():
            if idx >= max_periodos:
                break
                
            temp = pd.DataFrame(acumulados + [row])
            prom_rtq = temp['CU_RTQ'].mean()
            prom_sel = temp[f'CU_{suf}'].mean()

            if prom_rtq < prom_sel:
                acumulados.append(row)
                mensajes_analisis.append(
                    f"✅ {row['FECHA']} -> incluido (per. #{len(acumulados)}: PROM_RTQ={prom_rtq:.2f} < PROM_{suf}={prom_sel:.2f})"
                )
            else:
                if not acumulados:
                    mensajes_analisis.append(
                        f"⏳ {row['FECHA']} -> RTQ no es más barato, intentando periodos anteriores..."
                    )
                    continue
                mensajes_analisis.append(
                    f"🛑 {row['FECHA']} -> detenido (PROM_RTQ={prom_rtq:.2f} >= PROM_{suf}={prom_sel:.2f})"
                )
                break

        if not acumulados:
            mensajes_analisis.append("⚠️ Ningún periodo válido donde RTQ tenga CU promedio más bajo")
            return None

        df_resultado = pd.DataFrame(acumulados).copy()
        df_resultado['NT'] = nt_seleccionado

        prom_rtq_final = df_resultado['CU_RTQ'].mean()
        prom_sel_final = df_resultado[f'CU_{suf}'].mean()

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