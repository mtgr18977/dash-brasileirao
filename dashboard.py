import streamlit as st
import pandas as pd

# Dados organizados em DataFrames para facilitar a manipulação
resultados_ordenados = {
    'Vencedor (Geral)': {'Melhores': [('Empate', 2221), ('Sao Paulo', 365), ('Flamengo', 354), ('Santos', 340), ('Internacional', 339)],
                         'Piores': [('Ipatinga', 9), ('CSA', 8), ('Gremio Prudente', 7), ('Joinville', 7), ('America-RN', 4)]},
    'Perdedor (Geral)': {'Melhores': [('Fluminense', 283), ('Athletico-PR', 282), ('Santos', 261), ('Botafogo-RJ', 259), ('Atletico-MG', 253)],
                         'Piores': [('Gremio Prudente', 21), ('Joinville', 21), ('Brasiliense', 20), ('Santo Andre', 19), ('Barueri', 13)]},
    'Perdedor (Mandante)': {'Melhores': [('Botafogo-RJ', 94), ('Fluminense', 93), ('Atletico-MG', 89), ('Vasco', 84), ('Coritiba', 82)],
                            'Piores': [('CSA', 8), ('Ipatinga', 7), ('Santo Andre', 6), ('Joinville', 6), ('Barueri', 2)]},
    'Vencedor (Mandante)': {'Melhores': [('Sao Paulo', 234), ('Santos', 230), ('Internacional', 229), ('Flamengo', 224), ('Athletico-PR', 221)],
                            'Piores': [('Joinville', 6), ('CSA', 6), ('Brasiliense', 6), ('Gremio Prudente', 5), ('America-RN', 2)]},
    'Empate (Mandante)': {'Melhores': [('Fluminense', 111), ('Sao Paulo', 111), ('Corinthians', 109), ('Santos', 106), ('Flamengo', 104)],
                          'Piores': [('Santo Andre', 5), ('Gremio Prudente', 5), ('CSA', 5), ('Ipatinga', 3), ('America-RN', 3)]},
    'Perdedor (Visitante)': {'Melhores': [('Athletico-PR', 215), ('Fluminense', 190), ('Santos', 188), ('Gremio', 171), ('Internacional', 171)],
                             'Piores': [('CSA', 14), ('Santo Andre', 13), ('Brasiliense', 12), ('Gremio Prudente', 12), ('Barueri', 11)]},
    'Vencedor (Visitante)': {'Melhores': [('Sao Paulo', 131), ('Flamengo', 130), ('Palmeiras', 117), ('Fluminense', 117), ('Cruzeiro', 116)],
                             'Piores': [('Gremio Prudente', 2), ('America-RN', 2), ('CSA', 2), ('Santa Cruz', 2), ('Joinville', 1)]},
    'Empate (Visitante)': {'Melhores': [('Corinthians', 120), ('Sao Paulo', 118), ('Flamengo', 117), ('Atletico-MG', 116), ('Palmeiras', 111)],
                           'Piores': [('Brasiliense', 5), ('Santo Andre', 3), ('Joinville', 3), ('CSA', 3), ('America-RN', 2)]}
}

# Função para converter os dados para um DataFrame
def convert_to_df(data, title):
    df = pd.DataFrame(data[title])
    df.columns = ['Time', 'Quantidade']
    return df

# Criação do Dashboard
st.title("Dashboard Interativo de Desempenho dos Times")

# Seleção de critério para exibição dos dados
criterio = st.selectbox("Escolha o critério:", list(resultados_ordenados.keys()))

# Exibição dos melhores e piores times para o critério selecionado
st.subheader(f"Melhores Times - {criterio}")
st.table(convert_to_df(resultados_ordenados, criterio)['Melhores'])

st.subheader(f"Piores Times - {criterio}")
st.table(convert_to_df(resultados_ordenados, criterio)['Piores'])
