import random
import time
import turtle

from torch import rand
tutel = turtle.Turtle()
#tutel.speed(100)
#for i in range(40):
    #tutel.circle(100)
    #tutel.left(10)
#for i in range(25):
    #tutel.left(13.7)
    #tutel.circle(140)
#time.sleep(10)
tutel.turtlesize(100)
for i in range(99):
    tutel.forward(100)
    tutel.left(random.randint(150,360))
