import pandas as pd

df = pd.read_csv('/data/ecommerce_preparados.csv')
df = df.dropna()

# Escreva seu código abaixo

# Cálculo das estatísticas
media = df['Desconto'].mean()  # Média dos descontos
mediana = df['Desconto'].median()  # Mediana dos descontos
variancia = df['Desconto'].var()  # Variância dos descontos
desvio_padrao = df['Desconto'].std()  # Desvio padrão dos descontos

# Como a função mode() retorna uma Série contendo todas as modas, [0] é usado para selecionar a primeira moda caso haja múltiplas.
moda = df['Desconto'].mode()[0]  # Moda dos descontos

minimo = df['Desconto'].min()  # Valor mínimo do desconto
quartis = df['Desconto'].quantile([0.25, 0.5, 0.75])  # Quartis dos descontos
maximo = df['Desconto'].max()  # Valor máximo do desconto

print(f'Média: {media:.2f}')
print(f'Mediana: {mediana:.2f}')
print(f'Variância: {variancia:.2f}')
print(f'Desvio padrão: {desvio_padrao:.2f}')
print(f'Moda: {moda:.2f}')
print(f'Mínimo: {minimo:.2f}')
print(f'Quartis:\n{quartis}')
print(f'Máximo: {maximo:.2f}')

# Exibe as primeiras linhas do DataFrame
df.head()

import pandas as pd

df = pd.read_csv('/data/ecommerce_preparados.csv')
df = df.dropna()

# Escreva seu código abaixo

# Calcula a correlação entre a quantidade vendida e o número de avaliações
corr_n_avaliacoes = df[['Qtd_Vendidos_Cod', 'N_Avaliacoes_MinMax']].corr()

# Calcula a correlação entre a quantidade vendida e a nota média
corr_nota = df[['Qtd_Vendidos_Cod', 'Nota_MinMax']].corr()

# Calcula a correlação entre a quantidade vendida e o preço
corr_preco = df[['Qtd_Vendidos_Cod', 'Preco_MinMax']].corr()

# Exibe os resultados
print("Correlação com o número de avaliações:", corr_n_avaliacoes)
print("Correlação com a nota média:", corr_nota)
print("Correlação com o preço:", corr_preco)


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

# Carrega os dados
df = pd.read_csv('/data/ecommerce_preparados.csv')
df = df.dropna()

# Define as variáveis preditoras e a variável alvo
X = df[['N_Avaliacoes_MinMax', 'Nota_MinMax', 'Preco_MinMax', 'Desconto_MinMax', 'Temporada_Cod', 'Marca_Freq', 'Material_Freq']]  # Preditor
Y = df['Qtd_Vendidos_Cod']

# Divide os dados em conjuntos de treino e teste
# Atenção, utilize os parâmetros com esses valores: `test_size=0.2` e `random_state = 42`.
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Cria e treina o modelo de Regressão Linear
modelo_lr = LinearRegression()
modelo_lr.fit(x_train, y_train)

# Faz previsões com o conjunto de teste
y_prev = modelo_lr.predict(x_test)

# Avalia o modelo
r2 = r2_score(y_test, y_prev)
print(f'Coeficiente de Determinação - R²: {r2:.2f}')

rmse = sqrt(mean_squared_error(y_test, y_prev))
print(f"Raiz do Erro Quadrático Médio - RMSE: {rmse:.2f}")

desvio_padrao = Y.std()
print(f"Desvio Padrão do campo Qtd_Vendidos_Cod: {desvio_padrao}")