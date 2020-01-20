

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color


    @property
    def values(self):
        return (self.value, self.color)
