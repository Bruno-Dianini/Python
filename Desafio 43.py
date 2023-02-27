pe = float(input('Dgite seu peso? (kg):'))
al = float(input('Digite sua altura? (m):'))
imc = pe / (al ** 2)
if imc < 18.5:
    print('Vocé esta abaixo do peso!.')
elif 18.5 <= imc < 25:
    print('Voce esta no peso ideal!')
elif 25 <= imc < 30:
    print('Voce esta com sobre peso!')
elif 30<= imc <  40:
    print('Voce tem obesidade!')
else:
    print('Voce tem obesidade morbida !')
print('E seu IMC é {:.1f}'.format(imc))
