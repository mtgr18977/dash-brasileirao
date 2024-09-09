import streamlit as st
import pandas as pd
from collections import defaultdict

def verificar_colunas(df):
    colunas_esperadas = ['rodada', 'mandante', 'visitante', 'formacao_mandante', 'formacao_visitante', 'tecnico_mandante', 'tecnico_visitante', 'vencedor']
    colunas_faltantes = [col for col in colunas_esperadas if col not in df.columns]
    return colunas_faltantes

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
        try:
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
        except KeyError as e:
            st.error(f"Erro ao processar uma linha: coluna {str(e)} não encontrada.")
            return None

    return estatisticas

st.set_page_config(page_title="Dashboard de Futebol", layout="wide")

st.title("Dashboard de Estatísticas de Futebol")

uploaded_file = st.file_uploader("Escolha o arquivo CSV", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, delimiter='\t')
        
        colunas_faltantes = verificar_colunas(df)
        if colunas_faltantes:
            st.error(f"As seguintes colunas estão faltando no arquivo CSV: {', '.join(colunas_faltantes)}")
        else:
            st.subheader("Visão Geral dos Dados")
            st.write(df)

            estatisticas = processar_csv(df)
            
            if estatisticas:
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

                st.subheader("Comparação de Métricas entre Times")
                metrica = st.selectbox("Escolha uma métrica para comparar todos os times:", 
                                       ['vencedor_geral', 'perdedor_geral', 'vencedor_mandante', 'perdedor_mandante', 
                                        'empate_mandante', 'vencedor_visitante', 'perdedor_visitante', 'empate_visitante'])

                dados_grafico = {time: stats[metrica] for time, stats in estatisticas.items()}
                st.bar_chart(dados_grafico)

    except pd.errors.EmptyDataError:
        st.error("O arquivo CSV está vazio.")
    except pd.errors.ParserError:
        st.error("Erro ao analisar o arquivo CSV. Verifique se o formato está correto.")
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado: {str(e)}")

else:
    st.info("Por favor, faça o upload de um arquivo CSV para começar.")
