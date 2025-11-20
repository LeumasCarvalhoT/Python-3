from time import sleep
def maior(lista):
    print('Analisando os números passados...')
    mai = 0
    for i in range(0, len(lista)):
        print(lista[i], end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(lista)} valores no total.\nSendo o maior valor o número ', end='')
    for i in range(0, len(lista)):
        if lista[i] > mai:
            mai = lista[i]
    print(F'{mai}.')
pimba = [9,8,6,4,10]
maior(pimba)
pimba = [1,1,1, 0]
maior(pimba)
pimba = []
maior(pimba)