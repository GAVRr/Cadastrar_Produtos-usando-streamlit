from opc import *
time = list()
jogador = dict()
lista = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome:')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
    lista.clear()

    for p in range(0, partidas):
        lista.append(int(input(f'   Quantos gols na partida {p+1}?')))
    jogador['Gols'] = lista[:]
    jogador['Total'] = sum(lista)
    time.append(jogador.copy())
    print('-=-'*20)
    print(jogador)
    print('-=-'*20)

    continuar = opc()
    if continuar == 'N':
        print('Encerrando...')
        break

print('cod ', end='')
for i in jogador:
    print(f'{i:<15} ', end='')
print()
print('-'*50)


for k, v in enumerate(time):
    print(f' {k:>3}' ,end ='' )
    for d in v.values():
        print(f' {str(d):<15}' , end = '')
    print()
print('-'*50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! o jogador com codigo {busca} não existe!')
    else:
        print(f' -- LEVANTAMENDO DO JOGADOR {time[busca] ['Nome']}:')
        for i , g in enumerate(time[busca]['Gols']):
            print(f'   no jogo {i+1} fez {g} gols.')
print('-'*50)
print('<< VOLTE SEMPRE >>')




