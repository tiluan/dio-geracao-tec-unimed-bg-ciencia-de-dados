# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Definindo o estilo do gráfico
plt.style.use("seaborn")

# Upload do arquivo
from google.colab import files
arq = files.upload()

# Criando nosso DataFrame a partir do arquivo Excel
df = pd.read_excel("AdventureWorks.xlsx")

# Visualizando as 5 primeiras linhas do DataFrame
df.head()

# Verificando a quantidade de linhas e colunas do DataFrame
df.shape

# Verificando os tipos de dados de cada coluna
df.dtypes

# Calculando a receita total (soma dos valores de venda)
receita_total = df["Valor Venda"].sum()
print("Receita total:", receita_total)

# Calculando o custo total (multiplicação do custo unitário pela quantidade e soma)
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])
custo_total = df["custo"].sum()
print("Custo total:", round(custo_total, 2))

# Calculando o lucro total (diferença entre a receita e o custo)
df["lucro"] = df["Valor Venda"] - df["custo"]
lucro_total = df["lucro"].sum()
print("Lucro total:", round(lucro_total, 2))

# Transformando a coluna "Tempo_envio" em número de dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

# Calculando a média do tempo de envio por marca
media_tempo_envio = df.groupby("Marca")["Tempo_envio"].mean()
print("Média do tempo de envio por marca:\n", media_tempo_envio)

# Verificando se há valores faltantes no DataFrame
valores_faltantes = df.isnull().sum()
print("Valores faltantes:\n", valores_faltantes)

# Calculando o lucro por ano e por marca
lucro_por_ano_marca = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()
print("Lucro por ano e por marca:\n", lucro_por_ano_marca)

# Resetando o índice e formatando a exibição do lucro por ano e por marca
lucro_ano = lucro_por_ano_marca.reset_index()
pd.options.display.float_format = '{:20,.2f}'.format
print("Lucro por ano e por marca (formatado):\n", lucro_ano)

# Calculando o total de produtos vendidos por produto (quantidade)
total_produtos_vendidos = df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)
print("Total de produtos vendidos por produto:\n", total_produtos_vendidos)

# Gráfico de barras horizontais do total de produtos vendidos por produto
total_produtos_vendidos.plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")
plt.show()

# Gráfico de barras do lucro por ano
df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Lucro")
plt.show()

# Selecionando apenas as vendas do ano de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]
df_2009.head()

# Gráfico de Lucro por Mês no ano de 2009
df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")

# Gráfico de Lucro por Marca no ano de 2009
df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')

# Gráfico de Lucro por Classe no ano de 2009
df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')

# Resumo estatístico do tempo de envio
df["Tempo_envio"].describe()

# Gráfico de Boxplot do tempo de envio
plt.boxplot(df["Tempo_envio"])

# Histograma do tempo de envio
plt.hist(df["Tempo_envio"])

# Tempo mínimo de envio
df["Tempo_envio"].min()

# Tempo máximo de envio
df['Tempo_envio'].max()

# Identificando o Outlier com tempo de envio igual a 20
df[df["Tempo_envio"] == 20]

# Salvando o DataFrame em um arquivo CSV
df.to_csv("df_vendas_novo.csv", index=False)
