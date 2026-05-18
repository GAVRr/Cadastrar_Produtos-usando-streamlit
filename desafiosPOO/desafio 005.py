from desafiosPOO.clasCB005 import *
from rich import print
from time import sleep

db = BancodeDados()
login_pessoa = ContaBancaria()
while True:

    sleep(0.5)
    login_pessoa.linha('MENU')
    login_pessoa.menu()

    try:

        escolha = int(input('\033[1;33mOpção:\033[m '))

    except(ValueError, TypeError):

        print('[red]Opção inválida[/]')
        continue

    if escolha > 7 or escolha <= 0:
        print('[red]Essa opção não existe![/]')

    print()

    if escolha == 1:
        login_pessoa.linha('CADASTRADOS')
        contas_do_banco = db.listar_todas()

        if not contas_do_banco:
            print('[red] Nenhuma conta no banco de dados![/]')


        else:
            sleep(1)
            for registro in contas_do_banco:
                p = ContaBancaria(registro[0], registro[1], 0, registro[2], registro[3])

                p.informacoes()

    if escolha == 2:
        while True:
            try:
                login_pessoa.id_conta = int(input(('Banco:')))
                break
            except (ValueError, TypeError):
                print('[red] Todos os campos são obrigatórios! e devem conter apenas números [/]')

        while True:
            login_pessoa.pedir_nome = str(input('Nome completo do titular: ')).strip().title()
            if login_pessoa.pedir_nome:
                break
            else:
                print('[red] Todos os campos são obrigatórios! e devem conter apenas letras [/]')

        while True:
            entrada = str(input('Email do titular:'))

            email_valido = login_pessoa.email_cliente(entrada)

            if email_valido:
                login_pessoa.email = email_valido
                break

            else:
                print('[yellow]Por favor, tente novamente![/]')

        while True:

            entrada = str(input('CPF do titular:'))

            cpf_valido = login_pessoa.cpf_cliente(entrada)

            if cpf_valido:
                login_pessoa.cpf = cpf_valido
                break

            else:
                print('[yellow]Por favor, tente novamente![/]')

        print()
        print(f'[green]Conta Criada com sucesso!.[/]')
        nova_pessoa = ContaBancaria(login_pessoa.id_conta, login_pessoa.pedir_nome, 0, login_pessoa.email,
                                    login_pessoa.cpf)

        db.salvarconta(nova_pessoa)

        print()

    if not db:
        if not escolha == 1:
            print('[red]nenhuma conta aberta, impossivel realizar essa operação![/]')


    else:

        if escolha == 3:
            contas_do_banco = db.listar_todas()

            if not contas_do_banco:
                print('[red] Nenhuma conta no banco de dados![/]')

            else:
                sleep(1)
                for indice, registro in enumerate(contas_do_banco):
                    print(f'[{indice}]')
                    p = ContaBancaria(registro[0], registro[1], 0, registro[2], registro[3])

                    p.informacoes()

                while True:
                    try:
                        indice = int(input('qual conta deseja realizar o deposito:'))
                        if indice > len(contas_do_banco):
                            print('[red]Essa conta não existe[/]')
                        else:
                            valor = float(input('Valor do deposito: R$'))
                            dados_conta = contas_do_banco[indice]
                            id_no_db = dados_conta[0]
                            saldo_atual = dados_conta[4]
                            novo_saldo = saldo_atual + valor
                            db.atualizar_saldo(id_no_db, novo_saldo)
                            print('[green]Depósito realizado![/]')
                            break
                    except(ValueError, TypeError):
                        print(f'[red]Campo obrigatório![/]')

        if escolha == 4:
            contas_do_banco = db.listar_todas()

            if not contas_do_banco:
                print('[red] Nenhuma conta no banco de dados![/]')
            else:
                sleep(1)
                for indice, registro in enumerate(contas_do_banco):
                    print(f'[{indice}]')
                    p = ContaBancaria(registro[0], registro[1], 0, registro[2], registro[3])

                    p.informacoes()
                while True:
                    try:
                        saque_conta = int(input('Qual conta deseja realizar o saque:'))
                        if saque_conta > len(contas_do_banco):
                            print('[red]Essa conta não existe[/]')
                        else:
                            valor = float(input('Valor do saque: R$'))
                            dados_conta = contas_do_banco[saque_conta]
                            id_no_db = dados_conta[0]
                            saldo_atual = dados_conta[4]
                            novo_saldo = saldo_atual - valor
                            db.atualizar_saldo(id_no_db, novo_saldo)
                            print('[green]Saque feito com sucesso[/]')
                            break
                    except (ValueError, TypeError):
                        print('[red]Campo obrigatório [/]')

        if escolha == 5:
            contas_do_banco = db.listar_todas()

            if not contas_do_banco:
                print('[red] Nenhuma conta no banco de dados![/]')
            else:
                for indice, registro in enumerate(contas_do_banco):
                    print(f'[{indice}]')
                    p = ContaBancaria(registro[0], registro[1], 0, registro[2], registro[3])
                    p.informacoes()
                try:
                    indice_conta = int(input('Deseja ver o saldo de qual conta:'))
                    if 0 <= indice_conta < len(contas_do_banco):
                        conta_selecionada = contas_do_banco[indice_conta]
                        saldo_valor = conta_selecionada[4]
                        print('-' * 20)
                        if saldo_valor < 0:
                            print(f'[red]Saldo: R$ {saldo_valor}[/]')
                        else:
                            print(f'Saldo: R$ {saldo_valor:.2f}')
                    else:
                        print('[red] opção inválida[/]')
                except ValueError:
                    print('[red]Opção inválida[/]')
            sleep(1)

    print()

    if escolha == 7:
        contas_do_banco = db.listar_todas()

        if not contas_do_banco:
            print('[red] Nenhuma conta no banco de dados![/]')

        else:
            sleep(1)
            for indice, registro in enumerate(contas_do_banco):
                print(f'[{indice}]')
                p = ContaBancaria(registro[0], registro[1], 0, registro[2], registro[3])

                p.informacoes()

            while True:
                try:
                    excluir_conta = int(input('Qual conta deseja exluir:'))
                    if 0 <= excluir_conta < len(contas_do_banco):
                        id_real = contas_do_banco[excluir_conta][0]

                        confirmacao = str(
                            input(f'\033[34mTem certeza que deseja exluir essa conta? (s/n)\033[0m')).capitalize()
                        if confirmacao == 'S':
                            db.deletar_conta(id_real)
                            print('[green]Conta exluida com sucesso[/]')
                        break
                    else:
                        print('[red]Índice inválido! tente novamente[/]')


                except(ValueError, TypeError):
                    print(f'[red]Digite um número válido![/]')

    if escolha == 6:
        print('[red]Encerrando...[/]')
        sleep(1)
        break
