#Module to hold all libraries

def dialogueLibrary(choice):
    dialogue = {
        "welcome" : "\t Welcome to the world of Thea",
        "currentlocation" : "Current Location: ",
        "menu" : "Choose where to go: \n \t 1: Barracks \n \t 2: Training Grounds \n \t 3: Mission",
        "Barracks" : ["1: Equipment", "2: Switch Location"],
        "Training Grounds" : ["1: Shooting Range", "2: Library" ,"3: Dueling Arena", "4: Switch Location"],
        "Mission" : ["1: Next Mission", "2: Switch Location"]
        }
    return dialogue[choice]

#Player always starts in barracks at the start
#
def locationLibrary(choice):
    location = {
        "1" : "Barracks",
        "2" : "Training Grounds",
        "3" : "Mission"
        }
    return location[choice]

