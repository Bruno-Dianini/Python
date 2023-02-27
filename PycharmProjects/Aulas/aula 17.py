num = [4,5,9,1]
num[2]= 3 # subistitui
num.append(7)#acrescenta
#num.sort()#ordena
num.sort(reverse=True)#ordem inversa
num.insert(2,0)#acrescenta
num.pop()#deletar elementos
if 2 in num:
    num.remove(2)#remove elementos
else:
    print('Não achei o numero 2')
print(num)
print(f'Essa lista tem {len(num)} elementos')

#valores = list()
#for cont in range(0,5)
    #Valores.append(int(input('Digite um valor:')

#for c,v in  enumerate(valores): organizar
    #print(f'na poseçao {c} encontrei o valor {v}!')
#print('Cheguei no final da lista ')
