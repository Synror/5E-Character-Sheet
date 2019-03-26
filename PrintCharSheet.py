## │║─═
## ┌┬┐╒╤╕╓╥╖╔╦╗
## ├┼┤╞╪╡╟╫╢╠╬╣
## └┴┘╙╨╜╘╧╛╚╩╝
## hear me out on this one, i'm gonna make a sperate file for printing the character sheet itself and its gonna be this long ;)
import math

## format number
def FormNum(inNumber):
    if inNumber > -1:
        return "+" + str(inNumber)
    else:
        return str(inNumber)

def printSpace(text, length):
    length -= 1
    print("│" + text, end=""
    )
    for i in range(0,(length-len(text))):
        print(" ", end="")

def printSideBySide(printListA, printListB, fullLength):
    if len(printListA) == len(printListB): ## check that they are the same length
        for i in range(printListA): ## for each line needed
            for j in range(0,1): ## for each printList (1/2 a line)
                if j == 0:
                    printSpace(printListA[i], fullLength/2) ## print first half
                else:
                    printSpace(printListB[i], fullLength/2) ## or seccond half

def divider(topSpace, botSpace):
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

def printCharSheet(name):

    ##  get from FH or pass into Function?
    classlist = "6/Sorcerer"
    race = "Aarakocra"
    background = "Merchant"
    abilityScores = [6, 13, 14, 13, 12, 16]
    savingThrows = [False, False, True, False, False, True]
    Prof = 3

    ## full length is 121 -1 for the end =120 that divides nicely
    print("┌───────────────────────────────────────┬───────────────────────────────────────────────────────────────────────────────┐")

    printSpace("Name: " + str(name), 40) #120
    printSpace("Level/Class: " + str(classlist), 80)
    print("│")

    print("├─────────────────────────────┬─────────┴───────────────────┬─────────────────────────────┬─────────────────────────────┤")
    #divider(40,30)

    printSpace("Race: "+ str(race), 30)
    printSpace("Background: " + str(background), 30)
    printSpace("", 30)
    printSpace("", 30)
    print("│")

    divider(30, 40)

    ## i'm gonna store all of the stuff in this array
    ## so that there are 3 coloums that work nicely together
    toPrint = [[],[],[]]

    toPrint[0].append("Ability Scores, Mods and Saves")
    scoreNames = ["Str", "Dex","Con","Int","Wiz","Cha"]
    for i in range(0, len(scoreNames)):
        Score = abilityScores[i]
        if Score < 10:
            Score = "0" + str(Score)
        else:
            Score = str(Score)
        Mod = int(abilityScores[i]/2)-5
        Save = Mod
        if savingThrows[i]:
            Save = Save + Prof

        toPrint[0].append(scoreNames[i] + ":    " + str(Score) + "      " + FormNum(Mod) + "       " + FormNum(Save))


    ## and now we print everything that was appended to toPrint !!
    for row in range(0,15):
        for col in range(0,3):
            try:
                printSpace(toPrint[col][row], 40)
            except IndexError:
                printSpace("",40)
        print("│")

    print("└───────────────────────────────────────┴───────────────────────────────────────┴───────────────────────────────────────┘")
printCharSheet("Deekek")
## └┴┘╙╨╜╘╧╛╚╩╝
