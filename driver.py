#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Ball driver

from Week5.ball import Ball

b1 = Ball(50, 100, 20)
b2 = Ball(200, 200, 100)

print("Address of b1:", b1)
print("Address of b2:", b2)
print(b1.x, b2.x)

b1.update()
b2.update()