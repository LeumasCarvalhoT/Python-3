import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://pudim.com.br/')
except urllib.error.URLError:
    print('O está está indisponível no dado momento')
else:
    print('Acessado com sucesso')