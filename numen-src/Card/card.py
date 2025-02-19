class Card:
    def __init__(self, value, is_visible = False, is_burnt = False):
        self.value = value
        self.is_visible = is_visible
        self.is_burnt = is_burnt

    def flip(self):
        self.is_visible = not self.is_visible

    def burn(self): #cards get burnt only once
        self.is_burnt = True

    def getvalue(self):
        return self.value


    # Learning OOP in Python from java