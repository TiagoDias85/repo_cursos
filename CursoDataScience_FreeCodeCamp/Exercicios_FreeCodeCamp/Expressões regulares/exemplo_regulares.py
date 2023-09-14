import re
handle = open("regex_sum.txt")
print(sum([int(n) for n in re.findall('[0-9]+', handle.read())]))
