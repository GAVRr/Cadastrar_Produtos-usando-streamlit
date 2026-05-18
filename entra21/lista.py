lista = []
while True:
    lista.append(str(input('Nome:')))
    lista.append(input('Idade:'))
    continuar = str(input('Quer continuar?')).upper()
    if continuar == 'N':
        break

for i, n in enumerate(lista):
    print(f'{i} | {lista[0]} - {lista[1]}')
