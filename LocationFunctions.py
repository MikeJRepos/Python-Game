#Functions associated with each location
import GameLibraries
import random

#Change Location
def chooseLocation(player): 
    print(GameLibraries.dialogueLibrary("menu"))
    choice = input()
    if choice == "1":
        player.setLocation(GameLibraries.locationLibrary("1"))
    elif choice == "2":
        player.setLocation(GameLibraries.locationLibrary("2"))
    elif choice == "3":
        player.setLocation(GameLibraries.locationLibrary("3"))
    else:
        print("Invalid choice")
        choice = ""
    print(GameLibraries.dialogueLibrary("currentlocation") + player.getLocation() + "\n")

#Library
def library(player):
    print("What skill do you want to improve?")
    while(True):
        for x in GameLibraries.dialogueLibrary("Library"):
            print(x + "\n")
        choice = input()
        if choice == "1":
            stat = player.getStrength()
            break
        elif choice == "2":
            stat = player.getInt()
            break
        elif choice == "3":
            stat = player.getCha()
            break
        elif choice == "4":
            stat = player.getDex()
            break
        else:
            print("Invalid Choice")

    #determine if skill is increased
    if stat > 20:
        print("Stat is greater than 20, you cannot increase it any further by studying")
        return
    elif stat > 15:
        #calculate here
    elif stat > 10:
        #calculate here
    elif stat > 5:
        #calculte here
    else:
        #calculate here

    if success:
        print("Successfully improved skill!")
        if choice == "1":
            player.setStrength(stat+1)
            return
        elif choice == "2":
            player.setInt(stat+1)
            return
        elif choice == "3":
            player.setCha(stat+1)
            return
        elif choice == "4":
            player.setDex(stat+1)
            return
    
#Arena
def arena(player):
    while(True):
        for x in GameLibraries.dialogueLibrary("Arena"):
            print(x + "\n")
        choice = input()
        if choice == "1":
            GameLibraries.enemyLibrary("choose")
            break
        elif choice == "2":
            GameLibraries.enemyLibrary("random")
            break
        elif choice == "3":
            print("Do Something")
        else:
            print("Invalid Choice")

    #Begin Combat
        

    
    
#Armory

#Missions
