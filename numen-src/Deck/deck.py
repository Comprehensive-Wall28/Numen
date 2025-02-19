from ..Card.card import Card

class Deck:
    def __init__(self, size, card_list):
        self.size = size
        self.cards = []
        self.card_list = card_list

    def init_deck(self):
        for i in range(self.size):
            self.cards.append(Card(i))

    def create_cards(self):
       for cards in range(5):

