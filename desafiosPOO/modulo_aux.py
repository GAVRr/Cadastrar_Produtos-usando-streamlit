# não esta sendo usado

def linha(msg):
    tamanho = len(msg) + 30
    print('-'*tamanho)
    print(f'               {msg}')
    print('-'*tamanho)


def menu():
        opcoes = list()
        opcoes.append('Ver conta cadastrada')
        opcoes.append('Abrir nova conta')
        opcoes.append('Depositar')
        opcoes.append('Sacar')
        opcoes.append('Ver saldo')
        opcoes.append('Sair do sistema')
        for i, op in enumerate(opcoes):
            print(f'[yellow]{i + 1}[/] - [blue]{op}[/]')
        print('-' * 30)