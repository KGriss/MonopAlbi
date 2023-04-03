class Player():
    SQUARE_PER_LINE = 9
    
    def __init__(self, idPlayer, color, money, isYounth):
        self.idPlayer = idPlayer
        self.color = color
        self.money = money
        #self.isYounth = isYounth

        self.image = None
        self.progress = 0
        self.square = 0
        self.isJailed = False

    def forward(self, value):
        pass       
    
    def gotoSquare(self, square):
        pass
    
    def addMoney(self, value):
        self.money += value
