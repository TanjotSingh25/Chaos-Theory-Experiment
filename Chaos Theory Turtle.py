from turtle import *
from random import *

speed(0)
s = []
#for i in range(6):
    #s.append(randrange(-250, 250))

penup()
sides = [(0, 250), (-250, 0), (250, 0)]

for i in range(3):
    goto(sides[i])
    dot(8, "Red")

r = (randrange(-100, 100), randrange(-100, 100))
goto(r)

while (True):
    rp = randrange(0, 3)
    side = sides[rp]
    r = ( (side[0]+r[0])/2, (side[1]+r[1])/2 )
    goto(r)
    dot(2)

done()