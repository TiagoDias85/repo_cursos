fname = input("Enter file name: ")
fh = open(fname)
fst_list = []
for line in fh:
    fh = line.split()
    for word in fh:
        if word not in fst_list:
            fst_list.append(word)

fst_list.sort()
print(fst_list)
