class Input:
    min = 0
    max = 0
    char = ''
    pswrd = ''

fileLines = []

with open('Inputs/DayTwo.txt') as f:
    for line in f.read().splitlines():
        splitLine = line.split()

        lineInput = Input()
        lineInput.min = int(splitLine[0].split('-')[0])
        lineInput.max = int(splitLine[0].split('-')[1])
        lineInput.char = splitLine[1][0:1]
        lineInput.pswrd = splitLine[2]

        fileLines.append(lineInput)

def part1():
    correctPasswords = 0

    for passAttempt in fileLines:
        repeats = 0

        for character in passAttempt.pswrd:
            if character == passAttempt.char:
                repeats += 1
        
        if repeats >= passAttempt.min and repeats <= passAttempt.max:
            correctPasswords += 1

    return correctPasswords

print ("Part 1 Valid Passwords: " + str(part1()))

def part2():
    correctPasswords = 0

    for passAttempt in fileLines:
        posOne = False
        posTwo = False

        posOneChar = passAttempt.pswrd[passAttempt.min - 1:passAttempt.min]
        posTwoChar = passAttempt.pswrd[passAttempt.max - 1:passAttempt.max]

        posOne = posOneChar == passAttempt.char
        posTwo = posTwoChar == passAttempt.char

        if posOne != posTwo:
            correctPasswords += 1

    return correctPasswords

print ("Part 2 Valid Passwords: " + str(part2()))