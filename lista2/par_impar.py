inteiro = [[], []]
for i in range(0, 7):
    par_impar = int(input(f'Informe o valor {i+1}º: ' ))
    if par_impar % 2 == 0:
        inteiro[0].append(par_impar)
    else:
        inteiro[1].append(par_impar)
print(f'''O total de valores pares foi igual à {inteiro[0]}.
Já os valores impares iguais à {inteiro[1]}.''')


