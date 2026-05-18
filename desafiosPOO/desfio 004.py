from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self , nome="" , nick="", jogo_favorito=""):
        self.nome = nome
        self.nick = nick
        self.jogo_favorito = jogo_favorito

    def pedir_input(self, mensagem):
        while True:
            valor = str(input(mensagem))
            if valor:
                return valor
            else:
                print('[red]O nome não pode estar vazio![/]')

    def info(self):

             self.nome = self.pedir_input('Nome do jogador:').title()
             print()

             self.nick = self.pedir_input(f'Nickname do {self.nome}:')
             print()

             self.jogo_favorito =self.pedir_input('Jogo favorito:').title()
             print()

    def ficha(self):
        conteudo = f'Nome verdadeiro: [blue]{self.nome}[/]'
        conteudo += f'\nNickname: [red]{self.nick}[/]'
        conteudo += f' \nJogo Favorito: [green]{self.jogo_favorito}[/]'
        painel = Panel(conteudo,title = 'Ficha do Jogador', width = 55)
        print(painel)



jogador = list()
while True:
    novo_jogador = Gamer()
    novo_jogador.info()
    jogador.append(novo_jogador)

    continuar = str(input('Deseja continuar? [S/N}:')).capitalize()
    if continuar == 'N':
        break
print()
for j in jogador:
    print(j.ficha())