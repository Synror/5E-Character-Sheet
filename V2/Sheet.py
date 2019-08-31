## ┌───────────────────────────────────────────────────────────┬──────┬────────────────────────────────────────────────────┐
## │[Name], A [alignment] [race] [levelClass]                  │Traits│                                                    │
## ├─────────┬─────────┬─────────┬─────────┬─────────┬─────────┤Ideals│                                                    │
## │STR 10 +0│DEX 10 +0│CON 10 +0│INT 10 +0│WIS 10 +0│CHA 10 +0│Flaws │                                                    │
## │ (ST +2) │         │ (ST +2) │         │         │         │Bonds │                                                    │
## ├─────────┴─────────┼─────────┴─────────┼─────────┴─────────┼──────┴────────────────────────────────────────────────────┤
## │+0 Acrobatics      │+0 Insight         │+0 Performance     │Background: [background]                                   │
## │+0 Animal Handling │+0 Intimidation    │+0 Persuasion      │AC: [AC] = [ACExplaination]                                │
## │+0 Arcarna         │+0 Investigation   │+0 Religion        │Held Weapon : [wieldType][weapon]                          │
## │+0 Athletics       │+0 Medicine        │+0 Slight of Hand  │Max HP: [HP]                                               │
## │+0 Deception       │+0 Nature          │+0 Stealth         │Speed: [SPD]ft                                             │
## │+0 History         │+0 Perception      │+0 Survival        │Hit Dice: [hitDice]                                        │
## ├───────────────────┴───────────────────┴───────────────────┴───────────────────────────────────────────────────────────┤
## │Proficiencies                                                                                                          │
## │    [class]                                                                                                            │
## │[classProf]                                                                                                            │
## │    [background]                                                                                                       │
## │[backgroundProf]                                                                                                       │
## │                                                                                                                       │
## │FEATURES                                                                                                               │
## │[class & feats text]                                                                                                   │
## └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
## this is the look that i'm going for

## imports yay
import metaDefine as info
import math

# Defining my own things yay
def printlen(string, length):
    if len(string) > length:
        print(string[:length], end = "")
    else:
        print(string, end = "")
        for i in range(0,length-len(string)):
            print(" ", end="")

## levelJob (calling the dnd classes JOBS to distinguish them from programming classes)
def calcLevelJob():
    out = ""
    for jobindex in range(0,len(info.jobs)):
        if levelJob[jobindex] > 0:
            out += str(levelJob[jobindex]) + "/" + info.jobs[jobindex] + " "
    return out[:-1]


## this adds a 0 infront of any ability scores less than 10, so 9 becomes "09" and the width is standard
def calcAbilityScore(integer):
    out = ""
    if integer < 10:
        out += "0"
    out += str(integer)
    return out

## this calculates the ability modifier based of of the score that is put into it
def calcAbilityModifier(score):
    modifier = math.floor((score-10)/2)
    return addPositivePlus(modifier)

## this adds a "+" infront of an int if it is positive (or = 0)
def addPositivePlus(int):
    out = ""
    if int >= 0:
        out += "+"
    out += str(int)
    return out

def printSkills(start, stop):
    for i in range(start, stop):
        ## get the base score from ability
        ## add bonus from skill proficiencies
        ## add a "+" for positive
        ## print modifier
        print("+X", end = " ")
        ## print name of mod
        printlen(info.skillList[i][0], 16)
        print("│", end = "")

## at some point there is gonna be some file handling or something here
name = "Deekek"
alignment = "NG"
race = "Aarakocra"
abilityScores = [6,13,14,13,12,16]
levelJob = [0]*12
startingJob = 9
levelJob[startingJob] = 7 # level 7

traits = "I am well known as a merchent around Eutharia"
ideals = "To have Eutaria see peace"
flaws  = "I am simple minded and prone to forgetting"
bonds  = "My Friends, Wife and Magic Hat"

## and the fun begins (each new line has a space between)

print("┌───────────────────────────────────────────────────────────┬──────┬────────────────────────────────────────────────────┐")

print("│", end = "")
printlen(name + ", A " + alignment + " " + race + " " + calcLevelJob(), 59)
print("│Traits│", end="")
printlen(traits, 52)
print("│")

print("├─────────┬─────────┬─────────┬─────────┬─────────┬─────────┤Ideals│", end = "")
printlen(ideals, 52)
print("│")

print("│", end = "")
for i in range(0,6):
    print(info.abilities[i][:3] + " " + calcAbilityScore(abilityScores[i]) + " " + calcAbilityModifier(abilityScores[i]), end = "│")
print("Flaws │", end = "")
printlen(flaws, 52) ## this is where the flaws text will go
print("│")

print("│", end = "")
for i in range(0,6):
    if info.savingThrowList[startingJob][i]:
        print(" (ST +2) │", end = "")
    else:
        print("         │", end = "")
print("Bonds │", end = "")
printlen(bonds, 52) ## this is where the flaws text will go
print("│")

print("├─────────┴─────────┼─────────┴─────────┼─────────┴─────────┼──────┴────────────────────────────────────────────────────┤")

for i in range(0,6):
    print("│", end = "")
    printSkills(i*3,(i+1)*3)
    printlen("", 59)
    print("│")

print("├───────────────────┴───────────────────┴───────────────────┴───────────────────────────────────────────────────────────┤")

## featuers or something

print("└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘")
