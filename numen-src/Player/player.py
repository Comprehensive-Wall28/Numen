class Player:
    def __init__(self, player_cards):
        self.score = 0
        self.player_cards = player_cards

    def set_score(self, value):
        self.score += value


