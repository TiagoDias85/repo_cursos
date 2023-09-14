import requests
from bs4 import BeautifulSoup

url = 'https://spacetoday.com.br/'  # Substitua pela URL desejada

# Fazer a solicitação GET para a URL
response = requests.get(url)

if response.status_code == 200:
    # Extrair o conteúdo HTML da resposta
    html_content = response.content

    # Criar um objeto BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar todas as divs que possuem a classe contendo "vlog" no texto
    divs = soup.find_all('div', class_=lambda c: c and 'vlog' in c)

    # Imprimir as divs encontradas
    if divs:
        for div in divs:
            print(div)
    else:
        print("Nenhuma div encontrada com a classe contendo 'vlog'.")

else:
    print('Erro ao fazer a solicitação:', response.status_code)
