def ficha(n, g):
    if not g.isnumeric():
        g=0
    if n.strip() == '':
        n = 'desconhecido'
    print(f'O jogador {n} fez {g} gol(s) no campeonato')
nome = str(input('Nome: ')).strip()
gols = str(input('Quantos gols? '))
ficha(nome, gols)
