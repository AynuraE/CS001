#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Counter

class Counter:
    def __init__(self, limit, initial = 0, min_digits = 1):
        self.limit = limit #ending point
        self.count = initial #starting point
        self.min_digits = min_digits #how many digits appear on the screen

    def get_value(self):
        return self.count #pulling the value

    def __str__(self): #All special methods have underscore. Must return a string
        string_count = str(self.count)
        if len(string_count) < self.min_digits:
            while len(string_count) < self.min_digits:
                string_count = "0" + string_count
        return string_count

    def tick(self):
        if self.count <= 0:
            self.count = self.limit - 1 #ticking to 00:59 after 0
            return True
        else:
            self.count = self.count - 1
            return False




