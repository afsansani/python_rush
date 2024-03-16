#making some triangles that ultimately creates a pentagon in the center

from turtle import *

#object spawning region
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

#Let's make a basic triangle first
## Imagine an acute triangle with 60 DEG values for all corners
t1.color("orange")
t1.speed(1)
t1.width(4)

t2.color("red")
t2.speed(1)
t2.width(4)

t3.color("black")
t3.speed(1)
t3.width(4)

#making one triangle
#t1.begin_fill()
t1.left(60)
t1.fd(50) #movement 50 units. [Imagine, AB has length 50]
t1.right(60)
t1.right(60)
t1.fd(50)
t1.right(120)
t1.fd(50)
#t1.end_fill()
#DEG = 60
#length = 50

#starRED
for i in range(5):
    t2.fd(150)
    t2.left(144)

# starBLACK
t3.goto(150,50)
t3.begin_fill()
for j in range(5):
    t3.fd(150)
    t3.left(144)
t3.end_fill()
#make the drawing stay on screen
done() 