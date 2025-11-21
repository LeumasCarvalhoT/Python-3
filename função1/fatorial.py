def fat(v, show=False):
    """
    fat(v, show=False)
    -> Calcula o fatorial de uma valor.
    1. v: O número a ser fatorado;
    2. show: (opcional) Decide se mostra ou não a conta;
    3. returna: O valor do fatorial do valor v.
    """
    c = 1
    for j in range(v, 0, -1):
        if show:
            if j != 1:
                print(f'{j} x ', end='')
            else:
                print(f'{j} = ', end='')
        c *= j
    return c
print(fat(5, True))
