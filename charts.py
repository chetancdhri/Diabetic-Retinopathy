import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st


def create_patient_demographics_chart(patients_df):
    """Create comprehensive patient demographics dashboard"""

    # Age distribution
    fig_age = px.histogram(patients_df, x='age', nbins=15,
                           title='Age Distribution of Patients',
                           color_discrete_sequence=['#667eea'])
    fig_age.update_layout(showlegend=False)

    # DR Stage distribution
    stage_counts = patients_df['dr_stage'].value_counts().sort_index()
    fig_stages = px.pie(values=stage_counts.values, names=stage_counts.index,
                        title='Distribution of DR Stages',
                        color_discrete_sequence=px.colors.sequential.RdBu)

    # HbA1c vs DR Stage
    fig_scatter = px.scatter(patients_df, x='hba1c', y='age', color='dr_stage',
                             size='diabetes_duration', hover_data=['patient_id'],
                             title='HbA1c vs Age colored by DR Stage',
                             color_continuous_scale='viridis')

    # Risk factors correlation
    corr_data = patients_df[['age', 'diabetes_duration', 'hba1c', 'bp_systolic', 'dr_stage']].corr()
    fig_corr = px.imshow(corr_data, title='Risk Factors Correlation Matrix',
                         color_continuous_scale='RdBu_r', aspect="auto")

    return fig_age, fig_stages, fig_scatter, fig_corr


def create_treatment_effectiveness_chart():
    """Create treatment effectiveness visualization"""
    treatments = ['Laser Therapy', 'Anti-VEGF', 'Vitrectomy', 'Combination']
    success_rates = [65, 78, 72, 85]
    side_effects = [15, 12, 25, 18]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        name='Success Rate (%)',
        x=treatments,
        y=success_rates,
        marker_color='#2ecc71'
    ))

    fig.add_trace(go.Bar(
        name='Side Effects (%)',
        x=treatments,
        y=side_effects,
        marker_color='#e74c3c'
    ))

    fig.update_layout(
        title='Treatment Effectiveness and Side Effects',
        barmode='group',
        xaxis_title='Treatment Type',
        yaxis_title='Percentage (%)'
    )

    return fig


def create_progression_timeline():
    """Create disease progression timeline"""
    stages = ['No DR', 'Mild NPDR', 'Moderate NPDR', 'Severe NPDR', 'PDR']
    time_months = [0, 24, 48, 72, 96]
    risk_scores = [5, 20, 45, 75, 90]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=time_months,
        y=risk_scores,
        mode='lines+markers',
        name='Progression Risk',
        line=dict(color='#e74c3c', width=4),
        marker=dict(size=8)
    ))

    fig.update_layout(
        title='Disease Progression Timeline',
        xaxis_title='Time (Months)',
        yaxis_title='Progression Risk (%)',
        showlegend=False
    )

    # Add stage annotations
    for i, stage in enumerate(stages):
        fig.add_annotation(
            x=time_months[i],
            y=risk_scores[i],
            text=stage,
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-40
        )

    return fig