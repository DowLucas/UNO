from deck import Deck
from player import Player

class Game:
    def __init__(self, num_players, num_start_cards=7):
        self.current_card = None
        self.players = {i: Player() for i in range(1, num_players+1)}
        self.deck = Deck()

        self.startGame()

    def startGame(self):
        for player in self.players.values():
            for _ in range(7):
                player.addCard(self.deck.pullCard())




game = Game(4)

for player in game.players.values():
    print(player.hand)



