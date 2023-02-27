palavras = ('pao', 'feijao', 'queijo', 'macarao', 'abobrinha','sorvete', 'maionese', 'novela')
for p in palavras:
    print(f'\nNas palavras {p.upper()} temos vogais',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
