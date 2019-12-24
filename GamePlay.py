#Main code for the game loop
#RPG type game, similar to D&D

#Game layout: Splash text
#             Continue or start new?
#               Classes: Soldier, technician, smuggler
#             Load or create character
#             Go through game loop

###############
## Variables ##
###############

gameOver = 0
stop = 0

#Function Defs
def createCharacter():
    #Player Character values
    characterName = ""
    characterClass = ""
    strength = ""
    intelligence = ""
    charisma = ""
    dexterity = ""
    wisdom = ""
    pointSum = 0
    
    print("Code to create a character to go here")
    print("Enter Character Name")
    charaterName = input()
    print("Choose Character Class: 1: 2: 3: ")
    characterClass = input()

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
        

def loadCharacter():
    print("Code to load character goes here")

#Splash text
print("Welcome to the world of Thea");
print("Enter 1 for new game or 2 to continue")
start = input()

if start == "1":
    createCharacter()
elif start == "2":
    loadCharacter()
else:
    print("Invalid entry")
        




#while(gameOver):
    #Run game until game over or player quits
