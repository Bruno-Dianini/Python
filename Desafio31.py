d= float(input('Digite a distancia que irra percorrer:'))
#k = d* 0.50
#m = d* 0.45
#if  d <200 :
 #   print('O valor sera R${}'.format(k))
#else:
    #print('O valor sera R${}'.format(m))

print('Voce esta preste a comeca uma vigem de {} Km'.format(d))
pre= d* 0.50 if d <= 200 else d*0.45
print('E o preço da sua passagem é de R${}'.format(pre))
