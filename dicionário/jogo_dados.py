from random import randint
from operator import itemgetter
jogadores = {'Jogador 1': randint(1,6),
             'Jogador 2': randint(1,6),
             'Jogador 3': randint(1,6),
             'Jogador 4': randint(1,6)}
for j, i in jogadores.items():
    print(f'{j} ganhou {i} no dado.')
print('+='*20)
ordenado = {}
ordenado = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
c = 1
for j, i in ordenado:
    print(f'Em {c}º lugar: {j} com {i}.')
    c+=1

#for i in jogadores:
  #  print
