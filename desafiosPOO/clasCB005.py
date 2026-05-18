from validate_docbr import CPF
from rich import print
from rich.panel import Panel
import sqlite3

dinheiro = list()


class ContaBancaria:
    def __init__(self, Banco=00, nome='desconhecido', saldo=0, email='Não informado', cpf=''):
        self.Banco = Banco
        self.titular = nome
        self.saldo = saldo
        self.email = email
        self.cpf = cpf

        print()

    def pedir_valor(self, dinheiro) -> float:
        while True:
            try:
                valor = float(dinheiro)
                return valor
            except(ValueError, TypeError):
                print('[red] [ERRO] O campo não pode estar vazio, e deve conter apenas números[/]')

    def pedir_nome(self, nome):
        self.titular = nome
        return self.titular

    def email_cliente(self, email_usuario):

        self.email = str(email_usuario).strip()

        if not self.email:
            print('[red] O e-mail não pode estar vazio![/]')
            return None

        if len(self.email) < 5:
            print('[red] E-mail muito curto para ser válido[/]')
            return None

        if self.email.isdigit():
            print('[red] e-mail não pode conter apenas números[/]')
            return None

        if self.email.startswith('@') or self.email.startswith('.'):
            print('[red] E-mail inválido,não pode iniciar com "@" ou "." [/]')
            return None

        if self.email.endswith('.') or self.email.endswith('@'):
            print('[red] E-mail inválido,não pode terminar  com "@" ou "." [/]')
            return None

        if "@" not in self.email or "." not in self.email:
            print('[red]O e-mail deve obrigatoriamente ter pelo menos um "@" e um "."[/]')
            return None

        if "@" not in self.email:
            print('[red]E-mail precisa ter um "@"[/]')
            return None

        if "." not in self.email.split("@")[-1]:
            print('[red]E-mail precisa de um ponto após o "@" (ex: .com)[/]')
            return None


        else:
            return self.email

    def cpf_cliente(self, cpf_):
        cliente_ = str(cpf_)
        if len(cliente_) < 11 or len(cliente_) > 11:
            print('[red]CPF inválido[/]')
        else:
            return cliente_

    def id_conta(self, num: int):
        self.Banco = int(num)
        return self.Banco

    def deposito(self, num):
        valor = float(num)
        if valor <= 0:
            print('[red] Impossível depositar esse valor![/]')
        else:
            self.saldo += valor
            dinheiro.append(self.saldo)
            if len(dinheiro) > 1:
                dinheiro.pop(0)

            print(f'[green]Deposito de R${valor} feito com sucesso![/]')

            return valor

    print()

    def sacar(self, num):
        valor = float(num)
        if valor > self.saldo:
            print(f'[red]Saque NEGADO de R${valor:,.2f}. SALDO INSUFICIENTE.[/]')
            print()
        else:
            self.saldo -= valor
            print(f'[green]Saque de R${valor:,.2f} autorizado[/]')

    def menu(self):
        opcoes = list()
        opcoes.append('Ver contas cadastradas')
        opcoes.append('Abrir nova conta')
        opcoes.append('Depositar')
        opcoes.append('Sacar')
        opcoes.append('Ver saldo')
        opcoes.append('Sair do sistema')
        opcoes.append('Exluir conta')
        for i, op in enumerate(opcoes):
            print(f'[yellow]{i + 1}[/] - [blue]{op}[/]')
        print('-' * 30)

    def linha(self, msg):
        tamanho = len(msg) + 30
        print('-' * tamanho)
        print(f'               {msg}')
        print('-' * tamanho)

        print()

    def informacoes(self):

        txt_banco = f"Banco: {self.Banco:03}"
        txt_nome = f"Titular: {self.titular}"
        txt_email = f'Email: {self.email}'
        txt_cpf = "".join(filter(str.isdigit, str(self.cpf)))

        cpf_corrigido = txt_cpf.zfill(11)

        cpf_handler = CPF()
        txt_cpf_formatado = f"CPF: {cpf_handler.mask(cpf_corrigido)}"

        texto_final = f"{txt_banco}\n{txt_nome}\n{txt_email}\n{txt_cpf_formatado}"
        detalhe = Panel(texto_final, title='Detalhes da conta', width=50)
        print(detalhe)


class BancodeDados:

    def __init__(self, db_name='banco_dedados.db'):
        self.db_name = db_name
        self._criar_tabela()

    def _criar_tabela(self):
        conector = sqlite3.connect(self.db_name)
        cursor = conector.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Banco INTEGER,
                titular TEXT,
                cpf TEXT,
                email TEXT,
                saldo REAL
                
            )
        """)
        conector.commit()
        conector.close()

    def salvarconta(self, conta):
        cpf_formatado = "".join(filter(str.isdigit, str(conta.cpf))).zfill(11)

        valor_saldo = float(conta.saldo)

        conector = sqlite3.connect(self.db_name)
        cursor = conector.cursor()

        cursor.execute("""
                    INSERT INTO contas (Banco, titular,email,cpf,saldo)
                    VALUES (?,?,?, ?, ?)
                """, (conta.Banco, conta.titular, conta.email, cpf_formatado, valor_saldo))

        conector.commit()

        conector.close()

    def listar_todas(self):
        conector = sqlite3.connect(self.db_name)
        cursor = conector.cursor()
        cursor.execute("SELECT Banco,  titular,email, cpf,saldo FROM contas")
        rows = cursor.fetchall()
        conector.close()
        return rows

    def atualizar_saldo(self, id_conta, novo_saldo):
        with  sqlite3.connect(self.db_name) as conector:
            cursor = conector.cursor()
            cursor.execute("""
            UPDATE contas 
            SET saldo = ? 
            WHERE Banco = ?
        """, (novo_saldo, id_conta))

            conector.commit()

    def deletar_conta(self, id_conta):
        with sqlite3.connect(self.db_name) as conector:
            cursor = conector.cursor()
            cursor.execute("DELETE FROM contas WHERE Banco = ?", (id_conta,))
            conector.commit()
