def escreva(txt):
    tamanho = len(txt) +4
    print('~' * tamanho)
    print(f'  {txt}')
    print('~'*tamanho)

oi =str(input('Digite uma mensagem:'))
escreva(oi)