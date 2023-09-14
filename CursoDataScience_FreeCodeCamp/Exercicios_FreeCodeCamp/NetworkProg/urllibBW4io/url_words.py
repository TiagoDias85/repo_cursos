import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Criando a lista em ordem crescente dos valores do dicionário
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

# Exibindo a lista em ordem crescente
for item in sorted_counts:
    print(item)
