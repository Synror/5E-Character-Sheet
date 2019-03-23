## │║─═
## ┌┬┐╒╤╕╓╥╖╔╦╗
## ├┼┤╞╪╡╟╫╢╠╬╣
## └┴┘╙╨╜╘╧╛╚╩╝
## hear me out on this one, i'm gonna make a sperate file for printing the character sheet itself and its gonna be this long ;)
def printSpace(introText, variableText, length):
    length -= 1
    print("│" + introText + variableText, end=""
    )
    for i in range(0,(length-len(introText)-len(variableText))):
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
    FH = open(name+".txt", "r")
    classlist = "6/Sorcerer"
    background = "Merchant"
    ## full length is 121 -1 for the end =120 that divides nicely
    print("┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")

    printSpace("Name: ", name, 40) #120
    printSpace("Class: ", classlist, 80)
    print("│")

    print("├─────────────────────────────┬─────────┴───────────────────┬─────────────────────────────┬─────────────────────────────┤")
    #divider(40,30)

    printSpace("Background: ", background, 30)
    printSpace("","",30)
    printSpace("","",30)
    printSpace("","",30)
    print("│")

printCharSheet("Deekek")
