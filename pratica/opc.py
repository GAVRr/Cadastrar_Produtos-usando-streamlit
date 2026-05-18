from rich import print
def opc():
    continuar = ""

    while continuar not in ['S', 'N']:
        continuar = input('Deseja prosseguir?[S/N]').capitalize().strip()
        if continuar not in ['S', 'N']:
            print('[red]Dados invalidos, tente novamente.[/]')
    return continuar

def pular_linha():
    print('-' * 30)


def aumento_salario(salario_funcionario):
    porcentagem = int(input('Qual a porcentagem de aumento?: '))
    porcentagem_aumento = salario_funcionario * (porcentagem / 100)
    salario_final = salario_funcionario + porcentagem_aumento
    pular_linha()
    print(f'Novo salário calculado: R${salario_final:.2f}')
    return salario_final
