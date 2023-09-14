import urllib.request
from bs4 import BeautifulSoup
import os

save_directory = r"C:\Users\tiago\Desktop\Dev\Projetos Python\NetworkProg\urllibBW4io\imgs_teste"  # Especifique o diretório desejado

url = input("Insira o link: ")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read()


soup = BeautifulSoup(html, "html.parser")
img_tags = soup.find_all("img")

for img_tag in img_tags:
    img_url = img_tag.get("src")
    try:
        filename = img_url.split("/")[-1]
        save_path = os.path.join(save_directory, filename)  # Caminho completo para o arquivo
        urllib.request.urlretrieve(img_url, save_path)
        print("Imagem baixada:", filename)
    except Exception as e:
        print("Ocorreu um erro ao baixar a imagem:", str(e))
