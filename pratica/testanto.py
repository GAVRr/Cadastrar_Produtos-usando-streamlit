count = 0
soma = 0
mediaidade = 0
maioridadevelho = 0
nomevelho = ''
for c in range(1,5):
    nome = str(input('Nome:'))
    idade = (int(input('Idade:')))
    sexo = str(input('Sexo: [M/F]')).upper()
    soma+= idade
    if sexo == 'F' and idade < 20:
        count +=1
    if c == 1 and sexo == 'M':
        maioridadevelho = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadevelho:
        maioridadevelho = idade
        nomevelho = nome

mediaidade = soma / 4
print(f'A média de idade do grupo é de {mediaidade}')
print(f'{count} mulheres com menos de 20 anos de idade!')
print(f'o nome do homem mais velho é {nomevelho} e a idade dele é {maioridadevelho}')