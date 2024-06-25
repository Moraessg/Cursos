#Questão 1
nome = input("Qual o seu nome?")
sobrenome = input("Qual o seu sobrenome?")
print("Olá, " + nome + " " + sobrenome)

#Questão 2
soma = (13 + 15 + 16 + 6)
print ("A soma é:",soma)

#desafio Mario
tamanho = int(input("Qual o tamanho que quer a pirame?"))
for i in range (1, tamanho + 1):
    tamanho -= 1
    print (" " * tamanho, end="")
    print ("#" * i)

#desafio Mario2
tamanho = int(input("Qual o tamanho que quer a pirame?"))
for i in range (1, tamanho + 1):
    tamanho -= 1
    print (" " * tamanho, end="")
    print ("#" * i + " " + "#" * i)