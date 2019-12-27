#Main code for the game loop
#RPG type game, similar to D&D but set in teh world of Thea during the Machina wars

################
### Includes ###
################
#include "GameModules.h"

###############
## Variables ##
###############

gameOver = 0
stop = 0
validEntry = 0
characterName = ""
characterClass = ""
strength = ""
intelligence = ""
charisma = ""
dexterity = ""
wisdom = ""

#Function Defs
def createCharacter():
    #Player Character values
    global characterName, characterClass, strength, intelligence, charisma, dexterity, wisdom
    pointSum = 0

    print("Choose Character Class: 1: 2: 3: ")
    characterClass = input()
    
    while (characterName == ""):
        print("Enter Character Name")
        characterName = input()
        if len(characterName) == 0 or len(characterName) > 10:
            print("Character Name is empty or greater than 10 characters")
            characterName = ""
            continue
        
    while (pointSum !=5):
        #User distributes skill points
        print("Distribute your 5 points")
        #Set strength
        print("Strength: ")
        strength = input()
        if strength == "" or strength == "0":
            print("Invalid value entered")
            pointSum = 0
            continue
        pointSum += int(strength)

        #Set intelligence
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

        #Set wisdom
        print("Wisdom: ")
        wisdom = input()
        if wisdom == "" or wisdom == "0":
            print("Invalid value entered")
            continue
            pointSum = 0
        pointSum += int(wisdom)

        if pointSum != 5:
            print("Points not distributed properly")
            pointSum = 0
            continue

    f = open("player", "w")
    f.write(characterName + "\n")
    f.write("Strength: " + strength + "\n")
    f.write("Intelligence: " + intelligence + "\n")
    f.write("Charisma: " + charisma + "\n")
    f.write("Dexterity: " + dexterity + "\n")
    f.write("Wisdom: " + wisdom)
    #f.close()
    

def loadCharacter():
    print("Code to load character goes here")
    global characterName, characterClass, strength, intelligence, charisma, dexterity, wisdom
    
def splashScreen():
    global validEntry
    print("\t Welcome to the world of Thea");
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
            
while(not gameOver):
    #Main game loop code
    splashScreen()
    exit()
