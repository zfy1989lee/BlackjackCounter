# High-Low method functions
# https://www.youtube.com/watch?v=G_So72lFNIU
# https://www.blackjackincolor.com/truecount1.htm (Graphs about True Count frequencies)
# True Count = Running Count / # of Decks Remaining Rounded to Nearest Half Deck

# UPDATED (8/14/17)

import Card
import Decks

class Hi_Lo:
    def __init__(self, numOfDecks: int):
        self._deck = Decks(numOfDecks)
        self._runningCount = int()
        self._trueCount = int()
        
    def update_running_count(self, cards: list):
        '''
        Updates the running count with list of Cards in current deal.
        '''
        for card in cards:
            self._runningCount += card.get_count()
        self._deck.subtract(cards)
        return
    
    def update_true_count(self, cards: list):
        '''
        Updates the true count with list of Cards in current deal.
        '''
        self._trueCount = self._runningCount / self._deck._get_remaining_count()
    
    def get_running_count(self):
        '''
        Returns the current running count of the deck.
        '''
        return self._runningCount
    
    def get_true_count(self):
        '''
        Returns the true count of the deck.
        '''
        return self._trueCount