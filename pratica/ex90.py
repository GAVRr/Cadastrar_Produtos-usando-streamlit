tabela = {}
tabela['Nome'] = str(input('Nome:')).strip().capitalize()
tabela['Média'] = float(input('Média do aluno:'))
print('-=' * 20)
if tabela['Média'] < 5.9:
    tabela['Situação'] ='\033[0;31mReprovado\033[m'
elif tabela['Média'] > 5.9 and tabela['Média'] <= 6.9 :
    tabela['Situação'] ='\033[0;33mRecuperação\033[m'
else:
    tabela['Situação'] = '\033[0;3 2mAprovado\033[m'
for k, v in tabela.items():
    print(f'{k} - {v}')