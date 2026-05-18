
import urllib.request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/110.0.0.0'}
try:
    site = urllib.request.Request('https://www.pudim.com.br',headers=headers)
    valor = urllib.request.urlopen(site)
except urllib.error.URLError as e:
    print(f'O site não está respondendo :( {e.reason}')
else:
    print(' O site está respondendo')
