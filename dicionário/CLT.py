from datetime import date
trabalhador = {}
trabalhador['Nome'] = str(input('Nome: '))
idade = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - idade
trabalhador['carteira'] = int(input('Carteira de trabalho (Digite 0 se não tiver): '))
if trabalhador['carteira'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = 35 - (date.today().year - trabalhador['contratação']) + trabalhador['idade']
for j, i in trabalhador.items():
    print(f'- {j} sendo {i}')
