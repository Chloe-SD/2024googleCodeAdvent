import re

def sanitize(input_string):
    # Split on don't() and keep even parts (0,2,4...)
    parts = input_string.split("don't()")
    result = [parts[0]]
    for part in parts[1:]:
        #print("part:\n"+part)
        do_index = part.find('do()')
        if do_index != -1:
            #print("found:\n"+part[do_index + 4:])
            result.append(part[do_index + 4:])
    return ''.join(result)
    
    


def extract_patterns(text):
    regex = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(regex, text)
    return matches

def multiply(item):
    nums = re.findall(r'\d{1,3}', item)
    print(nums)
    if (len(nums)==2):
        return int(nums[0]) * int(nums[1])
    return 'x'


##PROGRAM##
total = 0
with open('day3\input.txt', 'r') as file:
    content = file.read()
text = sanitize(content)
muls = extract_patterns(text)
for mul in muls:
    #print(mul)
    temp = multiply(mul)
    #print(temp)
    total += temp
    
        

print(total)
