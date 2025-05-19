"""Módulo para la visualización de datos y gráficos."""

import plotly.graph_objects as go
import pandas as pd
from typing import Optional

def crear_grafico_comparacion(df_resultado: pd.DataFrame) -> Optional[go.Figure]:
    """
    Crea un gráfico interactivo comparando CU de RUITOQUE vs otro comercializador.
    
    Args:
        df_resultado: DataFrame con los resultados de la comparación.
    
    Returns:
        Figura de Plotly o None si hay error.
    """
    try:
        # Identificar el comercializador para comparar
        col_com = [col for col in df_resultado.columns if col.startswith("CU_") and col != "CU_RTQ"][0]
        comercializador = col_com.replace("CU_", "")

        # Crear figura
        fig = go.Figure()

        # Agregar línea para RUITOQUE
        fig.add_trace(go.Scatter(
            x=df_resultado['FECHA'],
            y=df_resultado['CU_RTQ'],
            name='RUITOQUE',
            line=dict(color='#64B43F', width=2),
            mode='lines+markers'
        ))

        # Agregar línea para el otro comercializador
        fig.add_trace(go.Scatter(
            x=df_resultado['FECHA'],
            y=df_resultado[col_com],
            name=comercializador,
            line=dict(color='#FF4B4B', width=2),
            mode='lines+markers'
        ))

        # Actualizar layout
        fig.update_layout(
            title=f'Comparación de CU entre RUITOQUE y {comercializador}',
            xaxis_title='Fecha',
            yaxis_title='Costo Unitario (CU)',
            hovermode='x unified',
            showlegend=True,
            template='plotly_white',
            height=500,
            legend=dict(
                yanchor="bottom",
                y=1.1,
                xanchor="center",
                x=0.5,
                orientation="h"
            )
        )

        # Agregar grid
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

        return fig
        
    except Exception as e:
        print(f"Error al crear el gráfico: {str(e)}")
        return None 