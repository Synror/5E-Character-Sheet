## │║─═
## ┌┬┐╒╤╕╓╥╖╔╦╗
## ├┼┤╞╪╡╟╫╢╠╬╣
## └┴┘╙╨╜╘╧╛╚╩╝
## hear me out on this one, i'm gonna make a sperate file for printing the character sheet itself and its gonna be this long ;)
import math
import metadef as MD

def printSpace(text, length):
    length -= 1
    print("│" + text, end=""
    )
    for i in range(0,(length-len(text))):
        print(" ", end="")

def divider(topSpace, botSpace):
    print("│")
    print("├", end="")
    for i in range(1,120):
        if(i%botSpace == 0 and i%topSpace == 0):
            print("┼", end="")
        elif(i%botSpace == 0):
            print("┬", end="")
        elif(i%topSpace == 0):
            print("┴", end="")
        else:
            print("─", end="")
    print("┤")

def charSheetPrint(name, classLevel, subClass, startingClass, race, subrace, abilityScores, weapons, armour):

    ## some calculatables: inc total char level, spellcasting level? &  proficency bonus
    charLevel = 0
    for i in range(0,len(classLevel)):
        charLevel += classLevel[i]
    prof = math.floor((charLevel-1)/4)+2

    ## full length is 121 -1 for the end =120 that divides nicely
    print("┌───────────────────────────────────────┬───────────────────────────────────────┬───────────────────────────────────────┐")

    classText = ""
    for i in range(0,len(MD.classList)):
        if i == startingClass:
            classText = str(classLevel[i]) + "/" + MD.classList[i] + classText
        elif classLevel[i] < 0:
            classText = classText + str(classLevel[i]) + "/" + MD.classList[i]

    printSpace("Name: " + str(name), 40) # adds up to 120
    printSpace("Race: " + str(MD.raceList[race]), 40)
    printSpace("Background: N/A", 40)

    divider(40, 120)

    printSpace("Level/Class: " + str(classText), 120)

    divider(120,20)

    for i in range(0,len(abilityScores)):
        abilityPrint = MD.statList[i] + ": " ## Str: Dex: Con: Int: Wiz: Cha:
        if abilityScores[i] < 10:
            abilityPrint = abilityPrint + "0" ## add a zero if the score is 9 or below
        abilityPrint = abilityPrint + str(abilityScores[i]) ## add the actual score
        ## base mod calculate
        baseMod = math.floor(abilityScores[i]/2)-5
        abilityPrint = abilityPrint + " " ## whitespace
        if baseMod > -1:
            abilityPrint = abilityPrint + "+"
        abilityPrint = abilityPrint + str(baseMod) ## the actual modifier

        if MD.savingThrowList[startingClass][i]: ## if there's a bonus to saving throw
            savethrowMod = baseMod + prof
            abilityPrint = abilityPrint + " ("
            if savethrowMod > -1:
                abilityPrint = abilityPrint + "+"

            abilityPrint = abilityPrint + str(savethrowMod)
            abilityPrint = abilityPrint + ")"

        printSpace(abilityPrint, 20)

    divider(20,20)

    for i in range(0,len(MD.skillList)):
        if i % 6 == 0 and i != 0:
            print("│")

        ## MD.skillList[1] gives number for which mod to use
        ## then we just use the floor(score/2)-5
        skillMod = math.floor(abilityScores[MD.skillList[i][1]]/2)-5
        ## positive or negative, convert to string
        if skillMod > 0:
            skillMod = "+" + str(skillMod)
        else:
            skillMod = str(skillMod)
        ## and print!
        printSpace(MD.skillList[i][0], 16)
        printSpace(skillMod, 4)

    divider(20,120)

    ## print("└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘")
