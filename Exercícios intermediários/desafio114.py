import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim.com.br')