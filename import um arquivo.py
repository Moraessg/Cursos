#Um arquivo
import pandas as pd

larguras = [7, 6, 5]

caminho_arquivo = 'C:\\Users\\gabri\\OneDrive\\Documents\\Curso Udemy\\GabrielMoraesSilva.txt'

dados = pd.read_fwf(caminho_arquivo, colspecs='infer', widths=larguras, header=None)

print(dados)

# Especifique o caminho para o arquivo Excel de saída
caminho_excel = 'C:\\Users\\gabri\\OneDrive\\Documents\\Curso Udemy\\teste.xlsx'

# Exporte os dados para o Excel
dados.to_excel(caminho_excel, index=False)
