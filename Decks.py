# Typically 1-8 decks of 52 cards in main deck

# UPDATED (7/30/17)
# UPDATED (8/14/17)

import Card

class Decks:
    def __init__(self, numOfDecks: float):
        self._staticNumOfDecks = int(numOfDecks)
        self._numOfDecks = numOfDecks   # Count to nearest half-deck
        self._percOutOfDeck = float()   # default 0.0
        self._cardList = list()
        self._setUp()
        
    def _setUp(self):
        '''
        Initializes Cards in Decks.
        '''
        for deck in range(0, self._numOfDecks):
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                card = Card(value)
                self._cardList.append(card)
        return
    
    def _round_to_nearest_half(self, value: float):
        '''
        Rounds and returns value to nearest 0.5.
        '''
        return round(value * 2) / 2
    
    def subtract(self, cards: list):
        '''
        Take out specific list of Cards from master deck after each round of card dealings.
        Also update self._percOutOfDeck and self._numOfDecks.
        '''
        for card in cards:
            self._cardList.remove(card)
        self._percOutOfDeck += len(cards)/self._staticNumOfDecks
        self._numOfDecks = self._round_to_nearest_half(len(self.cardList)/26)
        return
                
    def get_Deck_Count(self):
        '''
        Returns number of Cards in Decks as an int.
        '''
        return len(self._cardList)
    
    def get_Remaining_Count(self):
        return self._percOutOfDeck