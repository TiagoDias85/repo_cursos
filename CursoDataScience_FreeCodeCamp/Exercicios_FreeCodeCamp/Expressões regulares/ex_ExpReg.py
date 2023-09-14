import re
file = input("Insira o Arquivo:")
if len(file) < 1:
    file = "regex_sum.txt"
handle = open(file, "r")
lst = []
count = 0
nums = re.findall("[0-9]+", handle.read())
for n in nums:
    lst.append(n)
    count +=  1
lst_int = [int(nums) for nums in lst]
totsum = sum(lst_int)
print(lst)
print("Contagem:", count, "Soma Total:", totsum)
