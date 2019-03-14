## file for defining all of the things!!
print("testing")
import metadef as MD

## defining a process that lists items
## and returns int that user has inputted,
def ListAndSelect(text, metaRef):
    print("Choose a " + text)
    for i in range(0,len(metaRef)):
        if i < 10:
            print("0", end="")
        print(str(i) + " " + metaRef[i])
    output = int(input(""))
    return output

def CodeToText(code, ref):
    if code == "Wep":
        print(MD.weaponList[ref][0])
    elif code == "WTy":
        print(MD.weaponType[ref])
    else:
        print(MD.startEquip[startingClass][choices][items])

## name
## classlevel
## subclass
## race
## subrace
## background
## alignment
## ability scores (without any other bonuses)
## starting equipment (Class)

## HP Roles (only input on level up)

## (calculatable things)
## prof bonus (Combined Level)
## saving throws (Starting Class)
## passive perception
## armour class (Armour & Shield)
## speed (Race & Charger Feat)
## features and traits (Class Levels)
## ------------------------------------------------------

## name
print("D&D 5e Character Sheet Tracker")
name = input("Name a Character to Load:\n")
try:
    FH = open(name+".txt", "r")
    FH.close()
except FileNotFoundError:
    print("That PC was not found,\nCreating New\n")
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

## ability scores (without any other bonuses)
## starting equipment (Class)

    for choices in range(0,len(MD.startEquip[startingClass])):                                  ## for each choice of equipment
        if len(MD.startEquip[startingClass][choices]) != 1:                                     ## if there is actually a choice intead of the item being given to you
            for items in range(0,len(MD.startEquip[startingClass][choices])):                       ## for every item that you can choose from list:
                print(str(items) + " ", end="")                                                         ## index for selection
                print(MD.startEquip[startingClass][choices][items][0], end="*")                         ## ammount of the item (eg 2 handaxes)
                CodeToText(MD.startEquip[startingClass][choices][items][1:4],int(MD.startEquip[startingClass][choices][items][4:])) ## and the actual text
            chosenItem = int(input("Select an Item: "))                                             ## and ask for a selection after everthing is listed
                                                                                            ## to be appeneded / inputted to the right place (TBA)
        else:
            print("")

print("------------------")
print(name)
print("The " + MD.raceList[race], end = "")
for i in range(0,len(classLevel)):
    if classLevel[i] != 0:
        print(" " + str(classLevel[i]) + "" + MD.classList[i])
