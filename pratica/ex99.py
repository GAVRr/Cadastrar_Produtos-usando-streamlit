from opc import *
def maior(*num):
    cont = maior = 0
    pular_linha()
    print('\nAnalisando os valores...')
    pular_linha()
    for valor in num:
        print(f'{valor}' , end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'\nForam informados {cont} valores!')
    print(f'O maior valor informado foi {maior}')

pular_linha()
maior(3,5,8,1,10,8)
maior(6,8,3,4)
maior(4,8)
maior()
pular_linha()