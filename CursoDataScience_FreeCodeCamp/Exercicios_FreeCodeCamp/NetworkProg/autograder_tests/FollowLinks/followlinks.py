import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup

# Criação do contexto SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Solicita a entrada do usuário para a URL, número de repetições e posição
url = input("Digite a URL: ")
count = int(input("Digite o número de repetições: "))
position = int(input("Digite a posição: "))
print("Recuperando:", url)

n = 0  # contador inicializado

while True:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    if n == count:
        break

    for tag in tags:
        # Verifica se a posição da tag é igual à posição desejada
        if tags.index(tag) == (position - 1):
            # Recupera o valor do atributo "href" da tag
            link = tag.get("href", None)
            print("Recuperando:", link)
            url = link  # Atualiza a URL para a próxima iteração
            n += 1  # Incrementa o contador
            continue

print("Concluído.")
