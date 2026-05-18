def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except(ValueError, TypeError):
            print( '\n\033[1;31m[ERRO] número inválido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[1;31mO usuário preferiu encerrar o programa!\033[m')
            return 0
        else:
            return valor



def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except(ValueError, TypeError):
            print('\n\033[1;31m[ERRO] número inválido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[1;31mO usuário preferiu encerrar o programa!\033[m')
            return 0
        else:
            return valor


n1 = leiafloat('Digite um numero real: ')
n2= leiaint('Digite um numero inteiro: ')
print(f'Você digitou o número inteiro: {n2}')
print(f'E o número real: {n1}')