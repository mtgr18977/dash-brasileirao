import streamlit as st
import pandas as pd

# Dados organizados em DataFrames para facilitar a manipulação
resultados_ordenados = {
    'Vencedor (Geral)': {'Melhores': [('Empate', 2221), ('Sao Paulo', 365), ('Flamengo', 354), ('Santos', 340), ('Internacional', 339)],
                         'Piores': [('Ipatinga', 9), ('CSA', 8), ('Gremio Prudente', 7), ('Joinville', 7), ('America-RN', 4)]},
    'Perdedor (Geral)': {'Melhores': [('Fluminense', 283), ('Athletico-PR', 282), ('Santos', 261), ('Botafogo-RJ', 259), ('Atletico-MG', 253)],
                         'Piores': [('Gremio Prudente', 21), ('Joinville', 21), ('Brasiliense', 20), ('Santo Andre', 19), ('Barueri', 13)]},
    # Outras categorias continuam aqui...
}

# Função corrigida para converter os dados para um DataFrame
def convert_to_df(data, title, tipo):
    df = pd.DataFrame(data[title][tipo], columns=['Time', 'Quantidade'])
    return df

# Criação do Dashboard
st.title("Dashboard Interativo de Desempenho dos Times")

# Seleção de critério para exibição dos dados
criterio = st.selectbox("Escolha o critério:", list(resultados_ordenados.keys()))

# Exibição dos melhores e piores times para o critério selecionado
st.subheader(f"Melhores Times - {criterio}")
st.table(convert_to_df(resultados_ordenados, criterio, 'Melhores'))

st.subheader(f"Piores Times - {criterio}")
st.table(convert_to_df(resultados_ordenados, criterio, 'Piores'))
