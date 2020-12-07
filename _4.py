import re

nextPassport = True
validPassportsPart1 = 0
validPassportsPart2 = 0
currentPassport = ""

def checkForValidPassportPart1(passport):
    return "byr:" in passport and "iyr:" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport

def checkForValidPassportPart2(passport):
    if "byr:" in passport and "iyr:" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        splitPassport = passport.split(" ")

        isValidChecks = 0

        for field in splitPassport:
            if checkForValidField(field):
                isValidChecks += 1

        return isValidChecks == 7
    else:
        return False
    
def checkForValidField(field):

    fieldType, val = field.split(":")   

    if fieldType == "byr" and val.isdecimal  and 1920 <= int(val) <= 2002:
        return True
    elif fieldType == "iyr" and val.isdecimal and 2010 <= int(val) <= 2020:
        return True
    elif fieldType == "eyr" and val.isdecimal and 2020 <= int(val) <= 2030:
        return True
    elif fieldType == "hgt":
        height = val[:-2]
        suffix = val[-2:]
        if suffix == "cm" and height.isdecimal and 150 <= int(height) <= 193:
            return True
        elif suffix == "in" and height.isdecimal and 59 <= int(height) <= 76:
            return True
    elif fieldType == "hcl" and val and re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', val):
        return True
    elif fieldType == "ecl" and val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    elif fieldType == "pid" and val and val.isdecimal and len(val) == 9:
        return True

    return False

with open('Inputs/4.txt') as f:

    for index, line in enumerate(f.read().splitlines()):
        
        if not line:

            if checkForValidPassportPart1(currentPassport):
                validPassportsPart1 += 1

            if checkForValidPassportPart2(currentPassport):
                validPassportsPart2 += 1
            nextPassport = True
        else:
            if nextPassport:
                nextPassport = False
                currentPassport = line
            else:
                currentPassport += " " + line


if checkForValidPassportPart1(currentPassport):
    validPassportsPart1 += 1

if checkForValidPassportPart2(currentPassport):
    validPassportsPart2 += 1


print ("Day Four")
print ("Part 1 Valid Passports: " + str(validPassportsPart1))
print ("Part 2 Valid Passports: " + str(validPassportsPart2))
print ("")