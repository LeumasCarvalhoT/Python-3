order = []
for i in range(0, 5):
    n = int(input('Digite um número: '))
    if i == 0 or n >= order[-1]:
        order.append(n)
        print('Número adicionado no final da lista.')
    else:
        ord = 0
        while ord < len(order):
            if n <= order[ord]:
                order.insert(ord, n)
                print(f'Número adicionado na posição {ord} da lista,')
                break
            ord+=1

print(f'Os números digitados foram: {order}')