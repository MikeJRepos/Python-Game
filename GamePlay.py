#Main code for the game loop
#RPG type game, similar to D&D but set in the world of Thea during the Machina wars

###############
### Imports ###
###############
#import Dialogue
import GameFunctions
import CharacterClass

###############
## Variables ##
###############
gameOver = 0
player   = CharacterClass.Character()

#Initialize game parameters
GameFunctions.splashScreen(player)
         
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
