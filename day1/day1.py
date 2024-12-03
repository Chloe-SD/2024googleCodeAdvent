
with open('day1\input1.txt', 'r') as file:
    lines = file.readlines()

leftCol = []
rightCol = []

for line in lines:
    numbers = line.split()
    if len(numbers) == 2:
        leftCol.append(int(numbers[0]))
        rightCol.append(int(numbers[1]))
    else:
        print("error reading line")

#print(rightCol)
leftCol.sort()
rightCol.sort()
totaldifference = 0
simScore = 0

if len(leftCol) == len(rightCol):
    for i in range(len(leftCol)):
        totaldifference += abs(leftCol[i] - rightCol[i])
        
        #similarity score
        lNum = leftCol[i]
        rCount = rightCol.count(lNum)
        simScore += lNum * rCount

else:
    print("error - columns not equal")

print("Difference = ", totaldifference)
print("sim", simScore)



