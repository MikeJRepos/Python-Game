#Main code for the game loop
#RPG type game, similar to D&D but set in the world of Thea during the Machina wars

###############
### Imports ###
###############
#import Dialogue
import GameFunctions

###############
## Variables ##
###############
gameOver = 0

#Initialize game parameters
GameFunctions.splashScreen()
print("Name: " + GameFunctions.getAttribute("name") + " Class: " + GameFunctions.getAttribute("class") + " Strength: "
      + GameFunctions.getAttribute("strength") + " Intelligence: " + GameFunctions.getAttribute("intelligence") + " Charisma: "
      + GameFunctions.getAttribute("charisma") + " Dexterity: " + GameFunctions.getAttribute("dexterity"))
            
while(not gameOver):
    #Main game loop code
    GameFunctions.menu()

    print("Continue?: y or n")
    cont = input()
    if cont == "y":
        continue
    elif cont == "n":
        gameOver = 1
    else:
        print("Invalid Choice")
        
    
exit()
