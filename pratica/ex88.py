from random import randint
from time import sleep
jogos = int(input('Quantos jogos deseja jogar? '))
for c in range(jogos):
    lista = list()
    cont = 0

    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
            if cont >= 6:
                break
    sleep(0.5)
    print(f'Jogo {c+1}: {sorted(lista)}')