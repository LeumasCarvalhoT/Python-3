esc = ''
lista = []
v = c = 0
n = int(input('Informe um número: '))
print('Adicionado com sucesso.')
lista.append(n)
v += 1
while True:
    esc = str(input('Quer continuar?[S/N] ')).lower()
    if esc == 'n':
        break
    n = int(input('Informe um número: '))
    if n < lista[-1]:
        lista.append(n)
        v += 1
        print('Adicionado com sucesso.')
    else:
        c = 0
    while c < len(lista):
            if n >= lista[c]:
                lista.insert(c, n)
                v += 1
                break
            c += 1
print(f'Ao todo foram {v} números digitados.')
print(f'Os valores digitados ordem decrescente foram: {lista}')
if 5 in lista:
     print(f'O número 5 está na lista.')
else:
     print(f'O número 5 não foi encontrado!')