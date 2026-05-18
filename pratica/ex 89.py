boletim = []
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('primeira nota: '))
    nota2 = float(input('segunda nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome , [nota1 ,nota2], media])


    continuar = ''

    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar?[S/N]').upper().strip()
        if continuar not in ['S', 'N']:
            print('\033[91mDados invalidos, tente novamente.\033[0m')
    if continuar == 'N':
        break
print('-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for i , a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    opc = int(input('Mostrar notas de qual aluno?[999 para sair]'))
    if opc == 999:
        print('Encerrando...')
        break
    if opc <= len(boletim) -1:
        print(f'Notas de {boletim[opc] [0]} sao {boletim[opc][1]}')
print('-=' * 20)