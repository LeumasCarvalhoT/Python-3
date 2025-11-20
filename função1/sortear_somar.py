from time import sleep
from random import randint
def contando(L):
    print(f'Aleatoriamente inserindo valores {len(L)} na lista: ', end=' ')
    for i in range(0, len(L)):
        print(L[i], end=' ', flush=True)
        sleep(0.5)
    print('TERMINADO!')
def somando(L, s):
    print(f'Agora somando apenas os valores pares de {L}, conseguimos ', end='')
    for i in range (0, len(L)):
        if L[i] % 2 == 0:
            s += L[i]
    print(s)
soma = 0        
tabela = []
for i in range(0, 5):
    tabela.append(randint(0,9))
contando(tabela)
somando(tabela, soma)