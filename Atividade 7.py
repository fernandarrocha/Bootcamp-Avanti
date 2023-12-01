#Baixar o pandas
import pandas as pd

#Criar um DataFrame
dados = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Idade': [25, 30, 22, 35, 28],
    'Cidade': ['NY', 'LA', 'SF', 'LA', 'NY']
}

df = pd.DataFrame(dados)

#Selecionar uma coluna específica
coluna_idade = df['Idade']
print("Coluna de Idade:")
print(coluna_idade)

#Filtrar linhas com base em uma condição 
condicao = df['Idade'] > 25
linhas_filtradas = df.loc[condicao]
print("\nLinhas com Idade maior que 25:")
print(linhas_filtradas)
