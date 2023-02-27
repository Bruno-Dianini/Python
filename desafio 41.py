from datetime import date
d = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = d - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <=9:
    print('Classifição: Mirim.')
elif idade <=14:
    print('Classifição: Infantil.')
elif idade <= 19:
    print('Classifição: Junior.')
elif idade <= 25:
    print('Classifição: Senor.')
else:
    print('Classifição: Master.')
