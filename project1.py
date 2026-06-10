import random as rd

cards_no = {"spade":13,"clubs":13, "Hearts":13, "Diamonds":13}
cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "king", "queen"]

class play:
  def __init__(self,cards):
    self.spade = cards.copy()
    self.clubs = cards.copy()
    self.hearts = cards.copy()
    self.diamonds = cards.copy()

  def no (self):
    self.spade_no = 13
    self.clubs_no = 13
    self.hearts_no = 13
    self.diamonds_no = 13


  def show(self):
    print(f"spade: {self.spade} has {self.spade_no} cardS")
    
My_cards = play(cards)
My_cards.no()
My_cards.show()





