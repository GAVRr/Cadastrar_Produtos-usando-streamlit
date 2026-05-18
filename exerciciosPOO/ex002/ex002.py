#Declaração da classe
class Gafanhoto:
    def __init__(self , nome , idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade = self.idade + 1


    def __str__(self): # DUNDER METHOD
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos'

    def __getstate__(self):
        return f'Estado: Nome {self.nome} idade {self.idade}'

#Declaração do objeto
g1 = Gafanhoto('Gabriel',22)
g1.aniversario()
print(g1)
print(g1.__dict__)
print(g1.__getstate__())

