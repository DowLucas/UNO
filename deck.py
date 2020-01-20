from card import Card
import random

class Deck:

    def __init__(self):
        self.colors = ["red", "blue", "yellow", "green"]
        self.special_cards = {"skip": 2, "draw_two": 2, "reverse": 2}
        self.deck = self._makeNewDeck()
        random.shuffle(self.deck)


    def _makeNewDeck(self):
        colorsAndNumbers = [Card(value, color) for color in self.colors for value in range(1, 10) for _ in range(2)]
        for c in self.colors:
            colorsAndNumbers.append(Card(0, c))

        colorsAndSpecialCards = []
        for c in self.colors:
            for sp, num in self.special_cards.items():
                for i in range(1, num+1):
                    colorsAndSpecialCards.append(Card(sp, c))

        specialCards = []
        for _ in range(4):
            specialCards.append(Card("wild", None))

        for _ in range(4):
            specialCards.append(Card("wild_draw_four", None))


        deck = colorsAndNumbers
        deck.extend(colorsAndSpecialCards)
        deck.extend(specialCards)
        return deck


    def pullCard(self):
        if len(self.deck) == 0:
            return None
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card


    def __len__(self):
        return len(self.deck)
