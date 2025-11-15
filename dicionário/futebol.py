jogador_futebol = {}
gols = []
total = 0
jogador_futebol['nome'] = str(input('Nome do(a) futebolista: '))
jogador_futebol['partidas'] = int(input(f'Quantas partidas {jogador_futebol["nome"]} jogou? '))
for i in range(0, jogador_futebol['partidas']):
    gols.append(int(input(f'Quantos gols o jogador(a) fez na {i+1}º partida: ')))
    jogador_futebol['gols'] = gols
    total += gols[i]
jogador_futebol['total'] = total
print(jogador_futebol)
print()
for j, i in jogador_futebol.items():
    print(f'A informação {j} tem como valor {i}')
print()
print(f'{jogador_futebol["nome"]} jogou {jogador_futebol["partidas"]} partidas.')
for j, i in enumerate(jogador_futebol['gols']):
    print(f'-> Na partida {j+1}º, fez {i} gols.')
print(f'Sendo um total de {jogador_futebol["total"]}')
