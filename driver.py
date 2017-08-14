# Driver

# UPDATED (8/14/17)

import Hi_Lo
# import kivy

if __name__ == '__main__':
    numOfDecks = input('How many decks are in the master blackjack deck? (1-8): ')
    master = Hi_Lo(numOfDecks, 0)
    print(master.get_running_count())
    print(master.get_true_count())