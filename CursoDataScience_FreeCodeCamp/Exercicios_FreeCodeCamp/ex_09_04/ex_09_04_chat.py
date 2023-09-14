name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
arq = open(name)
maxcount = 0
emails = dict()
for line in arq:
    line = line.rstrip()
    if line.startswith("From:"):
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1

for email in emails:
    if emails[email] == maxcount or emails[email] >= maxcount:
        maxcount = emails[email]

for email in emails:
    if emails[email] == maxcount:
        print(email, maxcount)
