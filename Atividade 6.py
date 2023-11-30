import pandas as pd

#Substitua 'exemplo_arquivo.csv' pelo nome do seu arquivo.
caminho_arquivo = 'exemplo_arquivo.csv'

#Realiza a leitura do arquivo CSV e cria um DataFrame
dataframe = pd.read_csv(caminho_arquivo)

#Exibe as primeiras linhas do DataFrame
print(dataframe.head())
