#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Counter Driver

from counter import Counter

c1 = Counter(60, 0, 1) #Object
c2 = Counter(40, 1, 4)

print("Try out get value:", c1.get_value())
print("Try out tick:", c1.tick())
print("Try out string:", c1)

print("Try out get value:", c2.get_value())
print("Try out tick:", c2.tick())
print("Try out string:", c2)