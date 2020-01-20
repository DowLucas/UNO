from deck import Deck
from player import Player

import random

class Game:
    def __init__(self, num_players, num_start_cards=7):
        self.num_players = num_players
        self.__player_has_won = False
        self.reversed = False
        self.current_color = None

        self.current_card = None
        self.players = {i: Player() for i in range(1, num_players+1)}
        self.deck = Deck()


        self.startGame()
        self.gameLoop()

    def startGame(self):
        for player in self.players.values():
            for _ in range(7):
                if len(self.deck) != 0:
                    player.addCard(self.deck.pullCard())

        self.current_card = self.deck.pullCard()
        self.current_color = self.current_card.color
        self.numberPlayerTurn = random.randint(1, self.num_players)


    def gameLoop(self):
        if not self.__player_has_won:
            print(f"The top card in the discard pile is: {self.current_card}")
            print(f"Player {self.numberPlayerTurn}s turn. Please select your card\n")

            player_turn_hand = {i: card for i, card in enumerate(self.players[self.numberPlayerTurn].hand)}
            cards_able_to_play = self._handCheck(player_turn_hand)


            print("")



            input("Card number: ")


    def CheckIfCardCanBePlaced(self, card):
        # Lets first go trough each case when the current card is a number card
        if self.current_card.value == card.value or self.current_card.color == card.color:
            return True

        return False

    def _handCheck(self, hand):
        cardsAbleToPlay = {}
        for i in hand.keys():
            print(hand[i], self.CheckIfCardCanBePlaced(hand[i]))


game = Game(4)




for player in game.players.values():
    print(player.hand)



