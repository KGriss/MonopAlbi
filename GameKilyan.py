from random import *

class Game :
    def __init__(self):
        pass
    
    def rollDice(self):
        diceValue = randint(1,6)
        return diceValue
    
    def getChanceCard(self):
        return 2
