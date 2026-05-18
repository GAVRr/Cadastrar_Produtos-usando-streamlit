lista = []
while True:
    numero = int(input('Digite um numero: '))
    if numero not in lista:
     lista.append(numero)
     print('Número adicionado a lista!')
    else:
        print('Esse número ja foi adicionado na lista!')

    continuar = ''

    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar?[S/N]').upper().strip()
        if continuar not in ['S', 'N']:
            print('\033[91mDados invalidos, tente novamente.\033[0m')
    if continuar == 'N':
        break

print(f'Os número digitados foram: {sorted(lista)}')

