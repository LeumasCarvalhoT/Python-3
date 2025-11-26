def reduzidor(v = 0, t = 0):    
    print('---'*15)
    print(f'\t{'FACILITADOR, FUNÇÃO':>22}')
    print('---'*15)
    def moeda(v = 0, m = 'R$' ):
        return f'{m}{v:.2f}'.replace('.',',')
    def div(v):
        d = v/2
        return d
    def mult(v):
        m = v*2
        return m
    def alto_p(v, t):
        r = v + (v * t/100)
        return r
    def baixo_p(v, t):
        r = v - (v * t/100)
        return r
    print(f'Preço analisado: \t\t{moeda(v):>5}')  
    print(f'Metade do preço:\t\t{moeda(div(v)):>5}')
    print(f'Dobro do preço: \t\t{moeda(mult(v)):>5}')
    print(f'Preço aumentado em {t}%: \t{moeda(alto_p(v, t))}')
    print(f'Preço diminuido em {t}%: \t{moeda(baixo_p(v, t))}')
