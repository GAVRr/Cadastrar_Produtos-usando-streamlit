cpf = input('Digite o CPF: ')
soma = 0
multiplicador = 10
for i in range(9):
    soma += int(cpf[i]) * multiplicador
    multiplicador -= 1

resto = (soma * 10) % 11
digito_1 = resto if resto < 10 else 0


soma = 0
multiplicador = 11
for i in range(10):
    soma += int(cpf[i]) * multiplicador
    multiplicador -= 1

resto = (soma * 10) % 11
digito_2 = resto if resto < 10 else 0


if int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2:
    print(f" O CPF {cpf} é VÁLIDO!")
else:
    print(f" O CPF {cpf} é INVÁLIDO!")