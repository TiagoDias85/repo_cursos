import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Criação de um contexto SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Abrir uma conexão e obter os dados do XML
url = 'https://py4e-data.dr-chuck.net/comments_1828348.xml'
fhand = urllib.request.urlopen(url, context=ctx)
data = fhand.read()

# Analisar o XML e obter a raiz da árvore
tree = ET.fromstring(data)

# Encontrar os elementos com a tag <count>
counts = tree.findall('.//count')

# Realizar alguma manipulação ou processamento com os elementos encontrados
# ...
tot = 0
# Exemplo de impressão dos elementos encontrados
for count in counts:
    tot += int(count.text)

print (tot)
