## file for defining all of the things!!
import metadef as MD
import json
from PrintCharSheet import charSheetPrint

## defining a process that lists items
## and returns int that user has inputted,
def ListAndSelect(text, metaRef, CTT = 0):
    print("│  │")                                ## whitespace
    if text is not "":                           ## if there is a title
        print("│  │Choose a " + text)
    for i in range(0,len(metaRef)):              ## for all of the options in the list
        print("│", end="")                       ## print the number and |
        if i < 10:
            print("0", end="")
        print(str(i) + "│", end="")

        if CTT is 1:
            CodeToText(metaRef[i])
        else:
            print(metaRef[i])

    output = int(input("│>>│"))
    return output

def CodeToText(CodeIn):
    for i in range(0, int(len(CodeIn)/6)):
        if i+1 == int(len(CodeIn)/6) and i != 0:
            print(" and ", end="")
        elif i > 0:
            print(", ", end="")
        offset = i*6
        code = CodeIn[1+offset:4+offset]
        ref = int(CodeIn[4+offset:6+offset])
        if code == "Wep":
            print(CodeIn[0+offset], end="*")                         ## ammount of the item (eg 2 handaxes)
            print(MD.weaponList[ref][0], end="")
        elif code == "WTy":
            print(MD.weaponType[ref], end="")
        elif code == "Arm":
            print(MD.armourList[ref][0], end="")
        elif code == "Pak":
            print(MD.packList[ref] + " Pack", end="")
        elif code == "Shd":
            print("Shield", end="")
        else:
            print(MD.startEquip[startingClass][choice], end="")
    print("")
def CodeAppend(CodeIn):
    for j in range(0,int(len(CodeIn)/6)):
        offset = j*6
        amount = int(CodeIn[0+offset])
        code = CodeIn[1+offset:4+offset]
        ref = int(CodeIn[4+offset:6+offset])
        if code == "Wep":
            added = False
            for i in range(0,len(weapons)): ## check for duplicate weapons, say "2 Longsword" instead of "Longsword and Longsword"
                if weapons[i][1] == ref: ## if the weapon is already in inventory
                    weapons[i][0] += amount
                    added = True
            if not added: ## if there isn't already a weapon of this type in your inventory
                weapons.append([amount,ref]) ## add it
        if code == "Arm": ## don't get multiple armour so this flys :)
            global armour
            armour = ref
        if code == "Shd":
            global shield
            shield = 1

def SaveAndQuit():
    ## classlevel
    FH.write(str(classLevel) + "\n")
    ## subclass
    FH.writelines(str(subclass) + "\n")
    FH.writelines(str(startingClass) + "\n")
    ## race
    FH.writelines(str(race) + "\n")
    ## subrace
    FH.writelines(str(subrace) + "\n")
    ## background
    ## alignment
    ## ability scores (without any other bonuses)
    FH.writelines(str(abilityScores) + "\n")
    ## starting equipment (Class)
    FH.writelines(str(weapons) + "\n")
    FH.writelines(str(armour) + "\n")
    FH.writelines(str(shield) + "\n")

print("┌──┐")
print("│  │D&D 5e Character Sheet Tracker")
print("│  │Character Name")
name = input("│>>│")
try:
    FH = open(name+".txt", "r")
    classLevel = json.loads(FH.readline())
    subclass = json.loads(FH.readline())
    startingClass = int(FH.readline())
    race = int(FH.readline())
    subrace = int(FH.readline())
    abilityScores = json.loads(FH.readline())
    weapons = json.loads(FH.readline())
    armour = int(FH.readline())
    shield = int(FH.readline())
    FH.close()

except FileNotFoundError:
    print("│  │That PC was not found,\n│  │Creating New")
## classlevel
    ## defining the empty arrays to put data into
    classLevel = [0]*len(MD.classList)
    subclass = [0]*len(MD.classList)
    ## getting a starting class & putting it @ lvl 1
    startingClass = ListAndSelect("Class", MD.classList)
    classLevel[startingClass] = 1
## subclass
    ## if you get a subclass at level one
    if MD.subclassLevel[startingClass] == 1:
        ## for the start class selected, Get a Subclass
        subclass[startingClass] = ListAndSelect("Subclass", MD.subclassList[startingClass])
## race
    race = ListAndSelect("Race", MD.raceList)
## subrace
    if len(MD.subraceList[race]) > 1:
        subrace = ListAndSelect("Subrace", MD.subraceList[race])
    else:
        subrace = 0

## background
## alignment
    abilityScores = [0,0,0,0,0,0]
    print("│  │Ability Scores (H3/4d6)")
    for i in range(0,6):
        print("│  │" + MD.statList[i] + ": ")
        abilityScores[i] = int(input("│>>│"))

## ability scores (without any other bonuses)
## starting equipment (Class)
    weapons = []
    armour = 0
    shield = 0

    for choice in range(0, len(MD.startEquip[startingClass])):                  ## for every choice you get
        if len(MD.startEquip[startingClass][choice]) != 1:                      ## if the item isn't just given to you
            chosen = ListAndSelect("", MD.startEquip[startingClass][choice], 1) ## ask what choice they want

        else:                                                                   ## if it is just given to you
            chosen = 0                                                          ## add it automatically
            print("you also get other things (THIS BIT TBA)")
        CodeAppend(MD.startEquip[startingClass][choice][chosen])

go = True
while go: ## the main loop
    menu = ListAndSelect("Menu Option", MD.menuList)
    if menu == 0:
        charSheetPrint(name, classLevel, subclass, startingClass, race, subrace, abilityScores, weapons, armour, shield)
    if menu == 3:
        FH = open(name+".txt", "w")
        SaveAndQuit()
        FH.close()
        go = False
print("└──┘")
