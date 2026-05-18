from rich import inspect
class ContaBancaria:

    def __init__(self , id , nome , saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso! Saldo atual R$ {self.saldo:,.2f}')
        print()


    def __str__(self):
        return f'Conta: {self.id} pertence á {self.titular} e possui R${self.saldo:,.2f} reais '


    def depositar(self , valor):
        self.saldo +=valor
        print(f'\033[1;32mDepósito de R${valor:,.2f} autorizado\033[m')
    print()

    def sacar(self,valor):
        if valor > self.saldo:
            print(f'\033[1;31mSaque NEGADO de R${valor:,.2f} na conta {self.id}. SALDO INSUFICIENTE.\033[m')
            print()
        else:
            self.saldo -= valor
            print(f'\033[1;32mSaque de R${valor:,.2f} autorizado\033[m')
        print()


c1 = ContaBancaria(123 , 'Gabriel' , 4500)
c1.sacar(1000)
print(c1)
print()
