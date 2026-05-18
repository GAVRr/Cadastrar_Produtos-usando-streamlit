def fatorial(n , show = False):
    '''
    -> Calcular o fatorial de um valor
    :param n: O número a ser calculado
    :param show: (opcional) mostra o calculo do valor escolhido
    :return: retorna o resultado do calculo
    '''
    f = 1
    for c in range(n , 0 , -1):
        f*=c
        if show:
            print(c, end ='')
            if c > 1:
                print(' x ' , end = '')
            else:
                print(' = ', end='')
    return f





#Programa principal
print(fatorial(5, show =True))
help(fatorial)