from opc import *

cadastro = dict()
lista_cadastro = list()
while True:
    cadastro['Nome'] = str(input('Nome:')).upper().capitalize()
    cadastro['Sexo'] = str(input('Sexo:')).upper().capitalize()
    cadastro['Idade'] = int(input('Idade:'))
    lista_cadastro.append(cadastro.copy())
    cadastro.clear()

    continuar = opc()

    if continuar == 'N':
        print('Encerrando...')
        break
print('-==-'*20)

soma_idade = 0
for pessoa in lista_cadastro:
    soma_idade += pessoa['Idade']
if len(lista_cadastro) > 0:
    mediaidade = soma_idade / len(lista_cadastro)

mulheres = [mulher['Nome'] for mulher in lista_cadastro if mulher['Sexo'] == 'F']
if len(mulheres) > 0:
    print(f"=>    Lista com todas as mulheres: {', '.join(mulheres)}")
else:
    print('Não há mulheres cadastradas')

for p  in lista_cadastro:
    if p['Idade'] > mediaidade:

        print(f'=> Acima da média:        Nome: {p['Nome']} com idade de : {p['Idade']} anos')

print(f'=>    total de pessoas cadastradas: {len(lista_cadastro)}')
print(f'=>    A média de idade é: {mediaidade:.0f} anos' )
