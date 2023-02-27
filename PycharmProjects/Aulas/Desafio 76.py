lista = ('Lapis', 2, 'Boracha', 3, 'Caderno', 5, 'Livro', 45, 'Estojo',3 ,'Canetas', 10.45, 'Mochila', 50.50)
print('-'*40)
print('{:.^40}'.format('Listageem de Preço'))
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>3.2f}')
print('-'*40)
