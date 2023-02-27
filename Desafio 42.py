r1 = float(input('Primeiro Seguimento:'))
r2 = float(input('Segundo Seguimento:'))
r3 = float(input('Terceiro Seguimento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3 :
    print('Os seguimentos a cima podem formar um triangulo:', end='')
    if r1 == r2== r3:
        print('Equilatero!')
    elif r1 != r2 != r3 != r1 :
        print('Escaleno!')
    else :
        print('Isosceles!')
else:
    print('Os seguimentoi a cima não pode formar um triamgulo !')
