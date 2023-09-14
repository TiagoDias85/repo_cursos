import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import io

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

# Abrir o arquivo para escrita
with io.open('resultados.txt', 'w', encoding='utf-8') as arquivo:
    for tag in tags:
        href = tag.get('href', None)
        if href:
            # Gravar o resultado no arquivo
            arquivo.write(href + '\n')

# Exibir uma mensagem de confirmação
print("Resultados salvos no arquivo resultados.txt")
