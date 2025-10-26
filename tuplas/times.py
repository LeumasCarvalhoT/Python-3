times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia',
         'Botafogo', 'Fluminense', 'São Paulo', 'Vasco da Gama', 'Corinthians',
         'Bragantino', 'Atlético-MG', 'Grêmio', 'Ceára SC', 'Internacional', 'Santos', 
         'EC Vitória', 'Fortaleza', 'Juventude','Sport Recife')
print('-+-'*20)
print('Os 5 primeiros times são:')
for i in range(0, 5):
    print(times[i])

print('-+-'*20)
print('Os 4 últimos colocados são:')
for i in range(16, 20):
    print(times[i])

print('-+-'*20)
print('Os times em ordem alfabética:')
for i in range(0, len(times)):
    print((sorted(times)[i]))
print('-+-'*20)
print('A classificação do time {} é de {}º lugar'.format(times[8], 9))

