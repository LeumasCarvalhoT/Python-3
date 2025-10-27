palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for pal in palavras:
    print("\nNa palavra '{}', temos as vogais: ".format(pal), end='')
    for l in pal.lower():
        if l in 'aeiou':
            print('{}'.format(l), end=' ')