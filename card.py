

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color


    def isNumber(self):
        return True if type(self.value) == int else False

    def isPlusFour(self):
        return True if "wild_draw_four" in str(self.value) else False

    def isWild(self):
        return True if "wild" == str(self.value) else False

    def isPlusTwo(self):
        return True if str(self.value) == "draw_two" else False

    def isSkip(self):
        return True if str(self.value) == "skip" else False

    def isReverse(self):
        return True if str(self.value) == "reverse" else False

    def toString(self):
        return f"{str(self.color)} {str(self.value)}"

    '''def __str__(self):
        if self.color is None:
            return str(self.value)
        else:
            return self.color + " " + str(self.value)'''




#card = Card(2, "red")
#print(card.is_number())