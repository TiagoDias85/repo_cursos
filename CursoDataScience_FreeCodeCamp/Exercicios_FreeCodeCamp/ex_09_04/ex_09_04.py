name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
arq = open(name)
maxcount = 0
emails = dict()
for lines in arq:
    lines = lines.rstrip()
    lines = lines.split()
    if len(lines) >= 2 and lines[0].startswith("From:"):
        email = lines[1]
        emails[email] = emails.get(email, 0) + 1
        #print(emails)

while email in emails:
    if emails[email] >= maxcount:
        maxcount = emails[email]
    break
print(email, maxcount)
