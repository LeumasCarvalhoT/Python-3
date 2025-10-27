lista = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)
print('='*40)
print('{:^40}'.format('Lista de Preços'))
print('='*40)
for posi in range(0, len(lista)):
    if posi % 2 == 0:
        print('{:.<30}'.format(lista[posi]), end='')
    else:
        print('R${:>7.2f}'.format(lista[posi]))

  