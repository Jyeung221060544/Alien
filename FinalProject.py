from ProjectFunction import*

turtle.tracer(False)
stars()

jump(-340,170)
fillcircle(150,"yellow")

jump(250,200)
bob.left(45)
for times in range(4):
    bob.width(100+times*-20)
    bob.forward(times*30+10)

bob.width(0)
jump(250,150)
bob.begin_fill()
for times in range(40):
    bob.color("brown")
    bob.forward(6)
    bob.left(10)
bob.end_fill()

turtle.bgcolor("black")
greenhead()
eyes()
home()
jump(-27,-130)
bob.right(15)

for times in range(20):
    bob.width(5)
    bob.forward(4)
    bob.left(3)


turtle.tracer(True)
