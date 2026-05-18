def admin(adm):

    if adm == 'S':
        return True
    else:
        return False

nome = str(input('Nome: ')).capitalize()
resposta = str(input('Você é um administrador? [S/N]: ')).strip().capitalize()

if admin(resposta):
    print(f'Bem-vindo(a) administrador(a) {nome}')
else:
    print(f'Bem-vindo(a) {nome}')
