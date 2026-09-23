# Análise de Dados com Python — E-commerce

Repositório dedicado a estudos e projetos práticos de análise e preparação de dados utilizando Python, com foco em um dataset de e-commerce. Os scripts aqui documentados fazem parte de um pipeline progressivo: exploração inicial → limpeza → engenharia de atributos (feature engineering) → análise estatística, correlação e modelagem preditiva.

## 🎯 Objetivo do repositório
Reunir projetos práticos de análise de dados em Python, documentando cada etapa do raciocínio por trás do código — não apenas o "o quê", mas o "porquê" de cada transformação. A ideia é que cada novo projeto adicionado aqui siga a mesma lógica: dataset bruto → tratamento → dados prontos para análise ou modelagem.

## 🛠️ Tecnologias utilizadas
- Python 3
- pandas — manipulação, limpeza e análise estatística de dados tabulares
- scikit-learn (`MinMaxScaler`, `LabelEncoder`, `train_test_split`, `LinearRegression`, `r2_score`, `mean_squared_error`) — normalização, codificação e construção de modelos de machine learning

## 📁 Estrutura dos projetos

### Projeto_Analise_Dados_1.py
Primeira etapa do pipeline: exploração e limpeza inicial do dataset bruto (`ecommerce.csv`).
- Verificação da estrutura dos dados (dimensões, tipos, valores nulos)
- Tratamento de valores nulos nas colunas `Temporada` e `Marca`
- Identificação de outliers na coluna `N_Avaliacoes` pelo método do IQR
- Extração de duas informações misturadas na coluna `Condicao` (condição do produto + quantidade vendida)
- Limpeza da coluna `Desconto`, removendo o símbolo `%`

### Projeto_Analise_Dados_2.py
Continuação do pipeline, dividida em 3 blocos sequenciais que partem do dataset já tratado na etapa anterior:
- **Bloco 1:** exploração de dados únicos e estatísticas descritivas; criação do campo `Preco` (unindo Reais e Centavos); remoção de colunas não mais necessárias.
- **Bloco 2:** normalização de variáveis numéricas com `MinMaxScaler` (`Nota`, `N_Avaliacoes`, `Desconto`, `Preco`) e codificação de variáveis categóricas com `LabelEncoder` (`Marca`, `Material`, `Temporada`).
- **Bloco 3:** conversão manual da coluna `Qtd_Vendidos` (texto "amigável" como "+10mil") em valores numéricos, além de codificação por frequência (`value_counts` + `map`) para `Marca` e `Material`.

### Projeto_Analise_Dados_3.py
Terceira etapa do pipeline, focada em estatística descritiva, análise de correlação e regressão linear sobre o dataset preparado (`ecommerce_preparados.csv`):
- **Estatísticas Descritivas:** cálculo de média, mediana, variância, desvio padrão, moda, mínimo, quartis (25%, 50%, 75%) e máximo para a variável `Desconto`.
- **Análise de Correlação:** avaliação da correlação entre a variável alvo (`Qtd_Vendidos_Cod`) e as variáveis preditoras (`N_Avaliacoes_MinMax`, `Nota_MinMax` e `Preco_MinMax`).
- **Modelagem Preditiva:** divisão dos dados em conjuntos de treino e teste (`test_size=0.2`, `random_state=42`), treinamento de um modelo de **Regressão Linear** com `scikit-learn` e avaliação do desempenho com **R²** (Coeficiente de Determinação) e **RMSE** (Raiz do Erro Quadrático Médio).

---

## 📌 Padrão para projetos futuros
Novos projetos de análise de dados adicionados a este repositório devem seguir o mesmo padrão:
1. Um script `.py` numerado sequencialmente (`Projeto_Analise_Dados_N.py`)
2. Um arquivo de estudo em markdown correspondente (`Estudo_Projeto_N.md`), no formato bloco de código + explicação **Para que serve:**
3. Comentários explicativos no próprio código, priorizando entendimento sobre concisão
4. Um resumo geral ao final do estudo, listando as etapas do pipeline daquele projeto

---

## 🚀 Como executar

```bash
pip install pandas scikit-learn
python Projeto_Analise_Dados_1.py
python Projeto_Analise_Dados_2.py
python Projeto_Analise_Dados_3.py

