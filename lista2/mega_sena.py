from random import randint
from time import sleep
mega_sena = []
print('-='*5,'JOGO DA MEGA SENA','=-'*5)
jogos = int(input('Quantos jogos quer que sejam soteados?: '))
print('-='*5, F'SORTEANDO {jogos} JOGOS', '=-'*5 )
for i in range(0, jogos):
    for j in range(1, 7):
        n = randint(1, 60)
        for h in mega_sena:
            if n == h:
                n = randint(1, 60)
        mega_sena.append(n)
    mega_sena.sort()
    print(f'Jogo {i+1}: {mega_sena}')
    sleep(1)
    mega_sena.clear()
print('-='*5, 'BOA SORTE!', '=-'*5)





