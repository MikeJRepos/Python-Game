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
            
while(not gameOver):
    #Main game loop code
    GameFunctions.splashScreen()
    print("Name: " + GameFunctions.getAttribute("name") + " Class: " + GameFunctions.getAttribute("class") + " Strength: "
          + GameFunctions.getAttribute("strength") + " Intelligence: " + GameFunctions.getAttribute("intelligence") + " Charisma: "
          + GameFunctions.getAttribute("charisma") + " Dexterity: " + GameFunctions.getAttribute("dexterity"))

    GameFunctions.levelUp()

    print("Name: " + GameFunctions.getAttribute("name") + " Class: " + GameFunctions.getAttribute("class") + " Strength: "
          + GameFunctions.getAttribute("strength") + " Intelligence: " + GameFunctions.getAttribute("intelligence") + " Charisma: "
          + GameFunctions.getAttribute("charisma") + " Dexterity: " + GameFunctions.getAttribute("dexterity"))
    
    exit()
