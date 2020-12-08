exeList = []

class Execution():
    name = ""
    value = 0

with open('Inputs/8.txt') as f:
    for line in f.read().splitlines():
        newExe = Execution()
        splitLine = line.split(" ")
        newExe.name = splitLine[0]
        newExe.value = splitLine[1]
        exeList.append(newExe)

changedIndex = 0

def runGame():
    accumulation = 0
    currentIndex = 0
    runHistory = []

    while currentIndex < len(exeList):
        if currentIndex in runHistory:
            return [accumulation, 0]

        runHistory.append(currentIndex)
        
        opName = exeList[currentIndex].name
        opValue = exeList[currentIndex].value

        if opName == "acc":
            accumulation += int(opValue)
            currentIndex += 1
        elif opName == "jmp":
            currentIndex += int(opValue)
        else:
            currentIndex += 1

    return [accumulation, 1]

print ("Day Eight")
print ("Part 1 Answer: " + str(runGame()[0]))

def flipNames(name):
    if name == "jmp":
        return "nop"
    elif name == "nop":
        return "jmp"
    else:
        return "acc"

while True:
    
    exeList[changedIndex].name = flipNames(exeList[changedIndex].name)

    results = runGame()
    if results[1] == 1:
        print ("Part 2 Answer: " + str(results[0]))
        break

    exeList[changedIndex].name = flipNames(exeList[changedIndex].name)

    changedIndex += 1
    while changedIndex < len(exeList): 
        if exeList[changedIndex].name == "acc":
            changedIndex += 1
        else:
            break

    if changedIndex == len(exeList):
        break

print ("")