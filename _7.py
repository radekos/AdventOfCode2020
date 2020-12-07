class Bag:
    allowance = 0
    bags = []

bagList = dict()

goldPossible = 0
goldBagHolds = 0

with open('Inputs/7.txt') as f:
    for line in f.read().splitlines():

        firstSplit = line.split(" contain ")

        bagName = firstSplit[0]
        bagName = bagName.removesuffix("s")

        bag = Bag()
        bag.bags = dict()
        bag.allowance = 0

        childBags = firstSplit[1]

        if "no other bags" not in childBags:
            childBags = childBags.removesuffix(".")
            bagsSplit = childBags.split(", ")
            for childBag in bagsSplit:

                cBagName = childBag[2:]
                cBagName = cBagName.removesuffix("s")

                cBag = Bag()
                cBag.bags = dict()
                cBag.allowance = childBag[0:1]

                bag.bags.update({cBagName: cBag})

        bagList.update({bagName: bag})

def recursiveSearch(bagName):

    if bagName == "shiny gold bag":
        return 1

    if not bagList[bagName].bags:
        return 0

    for cBag in bagList[bagName].bags:
        if recursiveSearch(cBag) == 1:
            return 1

def recursiveAdd(parentName, parentBag):
    if not bagList[parentName].bags:
        return int(parentBag.allowance) 

    totalBags = 0
    for key, value in bagList[parentName].bags.items():
        totalBags += int(parentBag.allowance) * int(recursiveAdd(key, value))
    
    totalBags += int(parentBag.allowance)
    return totalBags
    
for k, v in bagList.items():
    if k == "shiny gold bag":
        for bag, bagVal in bagList[k].bags.items():
            goldBagHolds += int(recursiveAdd(bag, bagVal))

    if recursiveSearch(k) == 1:
        goldPossible += 1

print("Day Seven")
print("Part 1: " + str(goldPossible))
print("Part 2: " + str(goldBagHolds))