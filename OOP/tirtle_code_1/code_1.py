from turtle import *

# object creation
t1 = Turtle()
t2 = Turtle()
obj1 = Turtle()

# object property defining
# t1
t1.color("green")
t1.shape("turtle")
t1.speed(1)
# t2
t2.color("black")
t2.shape("turtle")
t2.speed(1)

# action defining for objects
# t1
t1.left(90)
t1.forward(50)
t1.forward(50)
t1.right(90)
t1.forward(50)
t1.right(90)
t1.forward(30)
t1.right(90)

# t2
t2.forward(50)
t2.left(90)
t2.forward(50)
t2.left(90)

# others
obj1.circle(50)
obj1.circle(40)
obj1.circle(30)
obj1.circle(20)
obj1.circle(10)
obj1.circle(5)

#turtles falling into abyss
t1.forward(25)
t2.forward(25)

t1.left(60) #60 deg rotation
t2.left(60)  # 60 deg rotation

t1.forward(50)
#needs more angles and length
t1.left(30)
t1.fd(20) #write forward or mini version - fd 

t2.forward(50)

t1.shape("circle")
t2.shape("circle")


# others
obj1.color("red")
obj1.circle(5)
obj1.circle(10)
obj1.circle(20)
obj1.circle(30)
obj1.circle(40)
obj1.circle(50)
# done method
done()
