from random import randint
numero = (randint(0, 10), randint(0, 10), randint(0, 10),
          randint(0, 10), randint(0, 10))
print('Os valores escolhidos foram: ',end='')
for i in numero:
    print(i, end=' ')
print('\nO maior valor sendo {}'.format(max(numero)))
print('Enquanto o menor {}'.format(min(numero)))