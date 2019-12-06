#Simple RPG type game

###############
## Variables ##
###############

WIDTH = 800
Height = 450 #Window size
ScreenState = 0

BLACK = (0, 0, 0)
BLUE = (0, 155, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (128, 0, 0)

def draw():
    if ScreenState == 0:
        screen.blit(images.splashscreen,(0,75))
    elif ScreenState == 1:
        screen.blit(images.mainscreen,(0,75))

def on_mouse_down(pos):
    global ScreenState
    if pos[0] < 800 and pos[0] > 0 and pos[1] < 450 and pos[1] > 0:
        ScreenState = 1

def game_loop():
    #enter stuff
    global ScreenState

clock.schedule_interval(game_loop, 0.03)



