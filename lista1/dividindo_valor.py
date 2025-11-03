numero = []
par = []
impar = []
while True:
    numero.append(int(input('Digite um número: ')))
    dec = str(input('Quer continuar?[S/N]: ')).lower()
    if dec in 'n':
        break
for i in numero:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'A lista completa se constitue de {numero}')
print(f'A lista de números é de {par}')
print(f'Já os números impares: {impar}')

    
    