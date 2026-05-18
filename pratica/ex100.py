from random import randint
lista = list()
def sorteia(lista):
    print('Números sorteados:')
    for n in range(0,5):
        n = randint(0,10)
        lista.append(n)
        print(f' {n}', end=' ')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nNúmeros pares somados: {soma}')




sorteia(lista)
somaPar(lista)
