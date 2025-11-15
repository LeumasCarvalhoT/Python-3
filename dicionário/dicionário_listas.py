pessoas = {}
informações = []
cadastrados = 0
media = 0
while True:
    pessoas['nome'] = str(input('Informe o nome: '))
    pessoas['sexo'] = str(input('Informe o sexo [M/F]: ')).upper()
    if pessoas['sexo'] not in 'MF':
        while pessoas['sexo'] not in 'MF':
            print("Resposta invalida! Só pode sexo 'M' ou 'F'!")
            pessoas['sexo'] = str(input('Informe o sexo [M/F]: ')).upper()
    pessoas['idade'] = int(input('Informe a idade: '))
    informações.append(pessoas.copy())
    pessoas.clear()
    resp = str(input('Quer continuar [S/N]? ')).upper()
    if resp in 'N':
            break
    if resp not in 'SN':
        while resp not in 'SN':
            print("Resposta Invalida! Só aceitamos 'S' ou 'N'!")
            resp = str(input('Quer continuar [S/N]? ')).upper()
        if resp in 'N':
            break
for i in range(0, len(informações)):
    if informações[i]['nome']:
        cadastrados += 1    
for j in range(0, len(informações)):
    media += informações[j]['idade'] 
print(f'A) Foram ao todo cadastrados {cadastrados} pessoas.')
print(f'B) A média de idade é de {(media/cadastrados):.2f}.')
print(f'C) As mulheres cadastradas foram: ', end='')
for i in informações:
    if i['sexo'] == 'F':
        print(F'{i['nome']}.', end=' ')
print()
print(f'D) Pessoas com idade maior que a média: ')
for i in informações:
    if i['idade'] > media/cadastrados:
        print(f'nome = {i['nome']}; sexo = {i['sexo']}; idade = {i['idade']};')


         
