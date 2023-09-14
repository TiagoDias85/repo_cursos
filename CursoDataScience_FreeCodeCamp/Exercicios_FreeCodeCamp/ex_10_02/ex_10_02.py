name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hrs = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith("From") and not line.startswith("From:"):
        for wds in line:
            wds = line.split()
            hr = wds[5]
            hr = hr.split(":")[0]
            for hr in wds:
                hrs[hr] = hrs.get(hr, 0) +1
print(hrs)
