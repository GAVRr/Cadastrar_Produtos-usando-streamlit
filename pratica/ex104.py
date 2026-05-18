
def leiaint(msg):
    valor = 0
    while True:
       try:
           valor = int(input(msg))
       except(ValueError, TypeError):
           return '\n\033[1;31m[ERRO] número inválido\033[m'
       except(KeyboardInterrupt):
           return '\n\033[1;31mO usuário preferiu encerrar o programa!\033[m'
       else:
        return valor





