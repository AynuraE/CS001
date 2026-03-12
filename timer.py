#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Timer

from Week6.counter import Counter

class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours, 2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)

    def __str__(self): #All special methods have underscore. Must return a string
        empty_string = " "
        hours_string = str(self.hours) #getting the numbers as strings
        minutes_string = str(self.minutes)
        seconds_string = str(self.seconds)
        return hours_string + ":" + minutes_string + ":"+ seconds_string

    def tick(self):
        if self.seconds.tick():
            if self.minutes.tick():
                self.hours.tick()


    def is_zero(self): #to show 00:00:00
        if self.seconds.get_value() == 0:
            if self.minutes.get_value() == 0:
                if self.hours.get_value() == 0:
                    return True
        return False