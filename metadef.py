menuList = ["Print Character Sheet","Level Up!", "Buy & Sell Equipment", "Save & Quit"]

classList = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]

subclassList = [["Berserker","Totem Warrior"],
                ["Lore","Valor"],
                ["Knowledge","Life","Light","Nature","Tempest","Trickery","War"],
                ["Arctic","Coast","Desert","Forest","Grassland","Mountain","Swamp","Underdark","Moon"],
                ["Champion","Battle Master","Eldritch Knight"],
                ["Open Hand","Shadow","Four Elements"],
                ["Devotion","Ancients","Vengeance"],
                ["Hunter","Beast Master"],
                ["Thief","Assassin","Arcane Trickster"],
                ["Draconic Bloodline","Wild Magic"],
                ["Archfey","Fiend","Great Old One"],
                ["Abjuration","Conjuration","Divination","Evocation","Enchantment","Illusion","Necromancy","Transmutation"]]

## classFeatures[Class][level]
classFeatures = [[["Rage","Unarmoured Defence"],["Reekless Attack","Danger Sense"],["Primal Path"],["ASI"],["Extra Attack","Fast Movement"],["Path Feature: "],["Feral Instinct"],["ASI"],["Brutal Criticals (1)"],["Path Feature: "],["Relentless Rage"],["ASI"],["Brutal Criticals (2)"],["Path Feature: "],["Persistent"],["ASI"],["Brutal Criticals (3)"],["Indomitable Might"],["ASI"],["Primal Champion"]],
                 [["Spellcasting","Bardic Inspiration (d6)"],["Jack of All Trades","Song of Rest (d6)"],["Bardic College","Expertise"],["ASI"],["Bardic Inspiration (d8)","Font of Inspiration"],["Countercharm","Collage Feature: "],[""],["ASI"],["Song of Rest (d8)"],["Bardic Inspiration (d10)","Expertise","Magical Secrets"],[""],["ASI"],["Song of rest (d10)"],["Magical Secrets","College Feature:"],["Bardic Inspiration(d12)"],["ASI"],["Song of Rest"],["Magical Secrets"],["ASI"],["Superior Inspiration"]],
                 [["Spellcasting","Divine Domain"],["Channel Divinity (1/Rest)","Domain Feature:"],[""],["ASI"],["Destroy Undead (CR:½)"],["Channel Divinity (2/Rest)","Domain Feature:"],[""],["ASI","Destroy Undead (CR:1)","Domain Feature: "],[""],["Divine Intervention"],["Destroy Undead (CR:2)"],["ASI"],[""],["Destroy Undead (CR:3)"],[""],["ASI"],["Destroy Undead (CR:4)","Domain Feature"],["Channel Divinity(3/Rest)"],["ASI"],["Improved Divine Intervention"]],
                 [["Spellcasting","Druidic"],["Wild Shape (Walking)","Druid Circle"],[""],["ASI","Wild Shape (Swimming)"],[""],["Circle Feature: "],[""],["Wild Shape (Flying)"],[""],["Circle Feature: "],[""],["ASI"],[""],["Circle Feature: "],[""],["ASI"],[""],["Timeless Body","Beast Spells"],["ASI"],["Archdruid"]],
                 [["Fighting Style","Second Wind"],["Action Surge (1)"],["Martial Archetype"],["ASI"],["Extra Attack"],["ASI"],["Archetype Feature: "],["ASI"],["Indomitable (1)"],["Archetype Feature: "],["Extra Attack (2)"],["ASI"],["Indomitable (2)"],["ASI"],["Archetype Feature: "],["ASI"],["Action Surge (2)","Indomitable (3)"],["Archetype Feature: "],["ASI"],["Extra Attack (3)"]],
                 [["Martial Arts","Unarmoured Defence"],["Ki","Unarmoured Movement"],["Monastic Tradition","Deflect Missiles"],["ASI","Slow Fall"],["Extra Attack","Stunning Strike"],["Ki-Empowered Strikes"],["Evasion","Stillness of Mind"],["ASI"],["Unarmoured Movement Improvement"],["Purity of Body"],["Tradition Feature: "],["ASI"],["Tongue of the Sun and Moon"],["Diamond Soul"],["Timeless Body"],["ASI"],["Tradition Feature: "],["Empty Body"],["ASI"],["Perfect Self"]],
                 [["Divine Sence","Lay on Hands"],["Spellcasting","Fighting Style","Divine Smite"],["Sacred Oath","Divine Health"],["ASI"],["Extra Attack"],["Aura of Protection"],["Oath Feature: "],["ASI"],[""],["Aura of Courage"],["Improved Divine Smite"],["ASI"],[""],["Cleansing Touch"],["Oath Feature: "],["ASI"],[""],["Aura Improvements"],["ASI"],["Oath Feature: "]],
                 [["01Rang"],["02Rang"],["03Rang"],["04Rang"],["05Rang"],["06Rang"],["07Rang"],["08Rang"],["09Rang"],["10Rang"],["11Rang"],["12Rang"],["13Rang"],["14Rang"],["15Rang"],["16Rang"],["17Rang"],["18Rang"],["19Rang"],["20Rang"]],
                 [["Expertise","Sneak Attack", "Thieves' Cant"],["Cunning Action"],["Roguish Archetype"],["ASI"],["Uncanny Dodge"],["Expertise"],["Evasion"],["ASI"],["Archetype Feature: "],["ASI"],["Reliable Talent"],["ASI"],["Archetype Feature: "],["Blindsense"],["Slippery Mind"],["ASI"],["Archetype Feature: "],["Elusive"],["ASI"],["Stroke of Luck"]],
                 [["Spellcasting","Sorcerous Origin"],["Font of Magic"],["Metamagic"],["ASI"],[""],["Origin Feature: "],[""],["ASI"],[""],["Metamagic"],[""],["ASI"],[""],["Origin Feature: "],[""],["ASI"],["Metamagic"],["Origin Feature: "],["ASI"],["Sorcerous Restoration"]],
                 [["Otherworldly Patron", "Pact Magic"],["Eldritch Evocations"],["Pact Boon"],["ASI"],[""],["Patron Feature: "],[""],["ASI"],[""],["Patron Feature: "],["Mystic Arcanum (6th)"],["ASI"],["Mystic Arcanum (7th)"],["Patron Feature: "],["Mystic Arcanum (8th)"],["ASI"],["Mystic Arcanum (9th)"],[""],["ASI"],["Eldritch Master"]],
                 [["Spellcasting","Arcane Recovery"],["Arcane Tradition"],[""],["ASI"],[""],["Tradition Feature: "],[""],["ASI"],[""],["Tradition Feature: "],[""],["ASI"],[""],["Tradition Feature: "],[""],["ASI"],[""],["Spell Mastery"],["ASI"],["Signature Spell"]]]

for printclassname in range(0,len(classList)):
    for printlevel in range(0,20):
        for printfeature in range(0, len(classFeatures[printclassname][printlevel])):
            if classFeatures[printclassname][printlevel][0] is not "":
                if printlevel<9: #this number may need changing if reimplemented
                    print(0, end="")
                print(str(printlevel + 1) + " " + classList[printclassname][:4] + " " + classFeatures[printclassname][printlevel][printfeature])
    print("----------------")
#did a thing here to make the array for me
#print("[", end="")
#for i in range(0,len(classList)):
#    print(",[", end="")
#    for j in range(0,20):
#        if j != 0:
#            print(",", end="")
#        print("[", end="")
#        if j<9:
#            print(0, end="")
#        print(str(j+1) + classList[i][:4] + "]", end="")
#    print("]", end="")
#print("]", end="")


subclassLevel = [3, 3, 1, 2, 3, 3, 3, 3, 3, 1, 1, 2]

raceList = ["Dwarf","Elf","Halfling","Human","Dragonborn","Gnome","Half-Elf","Half-Orc","Tiefling","Aarakocra"]

subraceList = [["Hill","Mountain"],
               ["High","Wood","Drow"],
               ["Lightfoot","Stout"],
               ["", "Var."],
               ["Black","Blue","Brass","Bronze","Copper","Gold","Green","Red","Silver","White",],
               ["Forest","Rock"],
               [""],
               [""],
               [""],
               [""]]

statList = ["Str", "Dex", "Con", "Int", "Wiz", "Cha"]

savingThrowList = [[True, False, True, False, False, False],
                   [False, True, False, False, False, True],
                   [False, False, False, False, True, True],
                   [False, False, False, True, True, False],
                   [True, False, True, False, False, False],
                   [True, True, False, False, False, False],
                   [False, False, False, False, True, True],
                   [True, True, False, False, False, False],
                   [False, True, False, True, False, False],
                   [False, False, True, False, False, True],
                   [False, False, False, False, True, True],
                   [False, False, False, True, True, False]]

## skillname, relatedstat(0-5)
skillList = [["Acrobatics",0],
              ["Animal Handling",4],
              ["Arcana",3],
              ["Athletics",0],
              ["Deception",5],
              ["History",3],
              ["Insight",4],
              ["Intimidation",5],
              ["Investigation",3],
              ["Medicine",4],
              ["Nature",3],
              ["Perception",4],
              ["Perforomance",5],
              ["Persuasion",5],
              ["Religion",3],
              ["Sleight of Hand",1],
              ["Stealth",1],
              ["Survival",4]]

## amount of thing, Weapon/type/ect,
## Wep = Weapon
## WTy = Weapon Type
## Pak = Pack
## Fcs = Focus
## Arm = Armour
## Shd = Shield
## last 2 numbers are reference to where full info is stored eg 1Wep00 is the 0th place in the array

## info on what stuff each class gets at the start
startEquip = [[["1Wep17", "1WTy02"],["2Wep03", "1WTy00"],["1Pak044Wep041Arm13"]],## barb
              [["1Wep25", "1Wep21", "1WTy00"],["1Pak01", "1Pak03"],["1Fcs001Wep011Arm02"]],## bard
              [["1Wep06", "1Wep30"],["1Arm06", "1Arm02", "1Arm10"],["1Wep33", "1WTy00", "1WTy01"],["1Pak04","1Pak05"],["1Fcs011Shd00"]], ## cleric
              [["1Wep26", "1WTy00"],["1WTy00","1Wty01","1Shd00"],["1Arm021Pak041Fcs03"]],## druid
              [["1Arm10", "1Arm021Wep35"],["1Wep33","2Wep03"],["1Pak02","1Pak04"]],## fighter
              [["1Wep27", "1WTy00", "1WTy01"],["1Pak02","1Pak04"],["5Wep115Wep111Arm14"]], ##monk
              [["1WTy021Shd00","1WTy031Shd00", "1WTy021WTy03", "2Wty02", "2WTy03"],["5Wep04","1WTy00"],["1Pak04","1Pak05"],["1Fcs01"],["1Arm10"]], ## Paladin
              [["1Arm06","1Arm02"],["2Wep27","2WTy00"],["1Pak02","1Pak04"],["1Wep35"]], ## ranger UA!
              [["1Wep25", "1Wep27"],["1Wep12","1Wep27"],["1Pak00","1Pak02","1Pak04"],["1Arm022Wep01"]], ## rouge
              [["1Wep33","1WTy00","1WTy01"],["1Pak02", "1Pak04"],["2Wep01"]], ## sorcerer
              [["1Wep33", "1WTy00", "1WTy01"],["1Pak02","1Pak06"],["1WTy00", "1WTy01"],["1Arm02"],["2Wep01"],["1Pak03","1Pak04"]],## warlock
              [["1Wep07","1Wep01"],["1Pak04","1Pak06"],["1Pak03","1Pak04"]]]## wizard

## name, weapontype(melee/range&simple/martial or special), (light,other,versitile,twohanded), damage(#D#), damagetype
weaponType = ["Simple Meelee", "Simple Ranged", "Martial Meelee", "Martial Ranged"]
weaponList = [["Club", 0, 0, "1d4", "Bludgeon"],
            ["Dagger", 0, 0, "1d4", "Piercing"],
         ["Greatclub", 0, 3, "1d8", "Bludgeon"],
           ["Handaxe", 0, 0, "1d6", "Slashing"],
           ["Javelin", 0, 1, "1d6", "Piercing"],
      ["Light Hammer", 0, 0, "1d4", "Bludgeon"],
              ["Mace", 0, 1, "1d6", "Bludgeon"],
      ["Quarterstaff", 0, 2, "1d6", "Bludgeon"],
            ["Sickle", 0, 0, "1d4", "Slashing"],
             ["Spear", 0, 2, "1d6", "Piercing"],
    ["Light Crossbow", 1, 3, "1d8", "Piercing"],
              ["Dart", 1, 1, "1d4", "Piercing"],
          ["Shortbow", 1, 3, "1d6", "Piercing"],
             ["Sling", 1, 1, "1d4", "Bludgeon"],
         ["Battleaxe", 2, 2, "1d8", "Slashing"],
             ["Flail", 2, 1, "1d8", "Bludgeon"],
            ["Glaive", 2, 3, "1d10","Slashing"],
          ["Greataxe", 2, 3, "1d12","Slashing"],
        ["Greatsword", 2, 3, "2d6", "Slashing"],
           ["Halberd", 2, 3, "1d10","Slashing"],
             ["Lance", 2, 1, "1d12","Piercing"],
         ["Longsword", 2, 2, "1d8", "Slashing"],
              ["Maul", 2, 3, "2d6", "Bludgeon"],
       ["Morningstar", 2, 1, "1d8", "Piercing"],
              ["Pike", 2, 3, "1d10","Piercing"],
            ["Rapier", 2, 1, "1d8", "Piercing"],
          ["Scimitar", 2, 0, "1d6", "Slashing"],
        ["Shortsword", 2, 0, "1d6", "Piercing"],
           ["Trident", 2, 2, "1d6", "Piercing"],
          ["War Pick", 2, 1, "1d8", "Piercing"],
         ["Warhammer", 2, 2, "1d8", "Bludgeon"],
              ["Whip", 2, 1, "1d4", "Slashing"],
           ["Blowgun", 3, 1, "1d1", "Piercing"],
     ["Hand Crossbow", 3, 0, "1d6", "Piercing"],
    ["Heavy Crossbow", 3, 3, "1d10","Piercing"],
           ["Longbow", 3, 3, "1d8", "Piercing"],
               ["Net", 3, 1, " 0 "]]

## pack
packList = ["Burgalar's","Diplomat's","Dungeoneer's","Entertainer's","Explorer's","Priest's","Scholar's"]

## music insturment / Arcane focus / component pouch / divine focus
focusList = ["Musical Insturment", "Holy Symbol", "Druidic Focus", "Arcane Focus", "Component Pouch"]
## name, type(unarmoured,UD,Light,Med,Heavy) ((for working out dex bonus)), baseAC, StrRequirement, StelthDisad(Bool), UDBonus, UD allowes shield
armourList = [["Unarmoured", 0, 10, 0, False],
                  ["Padded", 2, 11, 0, True],
                 ["Leather", 2, 11, 0, False],
         ["Studded Leather", 2, 12, 0, False],
                    ["Hide", 3, 12, 0, False],
             ["Chain Shirt", 3, 13, 0, False],
              ["Scail Mail", 3, 14, 0, True],
              ["Brestplate", 3, 14, 0, False],
              ["Half Plate", 3, 15, 0, True],
               ["Ring Mail", 4, 14, 0, True],
              ["Chain Mail", 4, 16, 13, True],
                  ["Splint", 4, 17, 15, True],
                   ["Plate", 4, 18, 15, True],
               ["Barb's UD", 1, 10, 0, False, 2, 1],
               ["Monk's UD", 1, 10, 0, False, 4, 0]]
