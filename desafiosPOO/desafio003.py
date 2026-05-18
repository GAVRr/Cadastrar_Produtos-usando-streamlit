from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_medio:float = 0.400
    preco_kg:float = 82.40
    def __init__(self, titulo , quantidade ):
       self._titulo = titulo
       self._quantidade = quantidade

    def __str__(self):
        return f'Esse é o {self._titulo} e tem {self._quantidade} pessoas'

    def calcular_qnt_carne(self) -> float:
        return self._quantidade * Churrasco.consumo_medio

    def calcular_custo_total(self) -> float:
        return self.calcular_qnt_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self._quantidade

    def analisar(self):
        conteudo = f'Analisando o [blue]{self._titulo}[/] com [green]{self._quantidade} convidados[/]'
        conteudo += f'\nCada convidado ira consumir [red]{Churrasco.consumo_medio:.3f}g[/], sendo o preço da carne [green]R${Churrasco.preco_kg:.2f}[/]'
        conteudo += f'\nRecomendo [blue]comprar {self.calcular_qnt_carne():.3f}kg[/] de carne'
        conteudo += f'\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/]'
        conteudo += f'\nCada participante tera que pagar [green]R${self.calcular_custo_individual()}[/]'
        painel = Panel(conteudo , title = self._titulo)
        print(painel)



c1 = Churrasco('Churrasco dos amigos', 15)
c1.analisar()

c2=Churrasco('Festa na Mansão', 80)
c2.analisar()