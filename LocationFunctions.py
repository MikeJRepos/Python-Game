
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

#Arena

#Armory

#Missions
