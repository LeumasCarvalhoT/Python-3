from datetime import date
def idade(ano):
    ano = date.today().year - ano 
    return ano
def votação(idade):
    if idade < 16:
        return 'Não tem idade para votar'
    elif (idade >= 16 and idade<18) or idade > 70:
        return 'Voto facultativo, não obrigatório.'
    else:
        return 'VOTO OBRIGATÓRIO!'
nascimento = int(input('Data de Nascimento: '))
nascimento = idade(nascimento)
print(f'Tendo {nascimento} anos: {votação(nascimento)}')