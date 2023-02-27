def nota(*n, sit=False):
    """
    Funcao para avaliar notas
    param n:usa notas para avaliar os alunos
    """

    r =dict()
    r['total'] = len(n)
    r['Maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situaçao'] = 'boa'
        elif r['media'] >= 5:
            r['situaçao'] = 'media'
        else:
            r['situaçao'] = 'ruim'

    return r


resp = nota(10, 10, 5, 6, sit=True)
print(resp)
help(nota)