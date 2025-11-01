n = []
maior = menor = 0
for i in range(0, 4):
    v = int(input(f'Digite um número na posição {i}: '))
    n.append(v)
    if i == 0:
        menor = maior = v
    else:
        if menor > v:
            menor = v
        elif maior < v:
            maior = v
print(f'Você digitou os seguintes valores: {n}')
print(f'O maior valor é {maior}, localizado na posição ', end='')
for j, i in enumerate(n):
    if i == maior:
        print(f'{j}...', end='')
print()
print(f'O menor valor é {menor}, localizado na posição ', end='')
for j, i in enumerate(n):
    if i == menor:
        print(f'{j}...', end='')
