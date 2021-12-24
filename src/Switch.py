from src.PlayingCard import PlayingCard
from src.ConsoleInput import ConsoleInput
from src.ConsoleOutput import ConsoleOutput

class switch():

    #instantiate variables
    no_of_cards = 7
    no_of_players = 2
    gameInput = ConsoleInput()
    playingCard = PlayingCard()
    output = ConsoleOutput()

    #sets game input so that test inputs can be run
    def set_game_input(self, game_input):
        self.gameInput = game_input

    #player turn logic, checks if can play from their hand
    #if they can loop until a valid card is input, check the card
    #against the top card, if valid continue, if not ask again
    #if the player cannot play from their hand they must draw a card
    #from the deck
    def player_turn(self, deck, hand, top_card):
        self.output.display(f"Your Hand is: \n{hand}")
        waiting = True
        can_play = self.can_play(hand, top_card)
        while waiting:
            if can_play:
                try:
                    card = self.gameInput.getString("Select a card to play: ").upper()
                except ValueError:
                    card = self.gameInput.getString("Please enter a valid card!: ").upper()
                    continue
                if not self.can_play_card(list(card), top_card):
                    self.output.display("Please select a valid card!")
                    continue
                else:
                    index = hand.index(card)
                    top_card[0] = hand.pop(index)
                    self.show_top_card(top_card)
                    waiting = False
            else:
                self.output.display("You must draw a card!")
                hand.append(self.playingCard.deal_a_card(deck))
                waiting = False

    #cpu player logic, determines whether can play from their hand
    #if it can, finds all valid cards and pops one from the list
    #if it cannot it must draw a card from the deck
    def computer_turn(self, deck, hand, top_card):
        valid_cards = []
        can_play = self.can_play(hand, top_card)
        if can_play:
            valid_cards = self.computer_valid_cards(hand, top_card)
            card = valid_cards.pop()
            index = hand.index(card)
            card = hand.pop(index)
            top_card[0] = card
            self.show_top_card(top_card)
        else:
            self.output.display("CPU must draw a card!")
            hand.append(self.playingCard.deal_a_card(deck))
            self.show_top_card(top_card)

    #finds all cards that the cpu can play from their hand
    def computer_valid_cards(self, hand, top_card):
        valid = []
        for card in hand:
            if self.can_play_card(card, top_card):
                valid.append(card)
        return valid

    #determines whether the players selected card can be played
    def can_play_card(self, card, top_card):
        for i in card:
            if i in list(top_card[0]):
                return True
        return False

    #determines whether the player can play a card from their hand
    def can_play(self, hand, top_card):
        target = list(top_card[0])
        for card in hand:
            for i in card:
                if i in target:
                    return True
        return False

    #displays the top card which the players must match to
    def show_top_card(self, top_card):
        self.output.display(f"\nTop Card: [{top_card[0]}]\n")

    #main game loop
    def play_switch(self, deck, hands):
        top_card = []
        playing = True
        player_hand = hands[self.playingCard.user_hand]
        CPU_hand = hands[1]
        top_card.append(deck.pop())    #starts the stack with the card from the top of the deck
        self.show_top_card(top_card)
        while playing:
            self.player_turn(deck, player_hand, top_card)
            if len(player_hand) < 1:
                self.output.display("You Win!")
                playing = False
            self.output.display("\nCPU turn\n")
            self.computer_turn(deck, CPU_hand, top_card)
            if len(CPU_hand) < 1:
                self.output.display(f"CPU hand: {CPU_hand}")
                self.output.display(f"Your hand: {player_hand}")
                self.output.display("CPU wins, unlucky!")
                playing = False


    def main(self):
        deck = self.playingCard.generate_deck()
        deck = self.playingCard.shuffle_cards(deck)
        hands = self.playingCard.deal_cards(deck, self.no_of_cards, self.no_of_players)
        self.play_switch(deck, hands)


if __name__ == "__main__":
    switch = switch()
    switch.main()