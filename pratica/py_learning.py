quantidade_funcionarios = 0
lista_cadastro = []

def pular_linha():
    print('-'*30)


def aumento_salario(salario):
    porcentagem = int(input('Qual a porcentagem de aumento?:'))
    porcentagem_aumento = salario_funcionario * (porcentagem / 100)
    salario_final = salario_funcionario + porcentagem_aumento
    pular_linha()
    print(f'Novo salario: {salario_final:.2f}')
    pular_linha()
    return salario_final

while True:
  nome_funcionario = str(input('Nome do funcionário:')).capitalize().strip()
  quantidade_funcionarios += 1
  funcao_funcionario = str(input('Função do funcionário:')).capitalize().strip()
  salario_funcionario = float(input('Salário do funcionario R$'))


  pular_linha()

  aumento = ""
  salario_aumento = salario_funcionario

  while aumento not in ['S', 'N']:
      aumento = input('Aplicar aumento?: [S/N] ').upper().strip()
      if aumento not in ['S', 'N']:
          print('\033[91mDados inválidos, tente novamente.\033[0m')

  if aumento == 'S':
      salario_aumento = aumento_salario(salario_funcionario)

  informaçoes = ('Nome:', nome_funcionario,
                     'Função:', funcao_funcionario,
                     'salário sem aumento: R$', salario_funcionario,
                     'Salário com aumento:', salario_aumento
                     )
  lista_cadastro.append(informaçoes)


  continuar = ""

  while continuar not in ['S', 'N']:
      continuar = input('Deseja cadastrar mais funcionários?[S/N]').upper().strip()
      if continuar not in ['S', 'N']:
          print('\033[91mDados invalidos, tente novamente.\033[0m')
  if continuar == 'N':
      break

print(f'Quantidade de funcionários cadastrados: {quantidade_funcionarios}')
pular_linha()
print('CADASTRADOS')
for funcionario in lista_cadastro:
    pular_linha()
    for i in range(0, len(funcionario), 2):
        if 'Salário' in str(funcionario[i]):
            print(f"{funcionario[i]} R${funcionario[i + 1]:.2f}")
        else:
         print(f"{funcionario[i]} {funcionario[i + 1]}")


