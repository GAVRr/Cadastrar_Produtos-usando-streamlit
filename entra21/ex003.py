queijo ,presunto = 50,50
carne = 100

dono = int(input('Quantidade de sanduiches:'))

qtd_queijo = (queijo * dono) / 1000
qtd_presunto = (presunto * dono) / 1000
qtd_carne = (carne * dono) / 1000
print()
print(f'QUANTIDADE DE INGREDIENTES PARA FAZER {dono} LANCHES')
print()
print(f'Queijo: {qtd_queijo:.3f} Kg')
print(f'Presunto: {qtd_presunto:.3f} Kg')
print(f'Carne: {qtd_carne:.3f} Kg')
