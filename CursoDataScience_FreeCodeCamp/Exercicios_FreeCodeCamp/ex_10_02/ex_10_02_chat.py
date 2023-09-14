name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hrs = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        hrs[hour] = hrs.get(hour, 0) + 1

for hour, count in sorted(hrs.items()):
    print(hour, count)
