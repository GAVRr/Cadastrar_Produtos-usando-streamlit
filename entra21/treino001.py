while True:
    nome = str(input('Nome: ')).capitalize()
    senha = input('Senha: ').capitalize()
    if senha == nome:
        print('Senha inválida, não pode ser o mesmo que o nome!')
        continue
    else:
        print('Senha válida')
        print(nome)
        if senha:
            print('*'* len(senha))

    ver_senha = str(input('Quer ver a senha?:')).upper()
    if ver_senha == 'S':
        print(f'Senha: {senha}')
        break