numero = (int(input('Digite um numero: ')),
           int(input('Digite um numero: ')),
          int(input('Digite um numero: ')),
          int(input('Digite um numero: ')),)
print(f'Você digitou os números {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O número 3 apareceu na {numero.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado!')
print('Os valores pares dgitados foram: ', end='')
for c in numero:
    if c % 2 == 0:
        print(f'{c}  ', end='')