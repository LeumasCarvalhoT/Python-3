boletim = []
alunos = []
while True:
    alunos.append(str(input('Nome do aluno(a): ')))
    alunos.append(float(input('Nota 1: ')))
    alunos.append(float(input('Nota 2: ')))
    boletim.append(alunos[:])
    alunos.clear()
    resp = input('Deseja continuar?[S/N]: ').upper()
    if resp == 'N':
        break
print(f'{'No.':<5}{'Nome':<8}{'Média':>5}')
for i , j in enumerate(boletim):
    print(f'{i:<5}{j[0]:<8}{(j[1] + j[2]) / 2:>5}')
while True:
    notas = int(input('Mostrar as notas de qual aluno?(Interropa informando 999): '))
    if notas == 999:
        break  
    elif notas <= len(boletim):
        print(f'As notas de {boletim[notas][0]} são: {boletim[notas][1]} e {boletim[notas][2]}')
        print('-+-'*10)


    