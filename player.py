

class Player:
    def __init__(self):
        self.hand = []


    def addCard(self, card):
        self.hand.append(card)
        
    def useCard(self, card):
        self.hand.remove(card)

    def hasWon(self):
        return True if len(self) == 0 else False



    def __len__(self):
        return len(self.hand)