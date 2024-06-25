nome = 'Gabriel Moraes'
tamanho_nome = len(nome)
print (tamanho_nome)

indice = 0
novo_nome = '' 
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'{letra}*'
    indice +=1
print (novo_nome)
tamano_novo = len(novo_nome)
print (tamano_novo)
