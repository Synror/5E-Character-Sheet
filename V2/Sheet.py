## ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
## │[Name], A [alignment] [race] [levelClass]                                                                              │
## ├─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬──────┬────────────────────────────────────────────────────┤
## │ STR: 10 │ Dex: 10 │ Con: 10 │ Int: 10 │ Wis: 10 │ Int: 10 │Traits│                                                    │
## ├─────────┴─────────┼─────────┴─────────┼─────────┴─────────┤Ideals│                                                    │
## │+0 Strength ST     │+0 Dexterity ST    │+0 Constitution ST │Flaws │                                                    │
## │+0 Intelligence ST │+0 Wizdom ST       │+0 Charisma ST     │Bonds │                                                    │
## ├───────────────────┼───────────────────┼───────────────────┼──────┴────────────────────────────────────────────────────┤
## │+0 Acrobatics      │+0 Insight         │+0 Performance     │Background: [background]                                   │
## │+0 Animal Handling │+0 Intimidation    │+0 Persuasion      │AC: [AC] = [ACExplaination]                                │
## │+0 Arcarna         │+0 Investigation   │+0 Religion        │Held Weapon : [wieldType][weapon]                          │
## │+0 Athletics       │+0 Medicine        │+0 Slight of Hand  │Max HP: [HP]                                               │
## │+0 Deception       │+0 Nature          │+0 Stealth         │Speed: [SPD]ft                                             │
## │+0 History         │+0 Perception      │+0 Survival        │Hit Dice: [hitDice]                                        │
## ├───────────────────┴───────────────────┴───────────────────┴───────────────────────────────────────────────────────────┤
## │Proficiencies                                                                                                          │
## │    Sorcerer                                                                                                           │
## │Darts, Daggers Slings ect                                                                                              │
## │    [background]                                                                                                       │
## │[backgroundProf]                                                                                                       │
## │                                                                                                                       │
## │Features                                                                                                               │
## │    Sorcerer                                                                                                           │
## │1st: Sorcerous origin, spellcasting ect                                                                                │
## └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
## this is the look that i'm going for

## __TODOD__
## print the Proficiencies and Features
## info calculations in printMiscInfo()
## File handling for use with multiple characters
## ability to make new characters

## imports yay
import metaDefine as info
import math

# Defining my own things yay

## this function is for printing with whitespace
def printlen(string, length):
    if len(string) > length:
        print(string[:length], end = "")
    else:
        print(string, end = "")
        for i in range(0,length-len(string)):
            print(" ", end="")

## levelJob is for figuring out what level and class your character is for the first line
def calcLevelJob():
    out = ""
    for i in range(0,len(job)):
        out += str(level[i]) + "/" + info.jobs[job[i]] + " "
    return out[:-1]


## this adds a 0 infront of any ability scores less than 10, so 9 becomes "09" and the width is standard
def calcAbilityScore(integer):
    out = ""
    if integer < 10:
        out += "0"
    out += str(integer)
    return out

## this calculates the ability modifier based of of the score that is put into it
def calcAbilityModifier(score, profExpert):
    modifier = math.floor((score-10)/2)
    ## this adds a "+" infront of an int if it is positive (or = 0)
    modifier += profExpert * profBonus ## times the actual prof bonus, this way if expertise is doing something we can pass in 2 for the mod instead of 1
    out = ""
    if modifier >= 0:
        out += "+"
    out += str(modifier)
    ## and return!
    return out

## i wraped this into a function because it makes it easy for me to call it later on


def printSkills(baseScore, profExpert, text):
    printlen(calcAbilityModifier(baseScore, profExpert) + " " + text, 19)
    print("│", end = "")

## at some point there is gonna be some file handling or something here
name = "Deekek"
alignment = "NG"
race = "Aarakocra"
abilityScores = [6,13,14,13,12,16]
job = [9]
level = [7]
skillProf = [[0]*6,[0]*18]
skillProf[0][2] = 1 ## base these off of info.savingThrowList[job[0]][i]
skillProf[0][5] = 1
skillProf[1][3] = 1 ## now all i need to do is remember what skills Deekek has
print(skillProf)
## Equipment (Armour & Weapons) (probably gonna be 2 different variables)
## background = int corrisponding with whatever background
## heldWeapon = int corrisponding with the weapon list

## flavortext (keep it short or it'll just not write the first however many characters)
traits = "I am well known as a merchant around Eutharia"
ideals = "To have Eutaria see peace"
flaws  = "I am simple minded and prone to forgetting"
bonds  = "My Friends, Wife and Magic Hat"

## Prof bonus, AC ect are compleatly calculatable
characterLevel = 0
for i in range(0,len(level)):
    characterLevel += level[i]
profBonus = 2 + math.floor((characterLevel-1)/4)

AC = 12 ## calculation needs to go here but this'll do for now
ACExp = "10 Unarmoured + 2 Dexterity" ## this will prolly be it's own function tbh
WeaponChoiceStr = "Quarterstaff" ## calc from new variable to be stored
maxHP = 48 ## calc from hp rolls and CON
speed = [25, 50] ## calc from race 2nd in array for flight speed
hitDice = "7d6" + " /LR"  ## calc from how many levels in a class (per long rest as they regen)
backgroundStr = "Merchant"

miscInfo = ["Max HP: " + str(maxHP), "AC: " + str(AC) + " = " + ACExp, "Held Weapon: " + WeaponChoiceStr, "Speed: " + str(speed), "Hit Dice: " + hitDice, "Backgroud: " + backgroundStr]

## and the fun begins (each new line has a space between) but this is where all of the prints go

print("┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")


print("│", end = "")
printlen(name + ", A " + alignment + " " + race + " " + calcLevelJob(), 119)
print("│")


print("├─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬──────┬────────────────────────────────────────────────────┤")


print("│", end = "")
for i in range(0,6):
    print(" " + info.abilities[i][:3] + ": " + calcAbilityScore(abilityScores[i]) + " │", end = "")
print("Traits│", end="")
printlen(traits, 52)
print("│")


print("├─────────┴─────────┼─────────┴─────────┼─────────┴─────────┤Ideals│", end = "")
printlen(ideals, 52)
print("│")


print("│", end = "")
for i in range(0,3):
    printSkills(abilityScores[i], skillProf[0][i], info.abilities[i] + " ST")
print("Bonds │", end = "")
printlen(bonds, 52)
print("│")


print("│", end = "")
for i in range(3,6):
    printSkills(abilityScores[i], skillProf[0][i], info.abilities[i] + " ST")
print("Flaws │", end = "")
printlen(flaws, 52)
print("│")


print("├───────────────────┼───────────────────┼───────────────────┼──────┴────────────────────────────────────────────────────┤")


for i in range(0,6):
    print("│", end = "")
    for j in range(0,3):
        printSkills(abilityScores[info.skillList[(3*i)+j][1]], skillProf[1][(3*i)+j], info.skillList[(3*i)+j][0])
    printlen(miscInfo[i], 59)
    print("│")


print("├───────────────────┴───────────────────┴───────────────────┴───────────────────────────────────────────────────────────┤")

print("│Features need to go here (or something like that)                                                                      │")

print("└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘")
