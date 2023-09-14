import urllib.request
import json

# Prompt para URL
url = "https://raw.githubusercontent.com/alura-challenges/aluraquiz-base/main/db.json"

response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")

info = json.loads(data)
questions = info["questions"]

for question in questions:
    title = question["title"]
    alternatives = question["alternatives"]
    print("Pergunta:", title)

    for index, alt in enumerate(alternatives, start=1):
        print(f"Alternativa {index}: {alt}")

    print()  # Linha em branco para separar as perguntas
