lista = [[0,0,0], [0,0,0], [0,0,0]]
pares = coluna3 = linha2 = 0
for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = int(input(f'Digite o valor para a posição {[i, j]}: '))
        if lista[i][j] % 2 == 0:
            pares += lista[i][j]
        if lista[i][j] == lista[i][2]:
            coluna3 += lista[i][2]
        if lista[1][j] > linha2:
            linha2 = lista[1][j]
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]:^5}]',end=' ')
    print()
print(f'A soma dos pares é de {pares}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'E o maior valor da segunda linha é o {linha2}')