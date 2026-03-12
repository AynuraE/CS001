#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Timer driver

from Week6.timer import Timer

t1 = Timer(1, 30, 0) #Object

while t1.is_zero() != True: #accessing to the 'is_zero' function in my timer.py that while it's not equal to True, it prints Timer object and tick.
    print(t1)
    t1.tick()

print(t1)
