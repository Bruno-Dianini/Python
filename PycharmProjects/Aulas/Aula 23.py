try:
    a=int(input('Primerio numero:'))
    b=int(input('Segundo numero:'))
    r=a/b
#except Exception as erro:
    #print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados q vc digitou')
except ZeroDivisionError:
    print('Não e possivel dividir o numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar o erro.')
#except Exception as erro:
    #print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre muito obrigado!!')
