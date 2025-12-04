def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True
    
def CriadorArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado')
        
def AbrirArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<20}{dado[1]} anos')
    finally:
        a.close()

def cadastrando(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve ERRO ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve ERRO ao tentar escrever os dados!')
        else:
            print(f'{nome} foi registrado.')
            a.close()

def lendo_int(v):
    while True:
            try:
                inic = int(input(v))
            except (ValueError, TypeError):
                print(f'\033[31mERRO: digite um número inteiro válido!\033[m')
                continue
            except (KeyboardInterrupt):
                 print('Sistema interrompido pelo usuário!')
                 break
            return inic
          




