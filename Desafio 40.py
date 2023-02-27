n1 = float(input('Diagite a primeira nota: '))
n2 = float(input(' digite a segunda nota '))
v = (n1+n2) /2
print('Tirando as notas {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(n1, n2 , v))
if 7 > v >=5:
    print('O aluno esta em recuperçao!!')
elif v < 5:
    print('O aluno esta reprovado!!')
else:
    print('O aluno esta aprovado')
