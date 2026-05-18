produtos = ('lápis' , 1.75,
            'Borracha' , 2.00,
            'Caderno' , 15.90,
            'Estojo' , 25.00,
            'Transferidor' , 4.20,
            'Compasso' , 9.99,
            'Mochila' , 120.00,
            'Canetas' , 22.00,
            'Livro' , 34.80,)

for n in range(0, len(produtos)):
    if n % 2 == 0:
     print(f'{produtos[n]:.<30}',end ='')
    elif n % 2 == 1:
        print(f'R${produtos[n]:>7.2f}')