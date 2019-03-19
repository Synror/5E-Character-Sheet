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


name = "Deekek"
classlist = "6/Sorcerer"
background = "Merchant"
## full length is 120
print("┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")

printSpace("Name: ", name, 120) #120
print("│")

printSpace("Class: ", classlist, 60)
printSpace("","",60)
print("│")

printSpace("Background: ", background, 40)
printSpace("","",40)
printSpace("","",40)
print("│")
