abilities = ["Strength","Dexterity","Constitution","Inteligence","Wizdom","Charisma"]

jobs = ["Barb", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rouge", "Sorcerer", "Warlock", "Wizard"]

savingThrowList = [[1, 0, 1, 0, 0, 0],
                   [0, 1, 0, 0, 0, 1],
                   [0, 0, 0, 0, 1, 1],
                   [0, 0, 0, 1, 1, 0],
                   [1, 0, 1, 0, 0, 0],
                   [1, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 1],
                   [1, 1, 0, 0, 0, 0],
                   [0, 1, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 1],
                   [0, 0, 0, 0, 1, 1],
                   [0, 0, 0, 1, 1, 0]]

skillList = [["Acrobatics",1],
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
