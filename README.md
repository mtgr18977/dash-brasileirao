# Dashboards do Campeonato Brasileiro

Este repositório contém dois dashboards interativos criados com Streamlit para análise de dados do Campeonato Brasileiro de Futebol. Os dashboards oferecem insights sobre o desempenho dos times, estatísticas de jogos, análise de treinadores e formações táticas utilizadas.

## Conteúdo

1. [Requisitos](#requisitos)
2. [Instalação](#instalação)
3. [Uso](#uso)
4. [Dashboards](#dashboards)
   - [Dashboard de Estatísticas de Times](#dashboard-de-estatísticas-de-times)
   - [Dashboard de Treinadores e Formações](#dashboard-de-treinadores-e-formações)
5. [Estrutura de Arquivos](#estrutura-de-arquivos)
6. [Contribuição](#contribuição)
7. [Licença](#licença)

## Requisitos

- Python 3.7+
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/dashboards-brasileirao.git
   cd dashboards-brasileirao
   ```

2. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Certifique-se de que o arquivo `campeonato-brasileiro-full.csv` está na raiz do diretório do projeto.

2. Para executar o Dashboard de Estatísticas de Times:
   ```
   streamlit run dashboard_estatisticas_times.py
   ```

3. Para executar o Dashboard de Treinadores e Formações:
   ```
   streamlit run dashboard_treinadores_formacoes.py
   ```

4. Abra seu navegador e acesse `http://localhost:8501` para visualizar o dashboard.

## Dashboards

### Dashboard de Estatísticas de Times

Este dashboard fornece uma análise detalhada do desempenho dos times no Campeonato Brasileiro. Ele inclui:

- Visão geral dos dados do campeonato
- Estatísticas detalhadas para cada time (vitórias, derrotas, empates)
- Comparação de métricas entre times
- Gráficos interativos para visualização de dados

### Dashboard de Treinadores e Formações

Este dashboard se concentra na análise dos treinadores e das formações táticas utilizadas. Ele oferece:

- Análise de desempenho dos treinadores (jogos, vitórias, empates, derrotas, aproveitamento)
- Visualização das formações mais utilizadas por times mandantes e visitantes
- Comparação de formações entre times mandantes e visitantes
- Gráficos de pizza e barras para representação visual dos dados

## Estrutura de Arquivos

```
dashboards-brasileirao/
│
├── dashboard_estatisticas_times.py
├── dashboard_treinadores_formacoes.py
├── campeonato-brasileiro-full.csv
├── requirements.txt
└── README.md
```

## Contribuição

Contribuições são bem-vindas! Se você tem sugestões para melhorar os dashboards ou adicionar novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Dataset

Disponível no respositório: [https://github.com/adaoduque/Brasileirao_Dataset](https://github.com/adaoduque/Brasileirao_Dataset).

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
