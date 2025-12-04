from lista_pessoa.capa import *
from lista_pessoa.arquivo import *
arq = 'Sua_Lista.txt'
if arqexiste(arq):
    print(f'Arquivo {arq} encontrado.')
else:
    print('Arquivo não encontrado!')
    CriadorArquivo(arq)
def execuções(op):
    m_capa()
    while True:
        escolha = str(input(op))
        if escolha == '1':
            print('---'*10)
            print(f'{'Pessoas Cadastradas':^30}')
            print('---'*10)
            AbrirArquivo(arq)
            m_capa()
            continue
        elif escolha == '2':
            print('---'*10)
            print(f'{'Novo Cadastro':^30}')
            print('---'*10)
            nome = str(input('Nome: '))
            idade = lendo_int('Idade: ')
            cadastrando(arq, nome, idade)
            m_capa()
            continue
        elif escolha.strip().isalpha():
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        elif escolha not in '123':
            print('\033[31mERRO! Digite uma das alternativas.\033[m')
        elif escolha == '3':
                break
    return int(escolha)
    
       
    

        