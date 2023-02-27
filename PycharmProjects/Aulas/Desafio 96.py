def area(largura, comprimento):
    a=largura*comprimento
    print(f'A area de terreno {largura}x{comprimento} e de {a:.2f}m²')

print('Controle de terreno')
print('-'*30)
l=float(input('Largura (m):'))
c=float(input('Comprimento (m):'))
area(l,c)
