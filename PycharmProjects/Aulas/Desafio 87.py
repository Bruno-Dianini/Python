mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = ter = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input('Digite um valor:'))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]:^5}]', end='')
        if mat[l][c] % 2 == 0:
            par += mat[l][c]
    print()
print('-=' * 30)
print(f'A soma dos numeros pares é {par}')
for l in range(0, 3):
    ter += mat[l][2]
print(f'A soma da terceira coluna é {ter}')
for c in range(0, 3):
    if c == 0:
        mai=mat[1][c]
    elif mat[1][c]> mai:
        mai = mat[1][c]
print(f'O maior valor da segunda linha é {mai}')
