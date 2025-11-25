l_c = ('\033[m',           #0 Sem cores
       '\033[0;30;41m',    #1 vermelho
       '\033[0;30;42m',    #2 verde
       '\033[0;30;43m',    #3 amarelo
       '\033[0;30;44m',    #4 azul
       '\033[0;30;45m',    #5 roxo
       '\033[0;30;47m'     #6 branco
        )
def ajuda(com):
    help(com)
def titulo(m, color=0):
    t = len(m) +2
    print(l_c[color])
    print('~'*t)
    print(f" {m}")
    print('~'*t)
    print(l_c[0])
comando = ''
while True:
    titulo('Sistema Ajuda, Python', 2)
    comando = str(input("Função ou Biblioteca (Digite um 'FIM' para finalizar): "))
    titulo(f'Acessando o manual do camando {comando}', 4)
    if comando.upper() == 'FIM':
        break
    else:
        print(l_c[6])
        ajuda(comando)
        print(l_c[0])
titulo('ATÉ BREVE', 1)