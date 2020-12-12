numbers = []

with open('Inputs/10.txt') as f:
    for line in f.read().splitlines():
        numbers.append(int(line))

numbers.sort()

oneDiff = 0
twoDiff = 0
thrDiff = 0

currentJoltage = 0

while True:
    if currentJoltage == max(numbers):
        currentJoltage += 3
        thrDiff += 1
        break
    elif currentJoltage + 1 in numbers:
        currentJoltage += 1
        oneDiff += 1
    elif currentJoltage + 2 in numbers:
        currentJoltage += 2
        twoDiff += 1
    elif currentJoltage + 3 in numbers:
        currentJoltage += 3
        thrDiff += 1
    
result = oneDiff * thrDiff

print ("Day Ten")
print ("Part 1: " + str(result))

combinationScore = {0: 1}

for n in numbers:
    combinationScore[n] = combinationScore.get(n-3, 0) + combinationScore.get(n-2, 0) + combinationScore.get(n-1, 0)

print ("Part 2: " + str(combinationScore[numbers[-1]]))
print ("")