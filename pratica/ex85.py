from opc import opc
lista = [[],[]]
valor = 0

for c in range(0,7):
    while True:
        try:
            valor = int(input('Digite um número:'))
            if valor % 2 == 0:
                lista[0].append(valor)
            if valor % 2 == 1:
                lista[1].append(valor)
            break
        except:
            print('ERRO! apenas números inteiros!')
            continue


print(f'Os números pares digitados foram {sorted(lista[0])}')
print(f'Os números impares digitados foram {sorted(lista[1])}')