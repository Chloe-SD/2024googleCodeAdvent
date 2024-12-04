import re
# Attempt at a cleaner solution for the same problem based 
# on other solutions I saw after completing mine
total = 0
regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
with open('day3\input.txt', 'r') as file:
    content = file.read()
matches = re.findall(regex, content)
do = True
for match in matches:
    if (match == "do()"):
        do = True
    elif (match == "don't()"):
        do = False
    else:
        if (do):
            nums = re.findall(r'\d{1,3}', match)
            total += int(nums[0]) * int(nums[1])
print(total)