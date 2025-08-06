"""Módulo para la visualización de datos y gráficos."""

import plotly.graph_objects as go
import pandas as pd
from typing import Optional

def crear_grafico_comparacion(df_resultado: pd.DataFrame, periodo_inicio: str = None, periodo_fin: str = None) -> Optional[go.Figure]:
    """
    Crea un gráfico interactivo comparando CU de RUITOQUE vs otro comercializador.
    
    Args:
        df_resultado: DataFrame con los resultados de la comparación.
        periodo_inicio: Periodo de inicio para filtrar (opcional)
        periodo_fin: Periodo final para filtrar (opcional)
    
    Returns:
        Figura de Plotly o None si hay error.
    """
    try:
        # Filtrar datos si se especifican periodos
        df_plot = df_resultado.copy()
        if periodo_inicio and periodo_fin:
            df_plot = df_plot[
                (df_plot['FECHA'] >= periodo_inicio) & 
                (df_plot['FECHA'] <= periodo_fin)
            ]
        
        if df_plot.empty:
            return None
            
        # Identificar el comercializador para comparar
        col_com = [col for col in df_plot.columns if col.startswith("CU_") and col != "CU_RTQ"][0]
        comercializador = col_com.replace("CU_", "")

        # Crear figura
        fig = go.Figure()

        # Separar periodos exitosos y de atención
        periodos_exitosos = df_plot[df_plot['ESTADO'] == '✅ Exitoso']
        periodos_atencion = df_plot[df_plot['ESTADO'] == '❌ Atención']

        # Agregar línea para RUITOQUE (todos los periodos)
        fig.add_trace(go.Scatter(
            x=df_plot['FECHA'],
            y=df_plot['CU_RTQ'],
            name='RUITOQUE',
            line=dict(color='#64B43F', width=2),
            mode='lines+markers'
        ))

        # Agregar línea para el otro comercializador (todos los periodos)
        fig.add_trace(go.Scatter(
            x=df_plot['FECHA'],
            y=df_plot[col_com],
            name=comercializador,
            line=dict(color='#FF4B4B', width=2),
            mode='lines+markers'
        ))

        # Agregar marcadores especiales para periodos de atención
        if not periodos_atencion.empty:
            fig.add_trace(go.Scatter(
                x=periodos_atencion['FECHA'],
                y=periodos_atencion['CU_RTQ'],
                name='Periodos de Atención',
                mode='markers',
                marker=dict(
                    symbol='x',
                    size=12,
                    color='#FF6B35',
                    line=dict(width=2, color='#FF6B35')
                ),
                showlegend=True
            ))

        # Actualizar layout
        fig.update_layout(
            title=f'Comparación de CU entre RUITOQUE y {comercializador}',
            xaxis_title='Periodos',
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