import re

def extract_patterns():
    regex = r"mul\(\d{1,3},\d{1,3}\)"
    with open('day3\input.txt', 'r') as file:
        content = file.read()
        matches = re.findall(regex, content)
    return matches

def multiply(item):
    nums = re.findall(r'\d{1,3}', item)
    print(nums)
    if (len(nums)==2):
        return int(nums[0]) * int(nums[1])
    return 'x'


##PROGRAM##
total = 0
muls = extract_patterns()
for mul in muls:
    #print(mul)
    temp = multiply(mul)
    #print(temp)
    total += temp
    
        

print(total)
