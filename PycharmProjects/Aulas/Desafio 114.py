import  urllib
import urllib,requests

try:
    site=urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O saite pudim nao eesta acessivel no momento')
else:
    print('Consegui acessar o saite pudim')

