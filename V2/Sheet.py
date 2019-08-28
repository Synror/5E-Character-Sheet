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

def printlen(string, length):
    if len(string) > length:
        print(string[:length])
    else:
        print(string, end = "")
        for i in range(0,length-len(string)):
            print(" ", end="")

print("┌───────────────────────────────────────────────────────────┬──────┬────────────────────────────────────────────────────┐")

print("│", end = "")
printlen("[Name]" + ", A " + "[alignment]" + " " "[race]" + " " + "[levelClass]", 59   )
print("│Traits│", end="")
printlen("", 52) ## this is where the traits text will go
print("│")

print("├─────────┬─────────┬─────────┬─────────┬─────────┬─────────┤Ideals│", end = "")
printlen("", 52) ## this is where the ideals text will go
print("│")
