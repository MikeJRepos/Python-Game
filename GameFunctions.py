#Module to hold Game functions

###############
### Imports ###
###############
import Dialogue

###############
## Variables ##
###############

stop = 0
validEntry = 0
characterName = ""
characterClass = ""
strength = ""
intelligence = ""
charisma = ""
dexterity = ""
EXP = "0"
HP = ""
location = "Barracks"

#Function Defs
#Create a new character
def createCharacter():
    #Player Character values
    global characterName, characterClass, strength, intelligence, charisma, dexterity, EXP, HP
    pointSum = 0

    #Pick class and assign base stats
    while(characterClass == ""):
        print("Choose Character Class:\n 1: Soldier \n 2: Smuggler \n 3: Technician \n")
        if input() == "1":
            characterClass = "Soldier"
            strength = "4"
            intelligence = "1"
            charisma = "3"
            dexterity = "2"
            HP = "4"
        elif input == "2":
            characterClass = "Smuggler"
            strength = "2"
            intelligence = "3"
            charisma = "4"
            dexterity = "1"
            HP = "4"
        elif input == "3":
            characterClass = "Technician"
            strength = "2"
            intelligence = "4"
            charisma = "1"
            dexterity = "3"
            HP = "4"
        else:
            print("Select a valid option")
    
    while (characterName == ""):
        print("Enter Character Name")
        characterName = input()
        if len(characterName) == 0 or len(characterName) > 10:
            print("Character Name is empty or greater than 10 characters")
            characterName = ""
            continue
        
    while (pointSum != 5):
        #User distributes skill points
        print("Distribute your 5 points")
        #Set Strength
        print("Strength: ")
        strength = input()
        if strength == "" or strength == "0":
            print("Invalid value entered")
            pointSum = 0
            continue
        pointSum += int(strength)

        #Set Intelligence
        print("Intelligence: ")
        intelligence = input()
        if intelligence == "" or intelligence == "0":
            print("Invalid value entered")
            continue
            pointSum = 0
        pointSum += int(intelligence)

        #Set Charisma
        print("Charisma: ")
        charisma = input()
        if charisma == "" or charisma == "0":
            print("Invalid value entered")
            continue
            pointSum = 0
        pointSum += int(charisma)

        #Set Dexterity
        print("Dexterity: ")
        dexterity = input()
        if dexterity == "" or dexterity == "0":
            print("Invalid value entered")
            continue
            pointSum = 0
        pointSum += int(dexterity)

        #Check that points were distributed properly
        if pointSum != 5:
            print("Points not distributed properly")
            pointSum = 0
            continue

    f = open("player", "w")
    f.write(characterName + "\n")
    f.write(characterClass + "\n")
    f.write("Strength: " + strength + "\n")
    f.write("Intelligence: " + intelligence + "\n")
    f.write("Charisma: " + charisma + "\n")
    f.write("Dexterity: " + dexterity + "\n")
    f.write("EXP: " + EXP)
    f.write("HP: " + HP)
    f.close()
    
#Load previously made character
def loadCharacter():
    global characterName, characterClass, strength, intelligence, charisma, dexterity, EXP, HP
    f = open("player", "r")
    characterName = f.readline()
    characterClass = f.readline()
    strength = f.readline()[-2:]
    intelligence = f.readline()[-2:]
    charisma = f.readline()[-2:]
    dexterity = f.readline()[-2:]
    HP = f.readline()[-2:]
    f.close()

#Functions to get and set attributes
def getAttribute(attribute):
    global characterName, characterClass, strength, intelligence, charisma, dexterity, EXP, HP
    if attribute == "name":
        return characterName
    elif attribute == "class":
        return characterClass
    elif attribute == "strength":
        return strength
    elif attribute == "intelligence":
        return intelligence
    elif attribute == "charisma":
        return charisma
    elif attribute == "dexterity":
        return dexterity
    elif attribute == "EXP":
        return EXP
    else:
        return " "

def levelUp():
    global characterName, characterClass, strength, intelligence, charisma, dexterity, EXP, HP
    print("Level Up")
    pointsAdded = 0
    while(pointsAdded != 3):
    
        for x in range(3):
            print(x)
            print("Choose where to put a point: \n"
                  "1: Strength \n"
                  "2: Intelligence \n"
                  "3: Charisma \n"
                  "4: Dexterity \n")
            choice = input()
            if choice == "1":
                strength = str(int(strength) + 1)
                pointsAdded += 1
            elif choice == "2":
                intelligence = str(int(intelligence) + 1)
                pointsAdded += 1
            elif choice == "3":
                charisma = str(int(charisma) + 1)
                pointsAdded += 1
            elif choice == "4":
                dexterity = str(int(dexterity) + 1)
                pointsAdded += 1
            else:
                print("Invalid Selection")
        choice = ""
        
        if pointsAdded != 3:
            pointsAdded = 0
            print("Points not properly distributed")
        
    f = open("player", "w")
    f.write(characterName + "\n")
    f.write(characterClass + "\n")
    f.write("Strength: " + strength + "\n")
    f.write("Intelligence: " + intelligence + "\n")
    f.write("Charisma: " + charisma + "\n")
    f.write("Dexterity: " + dexterity + "\n")
    f.write("EXP: " + EXP)
    f.close()
  
def splashScreen():
    global validEntry
    print(Dialogue.dialogueLibrary("welcome"));
    while(not validEntry):
        print("\t Enter 1 for new game or 2 to continue")
        start = input()
        if start == "1":
            validEntry = 1
            createCharacter()
        elif start == "2":
            validEntry = 1
            loadCharacter()
        else:
            print("Invalid Entry")

def menu():
    global location
    print(Dialogue.dialogueLibrary("currentlocation") + location + "\n")
    Dialogue.dialogueLibrary(location)
    if location == "Barracks":
        for x in Dialogue.dialogueLibrary("Barracks"):
            print(x + "\n")
    elif location == "Training Grounds":
        for x in Dialogue.dialogueLibrary("Training Grounds"):
            print(x + "\n")
    elif location == "Mission":
        for x in Dialogue.dialogueLibrary("Mission"):
            print(x + "\n")

def chooseLocation():
    global location
    print(Dialogue.dialogueLibrary("menu"))
    choice = input()
    if choice == "1":
        location = Dialogue.locationLibrary("1")
    elif choice == "2":
        location = Dialogue.locationLibrary("2")
    elif choice == "3":
        location = Dialogue.locationLibrary("3")
    else:
        print("Invalid choice")
        choice = ""
    print(Dialogue.dialogueLibrary("currentlocation") + location + "\n")
