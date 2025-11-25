def moeda(v = 0, m = 'R$'):
    return f'{m}{v:.2f}'.replace('.',',')
def metade(v):
    div = v/2
    return div
def dobro(v):
    mult = v*2
    return mult
def mais_porc(v, p):
    porc = v + (v * p/100)
    return porc
def menor_porc(v, p):
    porc = v - (v * p/100)
    return porc