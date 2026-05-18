try:
    a = int(input('Digite um número:'))
    b = int(input('Digite outro numero:'))
    r = a/b
except Exception as erro:
    print(f'Encontramos um erro {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')