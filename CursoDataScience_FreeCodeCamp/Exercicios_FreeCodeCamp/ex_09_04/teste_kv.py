name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
arq = open(name)
di = dict()
for line in arq:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        #print("add...")
        di[w] = di.get(w, 0) +1
largest = -1
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k

print ("Feito!, a Maior palavra é:", theword, largest)
