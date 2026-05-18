lista = []
maior = 0
menor = 0
for c in range (0,5):
    lista.append(int(input(f'Digite o {c} número:')))
    if c == 0 :
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]



print(f'Você digitou os valores {lista}')
print(f'O maior numero digitado foi o {maior} nas posições ' , end ='')
for i, v in enumerate(lista):
    if v == maior:
         print(f'{i:.>10}',end='')
print()
print(f'O menor numero digitado foi o {menor} nas posições ', end = '')
for number , values in enumerate(lista):
    if values == menor:
        print(f'{number:.>10}',end='')
