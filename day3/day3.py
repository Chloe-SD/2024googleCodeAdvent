import re

def sanitize(input_string): #pt2
    # Split on don't()
    parts = input_string.split("don't()")
    result = [parts[0]] # add first part regardless (assume do() at start)
    for part in parts[1:]:
        do_index = part.find('do()') #find first index of do()
        if do_index != -1: #ignore part if no do() is found
            result.append(part[do_index + 4:]) #add anying AFTER to first occurance of do() to result
    return ''.join(result) #return as one big stinr BC that how my part1 code handles it
    
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
text = sanitize(content) #pt2
muls = extract_patterns(text)
for mul in muls:
    #print(mul)
    temp = multiply(mul)
    #print(temp)
    total += temp
    
        

print(total)
