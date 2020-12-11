numbers = []

with open('Inputs/9.txt') as f:
    for line in f.read().splitlines():
        numbers.append(int(line))

def containsSum(targetNum, numberList):
    for num in numberList:
        reqNum = targetNum - num
        if reqNum != num and reqNum in numberList and reqNum > 0:
            return -1
        else:
            continue

    return targetNum

index = 0

print ("Day Nine")

preamble = 25

foundNumber = -1

while index + preamble < len(numbers):
    result = containsSum(numbers[index + preamble], numbers[index:index + preamble])
    if result != -1:
        foundNumber = result
        print ("Part 1 Answer: " + str(foundNumber))
        break

    index += 1

def continousSum():
    index = 0

    while index < len(numbers):
        additionList = []
        step = 1
        firstNumber = numbers[index]

        if (firstNumber == foundNumber):
            continue

        additionList.append(firstNumber)

        while index + step < len(numbers):
            nextNumber = numbers[index + step]

            if sum(additionList) + nextNumber > foundNumber:
                break

            additionList.append(nextNumber)

            if sum(additionList) == foundNumber:
                lowestNum = min(additionList)
                highestNum = max(additionList)

                print ("Part 2 Answer: " + str(lowestNum + highestNum))
                return 1

            step += 1
        
        index += 1

    return -1

continousSum()

print ("")