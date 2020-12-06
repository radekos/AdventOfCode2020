sumOfAnswers = 0
duplicateCheck = set()

with open('Inputs/DaySix.txt') as f:
    for line in f.read().splitlines():
        if not line:
            #Next Line
            duplicateCheck.clear()
        else:
            for char in line:
                if char not in duplicateCheck:
                    duplicateCheck.add(char)
                    sumOfAnswers += 1

print("Part 1, Total Checks: " + str(sumOfAnswers))

sumOfAnswers = 0
noOfPeople = 0
charDict = dict()
groupLine = ""

with open('Inputs/DaySix.txt') as f:
    for line in f.read().splitlines():
        if not line:

            for char in charDict:
                if charDict[char] == noOfPeople:
                    sumOfAnswers += 1

            #Next Line
            charDict.clear()
            noOfPeople = 0
            groupLine = ""
        else:
            for char in line:
                if char in charDict:
                    charDict.update({char: charDict[char] + 1})
                else:
                    charDict.update({char: 1})

            noOfPeople += 1
            groupLine += line

for char in charDict:
    if charDict[char] == noOfPeople:
        sumOfAnswers += 1

print("Part 2, Total Checks: " + str(sumOfAnswers))