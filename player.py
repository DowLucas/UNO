

class Player:
    def __init__(self):
        self.hand = []


    def addCard(self, card):
        self.hand.append(card)

    @property
    def num_cards(self):
        return len(self.hand)