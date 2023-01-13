import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/fewatts')
except urllib.error.URLError:
    print('O site não pode ser alcançado...')
else:
    print('Site acessado com sucesso!')
