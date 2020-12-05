
fileLines = []

with open('Inputs/DayFive.txt') as f:
    for line in f.read().splitlines():
        fileLines.append(line)

highestID = 0
allIds = []

for boardingPass in fileLines:

    lowerRow = 0
    upperRow = 127
    lowerCol = 0
    upperCol = 7

    for index, character in enumerate(boardingPass):
        if index < 7:
            if character == "F":
                upperRow = upperRow - -(-(upperRow - lowerRow) // 2)
            elif character == "B":
                lowerRow = lowerRow + -(-(upperRow - lowerRow) // 2)
        else:
            if character == "L":
                upperCol = upperCol - -(-(upperCol - lowerCol) // 2)
            elif character == "R":
                lowerCol = lowerCol + -(-(upperCol - lowerCol) // 2)

        if index > 8:
            multipliedId = upperRow * 8 + upperCol
            if highestID < multipliedId:
                highestID = multipliedId
            allIds.append(multipliedId)

print("Part 1, Highest Seat ID: " + str(highestID))

allIds.sort()
prevId = allIds[0]

for id in allIds:
    if id != prevId and id != (prevId + 1):
        print("Part 2, My Seat ID: " + str(prevId + 1))
    prevId = id
