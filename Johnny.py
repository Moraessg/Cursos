import os
import pandas as pd

# Carregando os dados do arquivo CSV (substitua 'seu_arquivo.csv' pelo nome real do seu arquivo)
dados = pd.read_csv(r'C:\Users\gabri\Downloads\Johnny\torradas.csv', encoding='ANSI')

# Diretório onde estão as imagens (substitua 'caminho/para/imagens' pelo caminho real)
diretorio_imagens = r'C:\Users\gabri\Downloads\Johnny\BAUDUCCO\PADARIA\Torrada Fermentacao Natural'

# Iterando sobre as linhas do DataFrame
for indice, linha in dados.iterrows():
    nome_antigo = linha['DESCRITIVO_IMAGEM']  # Coluna A
    extensao = os.path.splitext(linha['EAN-13'])[1]  # Extensão do arquivo da coluna F
    novo_nome = nome_antigo + extensao

    caminho_antigo = os.path.join(diretorio_imagens, nome_antigo)
    caminho_novo = os.path.join(diretorio_imagens, novo_nome)

    # Renomeando o arquivo
    os.rename(caminho_antigo, caminho_novo)

print('Renomeação concluída.')