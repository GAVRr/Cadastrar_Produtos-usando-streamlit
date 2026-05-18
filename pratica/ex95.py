def area(l , c ):
    soma = largura * comprimento
    return soma

largura = float(input('Qual a largura do terrendo:'))
comprimento = float(input('Qual o comprimento do terrendo:'))

print(f'Um terreno de {largura} x {comprimento} tem área de  {area(largura, comprimento):.1f}m²')