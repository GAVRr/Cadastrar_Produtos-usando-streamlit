#Declaração da classe
class Gafanhoto:
    def __init__(self):
        self.nome = ''
        self.idade = 0

    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):

        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos'

#Declaração do objeto
g1 = Gafanhoto()
g1.nome = 'Gabriel'
g1.idade = 22
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Gabriel'