dados = []
galeria = []
for c in range(0, 3):
    dados.append(str(input('Seu nome: ')))
    dados.append(int(input('Sua idade: ')))
    galeria.append(dados[:])
    dados.clear()
maior = menor = 0
for i in galeria:
    if i[1] >=18:
        print(f'{i[0]} é maior de idade')
        maior+=1
    else:
        print(f'{i[0]} é menor de idade')
        menor+=1
print(f'Há ao todo temos {maior} maiores e {menor} menores de idade')
