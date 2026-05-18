lista = []
while True:
    numero = int(input('Digite um valor:'))
    lista.append(numero)

    continuar = ''

    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar?[S/N]').upper().strip()
        if continuar not in ['S', 'N']:
            print('\033[91mDados invalidos, tente novamente.\033[0m')
    if continuar == 'N':
        break
print()
if 5 in lista:
    print('O número 5 foi encontrado na lista.')
else:
     print('O número 5 não foi encontrado na lista.')
print()
print(f'Foram digitados {len(lista)} números')
print()
print(sorted(lista,reverse=True))



