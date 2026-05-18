from random import randint
#gerador de "cnpj"
cnpj = ''
for i in range(14):
    cnpj = cnpj + str(randint(0,9))

print(f'Validando o CNPJ: {cnpj}')

# Crie um algoritmo que permite verificar se CNPJ
# é válido ou não.
if len(cnpj)!= 14:
   print('1')
   print('CNPJ INVÁLIDO')
elif cnpj == cnpj[0]* 14:
   print('2')
   print('CNPJ INVÁLIDO')
else:
    peso = 5
    soma = 0
    ultimo_digito, penultimo_digito = 0,0
#Validar o penultimo dígito
    for i in range(12):
        soma += int(cnpj[i])*peso
        peso-=1
        if peso < 2:
            peso = 9
    resto = soma % 11

    if resto < 2:
       penultimo_digito = 0
    else:
       penultimo_digito = 11 - resto

    # Validar o ultimo dígito
    peso = 6
    soma = 0

    for i in range(13):
        soma += int(cnpj[i]) * peso
        peso -= 1
        if peso < 2:
            peso = 9
    resto = soma % 11

    if resto < 2:
        ultimo_digito = 0
    else:
        ultimo_digito = 11 - resto

    if int(cnpj[12]) == penultimo_digito and int(cnpj[13]) == ultimo_digito:
        print('CNPJ Válido!')
    else:
        print('CNPJ Inválido!')
