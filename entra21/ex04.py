

lista = list()
for c in range(3):
    altura = float(input('Altura:'))
    print()
    idade = int(input('Idade:'))
    print()
    nome = str(input('Nome:'))
    print('-'*20)

    lista.append([altura , idade  , nome])

maior_a , menor_a  = 0 , 0
nome_menor = ''
nome_maior = ''
idade_maior,idade_menor= 0,0

for pessoa in lista:
    if pessoa[0] > maior_a:
        maior_a = pessoa[0]
        nome_maior  = pessoa[2]
        idade_maior = pessoa[1]

    if pessoa[0] < maior_a:
        menor_a = pessoa[0]
        nome_menor = pessoa [2]
        idade_menor = pessoa[1]

print(f'A pessoa com maior altura é {nome_maior} tem {idade_maior} anos, com  {maior_a:.2f}')
print()
print(f'A pessoa com menor altura é {nome_menor} tem {idade_menor} anos, com  {menor_a:.2f}')
