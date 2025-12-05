def m_capa():
    lista = ['Mostrar pessoas cadastradas',
             'Cadastrar mais alguém',
             'Sair do Sistema']
    print('---'*10)
    print(f'{'Menu Principal':^30}')
    print('---'*10)
    for i in range(0, 3):
        print(f'\033[33m{i+1}\033[m - \033[34m{lista[i]}\033[m')
def so_opcoes():
    lista = ['Mostrar pessoas cadastradas',
             'Cadastrar mais alguém',
             'Sair do Sistema']
    for i in range(0, 3):
        print(f'\033[33m{i+1}\033[m - \033[34m{lista[i]}\033[m')

 

