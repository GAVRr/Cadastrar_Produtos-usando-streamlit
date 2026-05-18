from datetime import datetime
cadastro = dict()
cadastro['Nome'] = str(input('Nome:')).strip().capitalize()
ano_nascimento = int(input('Ano de nascimento:'))
cadastro['idade'] = datetime.now().year - ano_nascimento
cadastro['Carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem):'))


if cadastro['Carteira de trabalho'] > 1:
    cadastro['Ano de contratação'] = int(input('Ano de contratação:'))
    cadastro['Salário'] = float(input('Salário:'))
    cadastro['Aposentadoria'] = cadastro['idade'] + ((cadastro['Ano de contratação'] + 35) - datetime.now().year)
print('-=-='*20)

for k,v in cadastro.items():
    print(f'{k} : {v}')
