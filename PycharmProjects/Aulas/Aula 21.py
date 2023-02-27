#help()#ajuda interativa
# __doc__ especificaçao
#def funcao():
#    n1=4
#    print(f'N1 dentro vale {n1}')


#n1=2
#funcao()
#print(f'N1 fora vale {n1}')

#def soma(a=0,b=0,c=0):
#    s=a+b+c
#    return s

#r1=soma(3,2,5)
#r2=soma(2,2)
#r3=soma(6)
#print(f'Os resultados foram {r1}, {r2}, {r3}')

#def fatorial(num=1):
#    f=1
#    for c in range(num, 0, -1):
#        f*=c
#    return f
#f1= fatorial(5)
#f2=fatorial(6)
#f3=fatorial()
#print(f'Os resultados sao {f1}, {f2}, {f3}')

def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False


num=int(input('Digite um valor:'))
if par(num):
    print('E par')
else:
    print('Nao e par')

