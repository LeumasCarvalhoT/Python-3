parenteses = str(input('Informe a formula matemática: '))
soma = 1+1
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
print(soma)
if len(pares) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta!')
