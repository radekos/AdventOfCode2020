import timeit

curGrid = []
curGridPart2 = []

with open('Inputs/11.txt') as f:
    for line in f.read().splitlines():
        curGrid.append(list(line))
        curGridPart2.append(list(line))

# How to get a pos = y, x, starts (0, 0) goes down right (-1, 0) -> (-1, 1)
neighbours = [[-1, -1], [-1, 0], [-1, 1], 
              [0, -1] ,          [0, 1] , 
              [1, -1] , [1, 0],  [1, 1] ]

def gameOfLifeReplacement(curGrid, neighbours):
    replacements = []

    for yIndex, y in enumerate(curGrid):
        for xIndex, x in enumerate(y):
            if x == "#":
                occupiedNgh = 0

                for ngh in neighbours:
                    if yIndex + ngh[0] < 0 or yIndex + ngh[0] >= len(curGrid) or xIndex + ngh[1] < 0 or xIndex + ngh[1] >= len(y):
                        continue

                    if curGrid[yIndex + ngh[0]][xIndex + ngh[1]] == "#":
                        occupiedNgh += 1
                        if occupiedNgh >= 4:
                            break

                if occupiedNgh >= 4:
                    replacements.append([yIndex, xIndex])

            elif x == "L":
                allNghEmpty = True

                for ngh in neighbours:
                    if yIndex + ngh[0] < 0 or yIndex + ngh[0] >= len(curGrid) or xIndex + ngh[1] < 0 or xIndex + ngh[1] >= len(y):
                        continue

                    if curGrid[yIndex + ngh[0]][xIndex + ngh[1]] == "#":
                        allNghEmpty = False
                        break

                if allNghEmpty:
                    replacements.append([yIndex, xIndex])

    if len(replacements) == 0:
        return 1

    for rep in replacements:
        if curGrid[rep[0]][rep[1]] == "#":
            curGrid[rep[0]][rep[1]] =  "L"
        elif curGrid[rep[0]][rep[1]] == "L":
            curGrid[rep[0]][rep[1]] =  "#"

    return 0

result = 0

while result == 0:
    result = gameOfLifeReplacement(curGrid, neighbours)

occupiedSeats = 0

for line in curGrid:
    for char in line:
        if char == "#":
            occupiedSeats += 1

print ("Day Ten")
print ("Part 1: " + str(occupiedSeats))

def gameOfLifeReplacement(curGrid, neighbours):
    replacements = []

    for yIndex, y in enumerate(curGrid):
        for xIndex, x in enumerate(y):
            if x == "#":
                occupiedNgh = 0

                for ngh in neighbours:
                    sightStep = 1

                    while True:
                        sightY = yIndex + (ngh[0] * sightStep)
                        sightX = xIndex + (ngh[1] * sightStep)

                        if sightY < 0 or sightY >= len(curGrid) or sightX < 0 or sightX >= len(y):
                            break

                        if curGrid[sightY][sightX] == "#":
                            occupiedNgh += 1
                            break
                        elif curGrid[sightY][sightX] == "L":
                            break

                        sightStep += 1

                    if occupiedNgh >= 5:
                        break

                if occupiedNgh >= 5:
                    replacements.append([yIndex, xIndex])

            elif x == "L":
                allNghEmpty = True

                for ngh in neighbours:
                    sightStep = 1

                    while True:
                        sightY = yIndex + (ngh[0] * sightStep)
                        sightX = xIndex + (ngh[1] * sightStep)

                        if sightY < 0 or sightY >= len(curGrid) or sightX < 0 or sightX >= len(y):
                            break

                        if curGrid[sightY][sightX] == "#":
                            allNghEmpty = False
                            break
                        elif curGrid[sightY][sightX] == "L":
                            break

                        sightStep += 1

                    if not allNghEmpty:
                        break

                if allNghEmpty:
                    replacements.append([yIndex, xIndex])

    if len(replacements) == 0:
        return 1

    for rep in replacements:
        if curGrid[rep[0]][rep[1]] == "#":
            curGrid[rep[0]][rep[1]] =  "L"
        elif curGrid[rep[0]][rep[1]] == "L":
            curGrid[rep[0]][rep[1]] =  "#"

    return 0

result = 0

while result == 0:
    result = gameOfLifeReplacement(curGridPart2, neighbours)

occupiedSeats = 0

for line in curGridPart2:
    for char in line:
        if char == "#":
            occupiedSeats += 1

print ("Part 2: " + str(occupiedSeats))
print ("")