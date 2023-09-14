import re
handle = open("mbox-short.txt")
spam = dict()
for line in handle:
    line = line.rstrip()
    if re.search("^From:", line):
        line = line.split(":")[1]
        spam[line] = spam.get(line, 0) + 1
        #print(line)

for k, v in sorted(spam.items()):
    print(v,k)
