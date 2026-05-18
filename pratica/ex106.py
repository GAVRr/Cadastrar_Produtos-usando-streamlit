from opc import opc
lista_estoque = list()
def estoque(item):
    if item.isnumeric():
        return (f'[ERRO] Números não  são aceitos!')
    if item.strip() == '':
        return f' Nenhum item adicionado!'
    else:
        lista_estoque.append(item)
        return f' Item {item} Adicionado no estoque!'




while True:
    novo_item = str(input('Adicionar novo item:')).capitalize().strip()
    print()
    resultado = estoque(novo_item)
    print(resultado)
    print()

    continuar = opc()

    if continuar == 'N':
        break

print()
print('----ESTOQUE ATUAL----')

for c,i in enumerate(lista_estoque , start =1):
    print(f' {c}...{i}')

