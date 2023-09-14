from urllib.request import urlopen
from bs4 import BeautifulSoup


url = input('Digite a URL - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
span_tags = soup.find_all('span', class_='comments')

soma = 0
for span in span_tags:
    numero = int(span.get_text())
    soma += numero

print("A soma dos números encontrados nas tags <span> é:", soma)
