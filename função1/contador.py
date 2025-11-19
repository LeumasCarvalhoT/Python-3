from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i>f:
        while i>=f:
            print(i, end=' ', flush=True)
            i-=p
            sleep(0.5)
        print('FIM!')
    else:
        while i<=f:
            print(i, end=' ', flush=True)
            i+=p
            sleep(0.5)
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez!')
inic = int(input('Inicia: '))
fim = int(input('Termina: '))
passo = int(input('Passada: '))
contador(inic, fim, passo)
