#Varios arquivos
import pandas as pd
import os

# Especifica o diretório contendo os arquivos de texto
diretorio = 'C:\\Users\\gabri\\OneDrive\\Documents\\Curso Udemy'

# Lista todos os arquivos no diretório
arquivos = [f for f in os.listdir(diretorio) if f.endswith('.txt')]

# Lista para armazenar os DataFrames de cada arquivo
dataframes = []

# Defina as larguras das colunas (posição inicial e final)
larguras = [7, 6, 5]

# Loop sobre cada arquivo
for arquivo in arquivos:
    caminho_arquivo = os.path.join(diretorio, arquivo)

    # Leia o arquivo usando read_fwf
    dados = pd.read_fwf(caminho_arquivo, colspecs='infer', widths=larguras, header=None)

    # Adicione o DataFrame à lista
    dataframes.append(dados)

# Combine todos os DataFrames em um único DataFrame
dados_combinados = pd.concat(dataframes, ignore_index=True)

# Exiba os dados combinados
print(dados_combinados)

# Especifique o caminho para o arquivo Excel de saída
caminho_excel = 'C:\\Users\\gabri\\OneDrive\\Documents\\Curso Udemy\\teste.xlsx'

# Exporte os dados combinados para o Excel
dados_combinados.to_excel(caminho_excel, index=False)
