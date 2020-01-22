from deck import Deck
from player import Player
import re

import random

class Game:
    def __init__(self, num_players, num_start_cards=7):
        self.num_players = num_players
        self.__player_has_won = False
        self.reversed = False
        self.current_color = None
        self.pickup_card_played = False
        self.pick_up_multiplier = 1

        self.discard_pile = []
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
        
        if self.current_card == None:
            self.current_card = random.choice(self.deck.colors)

        
        self.number_player_turn = random.randint(1, self.num_players)


    def playerSelectCard(self, hand):


        pick_up_card = self._handCheck(hand)

        if pick_up_card != None:
            return pick_up_card

        if pick_up_card is False:
            return False


        d = {i: self.CheckIfCardCanBePlaced(card) for i, card in hand.items()}
        d[-1] = False
        card_index = -1


        while d[card_index] != True:
            card_index = input("Card number: ")

            if card_index.isdigit():
                print("Match")
            else:
                card_index = -1
                continue


            try:
                card_index = int(card_index)
            except:
                card_index = -1
                continue
            print("Invalid card index\n")


        try:
            if self.CheckIfCardCanBePlaced(hand[card_index]):
                return hand[card_index]
            else:
                print(f"\nYou cannot play {hand[card_index].toString()}\n")
                self.playerSelectCard(hand)
        except:
            print("Invalid card number")
            self.playerSelectCard(hand)


    def selecteNewColour(self):
        for c in self.deck.colors:
            print(c)
        new_color = input("Select new colour: ")
        if new_color in self.deck.colors:
            self.current_color = new_color
        else:
            print("Invalid colour\n")
            self.selecteNewColour()

    def checkIfNextPlayerNeedsToPickUp(self, card):
        if card.isPlusFour() or card.isPlusTwo():
            self.pickup_card_played = True
            return True
        else:
            self.pickup_card_played = False
            return False

    def selectNextPlayer(self, card):
        if card == False:
            new_player_index = self.number_player_turn + 1 if not self.reversed else self.number_player_turn - 1
            if new_player_index > len(self.players):
                self.number_player_turn = 1
            elif new_player_index < 1:
                 self.number_player_turn = len(self.players)+1
            else:
                self.number_player_turn = new_player_index
            return

        if card.isSkip() and not self.reversed:
            print("Card is skip and game is not reversed")
            new_player_index = self.number_player_turn + 2

            if new_player_index > len(self.players):
                self.number_player_turn = new_player_index - len(self.players)
            else:
                self.number_player_turn = new_player_index

        elif card.isSkip() and self.reversed:
            new_player_index = self.number_player_turn - 2
            if new_player_index < 1:
                self.number_player_turn = new_player_index + len(self.players)
            else:
                self.number_player_turn = new_player_index

        else:
            new_player_index = self.number_player_turn + 1 if not self.reversed else self.number_player_turn - 1
            if new_player_index > len(self.players):
                self.number_player_turn = 1
            elif new_player_index < 1:
                 self.number_player_turn = len(self.players)
            else:
                self.number_player_turn = new_player_index

        print(self.number_player_turn)

            

    def gameLoop(self):
        if not self.__player_has_won:
            print(f"The top card in the discard pile is {self.current_card.toString()} (COLOUR: {self.current_color})")
            print(f"Player {self.number_player_turn}s turn. Please select your card\n")

            player_turn_hand = {i: card for i, card in enumerate(self.players[self.number_player_turn].hand)}

            print("")
            selected_card = self.playerSelectCard(player_turn_hand)

            if selected_card != False:
                self.players[self.number_player_turn].useCard(selected_card)

                if self.players[self.number_player_turn].hasWon():
                    print(f"Player {self.number_player_turn} has won!")
                    quit()

                print(selected_card.toString(), "VALUE")

                if selected_card.isWild() or selected_card.isPlusFour():
                    if selected_card.isPlusFour() and self.pickup_card_played:
                        self.pick_up_multiplier += 1
                    self.selecteNewColour()

                if selected_card.isPlusTwo():
                    if self.pickup_card_played:
                        self.pick_up_multiplier += 1
                    self.pickup_card_played = True

                if selected_card.isReverse():
                    self.reversed = not self.reversed


                self.pickup_card_played = self.checkIfNextPlayerNeedsToPickUp(selected_card)
                print(f"Next player needs to pickup card = {self.pickup_card_played}")

                self.current_card = selected_card

                if selected_card.color != None:
                    self.current_color = selected_card.color


            self.selectNextPlayer(selected_card)
            print(f"Current length of deck {len(self.deck)}")
            input("Press enter to end go...")



            self.gameLoop()


    def playerPickUpCard(self):
        new_card = self.deck.pullCard()
        self.players[self.number_player_turn].addCard(new_card)

        print(f"You cannot play any card. Your new card is {new_card.toString()}")
        if self.CheckIfCardCanBePlaced(new_card):
            play = input("Would you like to play this card ('y' for yes): ")
            if play == "y":
                return new_card
            else:
                print("You cannot play this card either")
                return None

    def PickUpNCards(self, numcards):
        input(f"You need to pickup {numcards*self.pick_up_multiplier} cards. press enter to continue.")
        for _ in range(numcards*self.pick_up_multiplier):
            new_card = self.deck.pullCard()
            print(f"You recieved a {new_card.toString()}")
            self.players[self.number_player_turn].addCard(new_card)

        self.pickup_card_played = False
        self.pick_up_multiplier = 1


    def CheckIfCardCanBePlaced(self, card):
        if self.pickup_card_played:
            # Check if player has the same card that was played
            if card.value == self.current_card.value:
                return True
            else:
                return False


        # Lets first go trough each case when the current card is a number card
        if self.current_card.value == card.value or self.current_color == card.color:
            return True

        if card.isPlusFour() or card.isWild():
            return True


        return False

    def _handCheck(self, hand):
        card_able_to_play = 0
        for i in hand.keys():
            print(f"{i}:",hand[i].toString(), "      CAN be played" if self.CheckIfCardCanBePlaced(hand[i]) else "      CANNOT be played")
            if self.CheckIfCardCanBePlaced(hand[i]):
                card_able_to_play += 1

        print(card_able_to_play, self.pickup_card_played)

        if card_able_to_play == 0 and self.pickup_card_played:
            self.PickUpNCards(4 if self.current_card.isPlusFour() else 2)
            return False

        if card_able_to_play == 0:
            card = self.playerPickUpCard()

            if card:
                return card
            else:
                return False




game = Game(4)




for player in game.players.values():
    print(player.hand)



