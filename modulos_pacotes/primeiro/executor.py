from meu_modulo import moeda, dobro, metade, mais_porc, menor_porc 
valor = int(input('Digite o valor: '))
taxa = int(input('Qual o valor da taxa (Digite zero(0) para anular)? '))
print(f'A metade de {moeda(valor)} é igual a {moeda(metade(valor))}')
print(f'O dobro de {moeda(valor)} é {moeda(dobro(valor))}')
if taxa != 0: 
    print(f'R${moeda(valor)} aumentado em {taxa}% é R${moeda(mais_porc(valor,taxa))}')
    print(f'R${moeda(valor)} diminuido em {taxa}% é R${moeda(menor_porc(valor,taxa))}')
