parenteses = str(input('Informe a formula matemática: '))
pares = []
for j in (parenteses):
    if j == '(':
        pares.append('(')
    elif j == ')':
        if len(pares) > 0:
            pares.pop()
        else:
            pares.append(')')
            break
if len(pares) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta!')
