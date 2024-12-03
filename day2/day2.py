with open('day2\input.txt', 'r') as file:
    lines = file.readlines()

def safeSequence(numbers):
    inc = True
    dec = True
    for i in range(len(numbers)-1):
        if numbers[i+1] > numbers[i]:
            dec = False
        elif numbers [i+1] < numbers [i]:
            inc = False 
    if not (inc or dec):
        return False
    safe = True
    if (inc or dec):
        for i in range(len(numbers)-1):
            dif = abs(numbers[i+1] - numbers[i])
            if ((dif < 1) or (dif > 3)):
                return False
    return True


safeCount = 0

for line in lines:

    numbers = list(map(int, line.strip().split()))

    if (safeSequence(numbers)):
        safeCount += 1
        continue

    for i in range(len(numbers)):
        copy = numbers[:i] + numbers[i+1:]
        #print(f"Checking modified list with index {i} removed: {copy}")
        if safeSequence(copy):
            #print(f"Safe after removing index {i}: {copy}")
            safeCount += 1
            break
    

print(safeCount)
            