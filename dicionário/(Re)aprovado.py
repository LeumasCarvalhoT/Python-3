estado_aluno = {}
estado_aluno['Nome']= str(input('Nome: '))
estado_aluno['Média'] = float(input(f'Média de {estado_aluno['Nome']}: '))
if estado_aluno['Média'] < 5:
    estado_aluno['Situação'] = 'Reprovado'
elif estado_aluno['Média'] >= 5 and estado_aluno['Média'] < 7:
    estado_aluno['Situação'] = 'em Recuperação'
elif estado_aluno['Média'] >= 7:
    estado_aluno['Situação'] = 'Aprovado'
print(f'- Sendo o aluno: {estado_aluno["Nome"]}')
print(f'- Com média igual a {estado_aluno['Média']}')
print(f'- Logo está {estado_aluno["Situação"]}')
