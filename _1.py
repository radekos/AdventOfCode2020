list = []

with open('Inputs/1.txt') as f:
    for line in f.read().splitlines():
      list.append(int(line))

def part1():
  for item in list:
    testVal = 2020 - item
    if testVal in list:
      return item * testVal

def part2():
  index = 0
  for item in list:
    index += 1

    for item2 in list[index:]:
      testVal = 2020 - item - item2
    
      if testVal in list:
        return item * item2 * testVal

print("Day One")
print("Part 1 Answer: " + str(part1()))
print("Part 2 Answer: " + str(part2()))
print("")