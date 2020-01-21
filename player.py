

class Player:
    def __init__(self):
        self.hand = []


    def addCard(self, card):
        self.hand.append(card)
        
    def useCard(self, card):
        self.hand.remove(card)

    def __len__(self):
        return len(self.hand)