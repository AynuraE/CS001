#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Deck class

from card import Card #importing
from random import randint

class Deck:
    def __init__(self):
        self.card_list = [] #creating an empty list

    def add_standard_cards(self):
        for suit in range(1, 5):
            for value in range(1, 14):
                self.card_list.append(Card(value, suit)) 

    def shuffle(self):
        for i in range(len(self.card_list)):
            num = randint(0, len(self.card_list) - 1) #randint gets a random card from any index 0 to last.
            new_card = self.card_list[num]
            self.card_list[num] = self.card_list[i]
            self.card_list[i] = new_card

    def deal(self, n):
        hand = Deck() #created a new object called hand within the Deck class
        for _new in range(n): #underscore is for not using the variable later
            new_item = self.card_list.pop() #removes the last item from a list
            hand.card_list.append(new_item) #adds the new item to the hand
        return hand

