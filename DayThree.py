grid = []

with open('Inputs/DayThree.txt') as f:
    for line in f.read().splitlines():
        grid.append(line)

def getEncTreesNo(r, d):
    x = 0
    y = 0

    encTrees = 0
    xSize = len(grid[0])

    while y < len(grid):
        if x >= xSize:
            x = x - xSize

        if grid[y][x] == '#':
            encTrees += 1

        x += r
        y += d
    
    return encTrees

print("Part 1 Encountered Trees: " + str(getEncTreesNo(3, 1)))

totalTrees = getEncTreesNo(1, 1) * getEncTreesNo(3, 1) * getEncTreesNo(5, 1) * getEncTreesNo(7, 1) * getEncTreesNo(1, 2)
print("Part 2 Multiplied Encountered Trees: " + str(totalTrees))