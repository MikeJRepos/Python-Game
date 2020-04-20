#Module to hold Game functions

###############
### Imports ###
###############
import Dialogue
import random
###############
## Variables ##
###############

stop = 0
validEntry = 0
location = "Barracks"

#Function Defs  
def splashScreen(player):
    print(Dialogue.dialogueLibrary("welcome"));
    while True:
        print("\t Enter 1 for new game or 2 to continue")
        start = input()
        if start == "1":
            validEntry = 1
            while True:
                print("Choose Character Class:\n 1: Soldier \n 2: Smuggler \n 3: Technician \n")
                if input() == "1":
                    player.setClass("Soldier")
                    player.setStrength(4)
                    player.setInt(1)
                    player.setCha(3)
                    player.setDex(2)
                    player.setExp(0)
                    player.setHP(4)
                    player.setWeapon1("Pistol")
                    player.setWeapon2("Sword")
                    player.setArmor("Fatigues")
                    break
                elif input == "2":
                    player.setClass("Smuggler")
                    player.setStrength(2)
                    player.setInt(3)
                    player.setCha(4)
                    player.setDex(1)
                    player.setExp(0)
                    player.setHP(4)
                    player.setWeapon1("Pistol")
                    player.setWeapon2("Sword")
                    player.setArmor("Fatigues")
                    break
                elif input == "3":
                    player.setClass("Technician")
                    player.setStrength(2)
                    player.setInt(4)
                    player.setCha(1)
                    player.setDex(3)
                    player.setExp(0)
                    player.setHP(4)
                    player.setWeapon1("Pistol")
                    player.setWeapon2("Sword")
                    player.setArmor("Fatigues")
                    break
                else:
                    print("Select a valid option")
            
            while True:
                print("Enter Character Name")
                Name = input()
                if len(Name) == 0 or len(Name) > 10:
                    print("Character Name is empty or greater than 10 characters")
                    continue
                else:
                    player.setName(Name)
                    break   
                   
            while (pointSum != 5):
                #User distributes skill points
                print("Distribute your 5 points")
            while(pointsAdded != 5):
                print("Choose where to put a point: \n"
                      "1: Strength \n"
                      "2: Intelligence \n"
                      "3: Charisma \n"
                      "4: Dexterity \n")
            choice = input()
            if choice == "1":
                player.setStrength(player.getStrength() + 1)
                pointsAdded += 1
            elif choice == "2":
                player.setInt(player.getInt() + 1)
                pointsAdded += 1
            elif choice == "3":
                player.setCha(player.getCha() + 1)
                pointsAdded += 1
            elif choice == "4":
                player.setDex(player.getDex() + 1)
                pointsAdded += 1
            else:
                print("Invalid Selection")

            print("Name: " + player.getName())
            print("Class: " + player.getClass())
            print("Strength: %s" % (player.getStrength()))
            print("Intelligence: %s" % (player.getInt()))
            print("Charisma: %s" % (player.getCha()))
            print("Dexterity: %s" % (player.getDex()))
            print("Experience: %s" % (player.getExp()))
            print("HP: %s" % (player.getHP()))
            print("Weapon1: " % (player.getW1()))
            print("Weapon2: " % (player.getW2()))
            print("Armor: " % (player.getArmor()))

            #End character creation
            player.save()
            return 0 
            
        elif start == "2":
            validEntry = 1
            f = open("player", "r")
            player.setName(f.readline())
            player.setClass(f.readline())
            player.setStrength(int(f.readline()[-2:]))
            player.setInt(int(f.readline()[-2:]))
            player.setCha(int(f.readline()[-2:]))
            player.setDex(int(f.readline()[-2:]))
            player.setExp(int(f.readline()[-2:]))
            player.setHP(int(f.readline()[-2:]))
            player.setWeapon1(f.readline())
            player.setWaepon2(f.readline())
            player.setArmor(f.readline())
            f.close()

            print("Name: " + player.getName())
            print("Class: " + player.getClass())
            print("Strength: %s" % (player.getStrength()))
            print("Intelligence: %s" % (player.getInt()))
            print("Charisma: %s" % (player.getCha()))
            print("Dexterity: %s" % (player.getDex()))
            print("Experience: %s" % (player.getExp()))
            print("HP: %s" % (player.getHP()))
            print("Weapon1: " % (player.getW1()))
            print("Weapon2: " % (player.getW2()))
            print("Armor: " % (player.getArmor()))
            return 0
            
        else:
            print("Invalid Entry")

def levelUp(player):
    print("Level Up!")
    pointsAdded = 0
    while(pointsAdded != 3):
        print("Choose where to put a point: \n"
              "1: Strength \n"
              "2: Intelligence \n"
              "3: Charisma \n"
              "4: Dexterity \n")
        choice = input()
        if choice == "1":
            player.setStrength(player.getStrength() + 1)
            pointsAdded += 1
        elif choice == "2":
            player.setInt(player.getInt() + 1)
            pointsAdded += 1
        elif choice == "3":
            player.setCha(player.getCha() + 1)
            pointsAdded += 1
        elif choice == "4":
            player.setDex(player.getDex() + 1)
            pointsAdded += 1
        else:
            print("Invalid Selection")

    #Add between 1-4 more points of HP
    newHP = random.randint(1,4)
    player.setHP(player.getHP() + newHP)
    print(str(newHP) + " points of HP added!\n")
    player.save()
        
    
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
