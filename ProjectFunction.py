import turtle
from random import randint
bob=turtle.Turtle()
bob.speed(0)

def eyes():
    righteye()
    lefteye()
    
def lefteye():
    home()
    jump(-25,-70)
    bob.begin_fill()
    bob.color("black")
    bob.right(185)
    for times in range(15):
        bob.forward(10)
        bob.right(4)
    for times in range(10):
        bob.forward(12)
        bob.right(16)
    for times in range(16):
        bob.forward(9.6433256)
        bob.right(3)
    bob.end_fill()


def righteye():
    jump(25,-70)
    bob.begin_fill()
    bob.color("black")
    bob.left(5)
    for times in range(15):
        bob.forward(10)
        bob.left(4)
    for times in range(10):
        bob.forward(12)
        bob.left(16)
    for times in range(16):
        bob.forward(9.6433256)
        bob.left(3)
    bob.end_fill()



def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()




def polygon_fill(sides, distance, c):
    bob.color(c)
    angle=360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def polygon(sides, distance, c):
    bob.color(c)
    angle=360/sides
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)


def home():
    bob.penup()
    bob.home()
    bob.pendown()

def fillcircle(distance,c):
    bob.begin_fill()
    bob.color(c)
    bob.circle(distance)
    bob.end_fill()

def greenhead():
    home()
    bob.begin_fill()
    bob.color("light green")
    jump(0,-200)
    bob.left(25)
    for times in range(20):
        bob.forward(20)
        bob.left(4)
    bob.left(75)
    bob.forward(335)
    bob.left(79)
    for times in range(20):
        bob.forward(20)
        bob.left(4)
    bob.end_fill()
    home()
    jump(-1,-64)
    fillcircle(169,"light green")

def stars():  
    for times in range(20):
        x=randint(0,5)
        y=randint(0,5)
        jump(x*75,y*75)
        fillcircle(5,"white")
    for times in range(20):
        x=randint(0,5)
        y=randint(0,5)
        jump(x*-75,y*-75)
        fillcircle(5,"white")
    for times in range(20):
        x=randint(0,5)
        y=randint(0,5)
        jump(-x*75,y*75)
        fillcircle(5,"white")
    for times in range(20):
        x=randint(0,5)
        y=randint(0,5)
        jump(x*75,-y*75)
        fillcircle(5,"white")

