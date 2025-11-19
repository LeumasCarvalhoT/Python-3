informações = []
jogador_futebol = {}
gols = []
total = 0
while True:
    jogador_futebol['nome'] = str(input('Nome do(a) futebolista: '))
    jogador_futebol['partidas'] = int(input(f'Quantas partidas {jogador_futebol["nome"]} jogou? '))
    for i in range(0, jogador_futebol['partidas']):
        gols.append(int(input(f'Quantos gols o jogador(a) fez na {i+1}º partida: ')))
    jogador_futebol['gols'] = gols[:]
    for i in gols:
        total += i
    jogador_futebol['total'] = total
    informações.append(jogador_futebol.copy())
    total = 0
    gols.clear()
    jogador_futebol.clear()
    resp = str(input('Deseja continuar [S/N]? ')).upper()
    if resp not in 'SN':
        print('Só pode S ou N!')
        while resp not in 'SN':
            resp = str(input('Deseja continuar [S/N]? ')).upper()
    elif resp in 'N':
        break
print('---'*20)
print(f'{'Cod.Nome':<15}{'gols':<16}{'total':>6}')
for j, i in enumerate(informações):
    if i['total'] == 0:
        print(F'{j} {i['nome']:<13}{'Sem rendimento'} ')
    else:
        print(F'{j} {i['nome']:<13}{str(i['gols']):<16}{i['total']:>5} ')
print('---'*20)
while True:
    dados = int(input('Deseja ver os dados de qual jogador (digite 999 para parar)?: '))
    if dados == 999:
            break
    else:
        if dados >= len(informações):
            print('Este jogador não existe!')
            dados = int(input('Deseja ver os dados de qual jogador (digite 999 para parar)?: '))
        elif dados <= len(informações):
            print('---'*20)
            print(F'LEVANTAMENTO DO JOGADOR {informações[dados]['nome']}')
            for j, i in enumerate(informações[dados]['gols']):
                print(f'No {j}º Jogo fez {i}')
            print('---'*20)

