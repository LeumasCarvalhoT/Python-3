informações = []
pessoas = []
menor = maior = 0
informações.append(str(input('Seu nome: ')))
informações.append(float(input('Seu peso: ')))
pessoas.append(informações[:])
menor = maior = informações[1]
informações.clear()
dec = input('Deseja continuar?[S/N]: ').upper()
while True:
    if dec == 'N' or dec == 'NÃO':
        break
    informações.append(str(input('Seu nome: ')))
    informações.append(float(input('Seu peso: ')))
    pessoas.append(informações[:])
    informações.clear()
    dec = input('Deseja continuar?[S/N]: ').upper()
print(pessoas)
for j in pessoas:
    if j[1] > maior:
        maior = j[1]
    elif j[1] < menor:
        menor = j[1]
print(f'Teve ao todo {len(pessoas)} pessoas registradas.')
print(f'O maior peso foi de {maior}. Peso de ',end='')
for i in pessoas:
    if i[1] == maior:
        print(f'[{i[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}. Peso de ',end='')
for i in pessoas:
    if i[1] == menor:
        print(f'[{i[0]}]', end=' ')
