from rich import print
from rich import inspect

class Funcionario:
    # Atributo de Classe

    empresa = 'WEG'

    def __init__(self , nome , setor , cargo):
        self._nome = nome
        self._setor = setor
        self._cargo = cargo


    def apresentação(self) -> str:
        return (f'Prazer meu nome é [blue]{self._nome}[/] sou do setor de [green]{self._setor}[/] e meu cargo é [red]{self._cargo}[/] na empresa [blue]{Funcionario.empresa}[/]')



pessoa = Funcionario('Gabriel', 'PDI' , 'Desenvolvedor')
print(pessoa.apresentação())
