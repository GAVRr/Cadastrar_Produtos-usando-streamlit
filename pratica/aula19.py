dicionario ={}
lista = []
for c in range(0,3):
    dicionario['nome'] = str(input('Informe seu nome:'))
    dicionario['Idade'] = int(input('Informe sua idade:'))
    lista.append(dicionario.copy())
for i in lista:
    for v in i.values():
        print(f'{v} ', end =' ')
    print()

