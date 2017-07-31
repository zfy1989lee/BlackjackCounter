# High-Low method functions
# https://www.youtube.com/watch?v=G_So72lFNIU
# https://www.blackjackincolor.com/truecount1.htm (Graphs about True Count frequencies)
# True Count = Running Count / # of Decks Remaining Rounded to Nearest Half Deck

import Card
import Decks

class Hi_Lo:
    def __init__(self, numOfDecks: int, percOutOfDeck: float):
        self._decks = numOfDecks
        self._perc = percOutOfDeck
    
    def get_running_count(self):
        pass
    
    def get_true_count(self):
        pass 