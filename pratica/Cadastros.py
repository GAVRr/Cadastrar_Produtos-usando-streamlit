from opc import *
from opc import pular_linha
from rich import print


funcionario_lista = list()

while True:
    cadastro = dict()
    cadastro['nome'] = str(input('Nome do funcionário: ')).capitalize().strip()
    cadastro['funcao'] = str(input('Função do funcionário: ')).capitalize().strip()
    cadastro['salario_base'] = float(input('Salário do funcionário R$'))

    pular_linha()

    cadastro['salario_final'] = cadastro['salario_base']

    aumento = ''
    while aumento not in ['S', 'N']:
        aumento = input('Aplicar aumento?: [S/N] ').upper().strip()
        if aumento not in ['S', 'N']:
            print('[red]Dados inválidos, tente novamente.[/]')

    if aumento == 'S':
        porcentagem_aumento = int(input('Porcentagem do aumento:'))
        cadastro['salario_final'] = cadastro['salario_base'] +(cadastro['salario_base'] * porcentagem_aumento / 100)

    funcionario_lista.append(cadastro.copy())
    cadastro.clear()

    pular_linha()

    continuar = opc()
    if continuar == 'N':
        break

pular_linha()
print()
print(f'=>    Quantidade de funcionarios cadastrados: {len(funcionario_lista)}')
print()
for f in funcionario_lista:
    print()
    print(f'.... FUNCIONÁRIO: {f['nome']} ....')
    print()
    print(f'=>    Função: {f['funcao']}')
    if f['salario_final'] > f['salario_base']:
        print(f'=>    Salário antes do aumento: R${f['salario_base']:.2f}')
        print(f'=>    Salário com aumento: R${f['salario_final']:.2f}')
    else:
        print(f'=>    Salário: R${f['salario_base']:.2f}')