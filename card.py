#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Card class

class Card:
    def __init__(self, value, suit):
        self.value = value # A standard deck has 52 cards: one of each value, for each suit. (We ignore the Joker.)
        self.suit = suit

    def __str__(self):
        list_of_suits = ["clubs", "spades", "diamonds", "hearts"] #There are four suits of cards: clubs, spades,
        # diamonds, and hearts

        list_of_values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] #In each suit, there are 13 card values:
        # cards with numbers 1 through 10, the Jack (11), the Queen (12), and the King (13)

        return list_of_values[self.value - 1] + " of " + list_of_suits[self.suit - 1] #a value of a suit

