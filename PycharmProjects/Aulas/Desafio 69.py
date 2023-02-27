maior = homem = mulher20 = 0
print('-='*30)
print('Registro de pessoas.')
print('-='*30)
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite um sexo [M/F]:')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
    print('-='*30)
    print('Novo registro')
    print('-='*30)
print('='*30)
print(f'Pessoas maiores de 18 anos:{maior}')
print(f'Sao {homem} homens cadastrados')
print(f'E temos {mulher20} mulher abaixo dos 20')
