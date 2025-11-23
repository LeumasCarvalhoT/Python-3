def dic(*v, sit=False):
    """
    dic(*v, sit=False):
        Função para analisar notase situações dos alunos de uma turma.
    1. v: uma ou mais notas dos alunos (aceita várias).
    2. sit: decide se mostrará ou não a situação dos alunos.
    3. return: dicionário com varias informações quanto a situação dos alunos.
    """
    d = {}
    d['total'] = len(v)
    d['maior'] = d['menor'] = v[1]
    d['media'] = 0
    for i in v:
        d['media'] += i / d['total']
        if d['maior'] < i:
            d['maior'] = i
        elif d['menor'] > i:
            d['menor'] = i
    if sit:
        if d['media'] < 5:
            d['situação'] = 'Ruim'
        elif d['media'] >= 5 and d['media'] < 7:
            d['situação'] = 'Passa'
        else:
            d['situação'] = 'Bem'
    return d
print(dic(5, 6, 6, 4, 8, 9, sit=True))
