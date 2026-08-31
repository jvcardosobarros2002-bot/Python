import pandas as pd  # Importa a biblioteca pandas, usada para manipular dados em formato de tabela (DataFrame)

# Lê o arquivo CSV e carrega os dados em um DataFrame chamado 'df'
df = pd.read_csv('/data/ecommerce.csv')

# ============================================================
# ETAPA 1: Verificação inicial da estrutura dos dados
# ============================================================

# df.shape retorna uma tupla (quantidade_de_linhas, quantidade_de_colunas)
# Isso nos dá uma ideia do tamanho total da base de dados
linhas_colunas = df.shape
print('Verificar a qtd de Linhas e colunas: ', linhas_colunas)

# df.dtypes retorna o tipo de dado de cada coluna (ex: int64, float64, object/texto)
# Isso é importante para saber se os dados estão no formato esperado
# (ex: uma coluna de preço não deveria ser do tipo texto)
tipos = df.dtypes
print('Verificar Tipagem:\n', tipos)

# df.isnull() marca cada célula como True (nula) ou False (preenchida)
# .sum() soma os True de cada coluna, contando quantos valores nulos existem em cada uma
nulos = df.isnull().sum()
print('Verificar valores nulos:\n', nulos)

# ============================================================
# ETAPA 2: Tratamento de valores nulos
# ============================================================

# .fillna('Não Definido') substitui todo valor nulo (NaN) da coluna
# pelo texto 'Não Definido', evitando que fiquem lacunas nos dados
df['Temporada'] = df['Temporada'].fillna('Não Definido')
df['Marca'] = df['Marca'].fillna('Não Definido')

# Repetimos as verificações acima para confirmar que os nulos foram tratados
# (o resultado de 'nulos' agora deve mostrar 0 para 'Temporada' e 'Marca')
linhas_colunas = df.shape
print('Verificar a qtd de Linhas e colunas: ', linhas_colunas)

tipos = df.dtypes
print('Verificar Tipagem:\n', tipos)

nulos = df.isnull().sum()
print('Verificar valores nulos:\n', nulos)

# Aplicamos o mesmo tratamento de nulos novamente (redundante, mas não causa erro,
# já que não há mais nulos para substituir nessas colunas)
df['Temporada'] = df['Temporada'].fillna('Não Definido')
df['Marca'] = df['Marca'].fillna('Não Definido')

# ============================================================
# ETAPA 3: Identificação de outliers usando o método do IQR
# ============================================================

# O IQR (Intervalo Interquartil) é uma técnica estatística para detectar valores
# "fora da curva" (outliers) em uma coluna numérica.

# Q1 (1º quartil): valor abaixo do qual estão 25% dos dados
q1 = df['N_Avaliacoes'].quantile(0.25)

# Q3 (3º quartil): valor abaixo do qual estão 75% dos dados
q3 = df['N_Avaliacoes'].quantile(0.75)

# IQR = diferença entre Q3 e Q1, representa a "faixa central" dos dados
iqr = q3 - q1

# limite_alto define o ponto acima do qual um valor é considerado outlier
# A constante 1.5 é o multiplicador padrão usado nesse método estatístico
limite_alto = q3 + 1.5 * iqr

# Filtra o DataFrame, mantendo apenas as linhas cujo número de avaliações
# ultrapassa o limite superior (ou seja, os produtos com avaliações "fora do comum")
df_avaliados = df[df['N_Avaliacoes'] > limite_alto]

# ============================================================
# ETAPA 4: Extração de informações da coluna 'Condicao'
# ============================================================
# Exemplo de valor original nessa coluna: "Novo | +10mil vendidos"

# .apply(lambda x: ...) executa uma função personalizada em cada valor da coluna
# x.split('|') separa a string em duas partes usando o caractere '|' como divisor
#   Ex: "Novo | +10mil vendidos" -> ['Novo ', ' +10mil vendidos']
# [0] pega a primeira parte ("Novo ")
# .strip() remove espaços em branco no início/fim ("Novo ")
# pd.notna(x) verifica se o valor não é nulo antes de tentar processar,
# evitando erro caso a célula esteja vazia; se for nula, retorna 'Nenhum'
df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split('|')[0].strip() if pd.notna(x) else 'Nenhum')

# Aqui pegamos a segunda parte da string (depois do '|'), ex: " +10mil vendidos"
# [1] pega essa segunda parte
# .strip() remove espaços extras -> "+10mil vendidos"
# .split(' ')[0] separa por espaço e pega a primeira palavra -> "+10mil"
# A condição verifica se o valor não é nulo E se contém o caractere '|'
# (ou seja, se realmente existe uma quantidade informada); caso contrário, retorna 'Nenhum'
df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split('|')[1].strip().split(' ')[0] if pd.notna(x) and '|' in x else 'Nenhum')

# ============================================================
# ETAPA 5: Limpeza da coluna 'Desconto'
# ============================================================

# .astype(str) converte todos os valores da coluna para o tipo texto (string)
# Isso é necessário para poder usar métodos de string como .split() em seguida
df['Desconto'] = df['Desconto'].astype(str)

# x.split('%')[0] separa a string no caractere '%' e pega apenas a parte ANTES dele
#   Ex: "18% OFF" -> ['18', ' OFF'] -> pega '18'
# .strip() remove espaços em branco que possam sobrar
# Resultado: a coluna passa a conter apenas o número do desconto, como texto "18"
df['Desconto'] = df['Desconto'].apply(lambda x: x.split('%')[0].strip())