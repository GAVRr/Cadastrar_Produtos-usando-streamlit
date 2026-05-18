from random import randint
from operator import itemgetter
jogos = {'Jogador1': randint(1, 6),
         'Jogador2': randint(1, 6),
         'Jogador3': randint(1, 6),
         'Jogador4': randint(1, 6),}
print('Valores sorteados:')
for k,v in jogos.items():
    print(f'{k} tirou {v} no dado.')
print('=--='*20)
ranking = sorted(jogos.items(), key = itemgetter(1), reverse = True)
for i , v in enumerate(ranking):
    print(f'{i+1} lugar:  {v[0]} com {v[1]} no dado.')