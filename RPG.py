#Simple RPG/Pokemon type game

###############
## Variables ##
###############

WIDTH = 800
HEIGHT = 800 #Window size
player_x = 600
player_y = 350

BLACK = (0, 0, 0)
BLUE = (0, 155, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (128, 0, 0)

def draw():
    screen.blit(pixil-frame-0,(0,0))

def game_loop():
    #enter stuff
    global player_x, player_y
    if keyboard.right:
        player_x += 5
    elif keyboard.left:
        player_x -= 5
    elif keyboard.up:
        player_y -= 5
    elif keyboard.down:
        player_y += 5
    

clock.schedule_interval(game_loop, 0.03)



