import streamlit as st
import pandas as pd
import csv
from collections import defaultdict
import plotly.graph_objects as go

def processar_csv(df):
    estatisticas = defaultdict(lambda: {
        'vencedor_geral': 0,
        'perdedor_geral': 0,
        'perdedor_mandante': 0,
        'vencedor_mandante': 0,
        'empate_mandante': 0,
        'perdedor_visitante': 0,
        'vencedor_visitante': 0,
        'empate_visitante': 0
    })

    for _, linha in df.iterrows():
        mandante = linha['mandante']
        visitante = linha['visitante']
        vencedor = linha['vencedor']

        if vencedor == '-':
            estatisticas[mandante]['empate_mandante'] += 1
            estatisticas[visitante]['empate_visitante'] += 1
        else:
            estatisticas[vencedor]['vencedor_geral'] += 1

            if vencedor == mandante:
                estatisticas[mandante]['vencedor_mandante'] += 1
                estatisticas[visitante]['perdedor_visitante'] += 1
            else:
                estatisticas[visitante]['vencedor_visitante'] += 1
                estatisticas[mandante]['perdedor_mandante'] += 1

        if vencedor != mandante and vencedor != '-':
            estatisticas[mandante]['perdedor_geral'] += 1
        if vencedor != visitante and vencedor != '-':
            estatisticas[visitante]['perdedor_geral'] += 1

    return estatisticas

def criar_grafico(dados, titulo):
    fig = go.Figure(data=[go.Bar(
        x=list(dados.keys()),
        y=list(dados.values()),
        text=list(dados.values()),
        textposition='auto',
    )])
    fig.update_layout(title=titulo, xaxis_title="Times", yaxis_title="Quantidade")
    return fig

st.set_page_config(page_title="Dashboard de Futebol", layout="wide")

st.title("Dashboard de Estatísticas de Futebol")

uploaded_file = st.file_uploader("Escolha o arquivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, delimiter='\t')
    estatisticas = processar_csv(df)

    st.subheader("Visão Geral dos Dados")
    st.write(df)

    times = list(estatisticas.keys())
    time_selecionado = st.selectbox("Selecione um time para ver estatísticas detalhadas:", times)

    if time_selecionado:
        st.subheader(f"Estatísticas para {time_selecionado}")
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Vencedor (geral)", estatisticas[time_selecionado]['vencedor_geral'])
            st.metric("Perdedor (geral)", estatisticas[time_selecionado]['perdedor_geral'])
            st.metric("Vencedor (Mandante)", estatisticas[time_selecionado]['vencedor_mandante'])
            st.metric("Perdedor (Mandante)", estatisticas[time_selecionado]['perdedor_mandante'])

        with col2:
            st.metric("Empate (Mandante)", estatisticas[time_selecionado]['empate_mandante'])
            st.metric("Vencedor (Visitante)", estatisticas[time_selecionado]['vencedor_visitante'])
            st.metric("Perdedor (Visitante)", estatisticas[time_selecionado]['perdedor_visitante'])
            st.metric("Empate (Visitante)", estatisticas[time_selecionado]['empate_visitante'])

    st.subheader("Gráficos Comparativos")
    metrica = st.selectbox("Escolha uma métrica para comparar todos os times:", 
                           ['vencedor_geral', 'perdedor_geral', 'vencedor_mandante', 'perdedor_mandante', 
                            'empate_mandante', 'vencedor_visitante', 'perdedor_visitante', 'empate_visitante'])

    dados_grafico = {time: stats[metrica] for time, stats in estatisticas.items()}
    fig = criar_grafico(dados_grafico, f"Comparação de {metrica.replace('_', ' ').title()} entre Times")
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Por favor, faça o upload de um arquivo CSV para começar.")
