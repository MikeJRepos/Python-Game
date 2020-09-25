#Module to hold all libraries
import random

def dialogueLibrary(choice):
    dialogue = {
        "welcome" : "\t Welcome to the world of Thea",
        "currentlocation" : "Current Location: ",
        "menu" : "Choose where to go: \n \t 1: Barracks \n \t 2: Training Grounds \n \t 3: Mission",
        "Barracks" : ["1: Equipment", "2: Switch Location"],
        "Training Grounds" : ["1: Library" ,"2: Arena", "3: Switch Location"],
        "Mission" : ["1: Next Mission", "2: Switch Location"],
        "Arena" : ["1: Choose Opponent", "2: Random Opponent", "3: Exit"],
        "Library" : ["1: Strength", "2: Intelligence", "3: Charisma", "4: Dexterity"]
        }
    return dialogue[choice]

#Player always starts in barracks at the start
def locationLibrary(choice):
    location = {
        "1" : "Barracks",
        "2" : "Training Grounds",
        "3" : "Mission"
        }
    return location[choice]

#Enemy Library, enemy name : [STR, INT, CHAR, DEX, HP, W1, W2, ARM, EXP] 
def enemyLibrary(playerChoice):
    enemies = {
        "rat" : [1, 1, 1, 1, 1, 1, 1, 1, 1]
        }
    if playerChoice == "choose":
        while(True):
            for x in enemies:
                print(x)
            print("Choose Enemy: ")
            choice = input().lower()
            if choice in enemies:
                return enemies[enemy]
            else:
                print("Invalid Option")
    elif playerChoice == "random":
        enemy = random.choice(list(enemies.keys()))
        print(enemy)
        return enemy
    else:
        print("Invalid Option")
        return

#Weapons Libraries, weapon name : []
def weaponLibrary(weapon):
    weapons = {
        "pistol" : []
        }
    return weapon(weapon)
