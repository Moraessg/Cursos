import os
ncpf = input ('Informe o numero do CPF : ').replace (".", "") .replace("-", "")

#Validador do 1 digito verificador
nove_digitos = ncpf[:9]
print('Os nove primeiros digitos são: ', nove_digitos)

soma_nove_digitos = (4+3+9+8+6+0+3+1+8)
contagem = 10
resultado_mult_1 = 0

for numero in nove_digitos:
    resultado_mult_1 += int(numero) * contagem
    contagem -= 1
digito_verificador_1 = (resultado_mult_1 * 10 % 11)
digito_verificador_1 = digito_verificador_1 if digito_verificador_1 <= 9 else 0


#Validador do 2 digito verificador
dez_digitos = ncpf[:9] + str(digito_verificador_1)
print ('Os dez primeiros digitos são: ' , dez_digitos)

resultado_mult_2 = 0
contagem_2 = 11

for numero2 in dez_digitos:
    resultado_mult_2 += int(numero2) * contagem_2
    contagem_2 -=1
digito_verificador_2 = resultado_mult_2 * 10 % 11
digito_verificador_2 = digito_verificador_2 if digito_verificador_2 <=9 else 0
numero_cpf = nove_digitos + str(digito_verificador_1) + str(digito_verificador_2)

os.system ('cls')

print ('O primeiro digito verificador é: ' , digito_verificador_1)
print ('O segundo digito verificador é:' , digito_verificador_2)
#print ('O numero do CPF correto é: ' , numero_cpf)

if ncpf == numero_cpf:
    print ('O CPF informado', ncpf,'é valido')
else:
    print('O CPF informado', ncpf, 'é invalido e o numero correto é', numero_cpf)


