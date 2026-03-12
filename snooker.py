from ball import Ball
from random import randint
from Week6.ball import Ball


class Snooker:
     def __init__(self):
         self.balls = []
         self.num_balls = num_balls

     def initialize_balls(self):
         for i in range(self.num_balls):
             self.balls.append(Ball())

     def update(self):
         for b in self.balls:
             b.update(randint(-5, 5))
            