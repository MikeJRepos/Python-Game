#RPG Character Class structure
class Character:
    """Character object built from save file or when created"""

    def __init__(self):
        self.characterName  = ""
        self.characterClass = ""
        self.strength = 0
        self.intelligence = 0
        self.charisma = 0
        self.EXP = 0
        self.HP = 0
        self.W1 = ""
        self.W2 = ""
        self.armor = ""
        self.location = "Barracks"

    #Functions to get and set attributes
    def getName(self):
        return self.characterName

    def getClass(self):
        return self.characterClass

    def getStrength(self):
        return self.strength

    def getInt(self):
        return self.intelligence

    def getCha(self):
        return self.charisma

    def getDex(self):
        return self.dexterity

    def getExp(self):
        return self.EXP

    def getHP(self):
        return self.HP

    def getHP(self):
        return self.HP

    def getWeapon1(self):
        return self.W1

    def getWeapon2(self):
        return self.W2

    def getArmor(self):
        return self.armor

    def getLocation(self):
        return self.location
        
    def setName(self, NAME):
        self.characterName = NAME

    def setClass(self, CLASS):
        self.characterClass = CLASS

    def setStrength(self, STR):
        self.strength = STR

    def setInt(self, INT):
        self.intelligence = INT

    def setCha(self, CHAR):
        self.charisma = CHAR

    def setDex(self, DEX):
        self.dexterity = DEX

    def setExp(self, exp):
        self.EXP = exp

    def setHP(self, hp):
        self.HP = hp

    def setWeapon1(self, w1):
        self.W1 = w1

    def setWeapon2(self, w2):
        self.W2 = w2

    def setArmor(self, arm):
        self.armor = arm

    def setLocation(self, loc):
        self.location = loc

    def save(self):
        f = open("player", "w")
        f.write(self.characterName + "\n")
        f.write(self.characterClass + "\n")
        f.write("Strength: %s\n" % (self.strength))
        f.write("Intelligence: %s\n" % (self.intelligence))
        f.write("Charisma: %s\n" % (self.charisma))
        f.write("Dexterity: %s\n" % (self.dexterity))
        f.write("EXP: %s\n" % (self.EXP))
        f.write("HP: %s\n" % (self.HP))
        f.write(self.W1 + "\n")
        f.write(self.W2 + "\n")
        f.write(self.armor + "\n")
        f.write(self.location)
        f.close()
        
