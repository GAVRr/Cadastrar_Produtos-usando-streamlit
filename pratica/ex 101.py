from datetime import date


def voto(ano_nasc):
    ano = date.today().year
    idade = ano - ano_nasc
    if idade < 16:
        return f'Você tem {idade} anos, situação de voto: NEGADO'
    elif idade >= 16 and idade < 18 or idade >= 70:
        return f'Você tem {idade} anos, situação de voto: OPCIONAL'
    else:
        return f'Você tem {idade} anos, situação de voto: OBRIGATÓRIO'


ano_nascimento = int(input('Ano de nasmineto:'))
print(voto(ano_nascimento))
