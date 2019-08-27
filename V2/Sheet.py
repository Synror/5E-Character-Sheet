## imports!
import Define as info
import Deekek as char
import math

## defing my own things
def printScore(line):
    print(info.abilities[line][:3], end = "")
    print(" ", end = "")
    if char.abilityScores[line] < 10:
        print("0", end = "")
    print(char.abilityScores[line], end = "")
    print(" ", end = "")
    if ((char.abilityScores[line]-10)/2) > -1:
        print("+", end = "")
    print(math.floor((char.abilityScores[line]-10)/2), end = "")
    print("  │", end = "")


def printSkills(line):
    for col in range(0,3):
        skillbonus = math.floor((char.abilityScores[info.skills[line + col][1]]-10)/2) + (char.skillProf[line + col] * 2)
        if skillbonus > -1:
            print("+", end = "")
        print(str(skillbonus) + " ", end = "")
        print(info.skills[line + col][0], end = "│")
    print("")

## and the main stuff starts here

print("┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")
firstline = char.name

if char.alignment[:1] is "E":
    firstline += ", An "
else:
    firstline += ", A "

firstline += char.alignment + " " + char.race + " " + char.levelClass



## whitespace after the first line
print("│" + firstline, end ="")
space = 119 - len(firstline)
for i in range(0,space):
    print(" ", end = "")
print("│")



print("├───────────┬───────────────┬───────────────┬───────────────┐                                                           │")
for i in range(0,6):
    print("│", end = "")
    printScore(i)
    printSkills(i*3)
