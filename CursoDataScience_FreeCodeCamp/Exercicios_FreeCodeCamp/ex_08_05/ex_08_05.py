fname = input("Enter file name: ")
arquivo = open(fname, 'r')
count = 0
for linha in arquivo:
    palavras = linha.split()
    if len(palavras) < 3 or palavras[0] != "From":
        continue
    print(palavras[1])
    count += 1
print("There were", count, "lines in the file with From as the first word")
