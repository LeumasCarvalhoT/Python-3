import os
num = []
while True:
    n = int(input('Escreva um valor: '))
    if n not in num:
        num.append(n)
        print('Armazenado com sucesso.')
    else:
        print('Número já existente, não pode ser armazenado.')
    opc = str(input('Quer continuar?[S/N] ')).lower()
    os.system('cls')
    if opc == 'não' or opc == 'n':
        break
num.sort()
print(f'Os números digitados foram {num}')