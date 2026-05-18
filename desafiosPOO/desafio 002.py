from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self , nome: str , preco: float):
        self._nome = nome
        self._preco = preco

    def etiqueta(self) -> Panel:

        conteudo = f'{self._nome.center(30,' ')}'
        conteudo += f'{'-' * 30}'
        precof = f'R${self._preco:,.2f}'
        conteudo += f'{precof.center(30 , '.')}'

        painel = Panel(conteudo,title= 'Produto', width = 34)
        return painel


p1 = Produto('computador' , 7000)
painel_produto = p1.etiqueta()

p2 = Produto('Teclado Gamer' , 1000)
painel_produto2 = p2.etiqueta()

print(painel_produto,painel_produto2)
