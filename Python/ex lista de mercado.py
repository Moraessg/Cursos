import os
lista_mercado = []

while True:
    print ('Selecione uma opção')
    opção  = input ('inserir [i] apagar [a] listar [l] : ')

    if opção == 'i':
        os.system ('cls')
        valor = input ('Valor: ')
        lista_mercado.append(valor)
    elif opção == 'a':
        os.system ('cls')
        valor_apagar = input ('Informe o indice: ')
        try:
            indice = int(valor_apagar)
            del lista_mercado [indice]
        except:
            print ('Não foi possível apagar o registro')
    
    elif opção == 'l':
        os.system ('cls')
        
        if len(lista_mercado) == 0:
            print ('Não há lista para exibir')
        for i, valor in enumerate(lista_mercado):
            print (i, valor)
    else:
        print ("Opção invalida. Selecione outra opção")