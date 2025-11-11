estado = {}
brasil = []
for c in range(0, 3):
    estado['estado'] = str(input('Informe o Estado: '))
    estado['sigla'] = str(input('Coloque a sigla: '))
    brasil.append(estado.copy())
for i in brasil:
    print(f'{i["estado"]}, {i["sigla"]}')