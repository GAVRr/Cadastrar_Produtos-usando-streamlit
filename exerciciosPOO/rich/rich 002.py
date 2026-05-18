from rich import print
from rich.table import Table

texto = str(input('Categoria:'))
produto1 = str(input('Produto:'))

preco1 = str(input('Preço:'))

produto2= str(input('Produto:'))

preco2 = str(input('Preço'))

tabela = Table(title = 'Tabela de preços')

tabela.add_column(texto,justify= 'right', style = 'red')
tabela.add_column('Preço',justify= 'center' , style = 'blue')
tabela.add_row(produto1 , preco1)
tabela.add_row(produto2,  preco2)

print(tabela)