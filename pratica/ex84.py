pessoas = []
dados = []
maiorpeso= 0
menorpeso= 0

while True:
    dados.append(str(input('Nome: ')).strip().upper())
    dados.append(float(input('Peso (em KG): ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar =''
    while continuar not in ['S','N']:
        continuar = str(input('Quer continuar? [S/N] ')).strip().capitalize()
    if continuar == 'N':
        break

print('-='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas')

print(f'O maior peso foi {maiorpeso} Kg de  ', end = '')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ', end = '')
print()
print(f'O menor peso foi {menorpeso} Kg de  ', end = '')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}] ', end = '')