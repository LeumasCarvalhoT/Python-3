def so_numero():
    v = str(input('Digite um número: '))
    if not v.isnumeric():
        while not v.isnumeric():
            print('\033[31mERRO! Valor inválido:\033[m ')
            v = str(input('Digite um número: '))
    return v
valor = so_numero()
print(f'Acabastes de informar o número: {valor}')
       
    