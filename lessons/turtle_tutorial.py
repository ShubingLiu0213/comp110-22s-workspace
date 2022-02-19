from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")
leo.speed(50)
i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i += 1
leo.penup()
leo.goto(00, 00)
leo.pendown()
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()
leo.hideturtle


bob: Turtle = Turtle()
bob.color(2, 23, 24)
bob.penup()
bob.goto(00, 00)
bob.pendown()
bob.speed(10)
bob.begin_fill()
i: int = 0
while(i < 3):
    bob.forward(190)
    bob.left(120)
    i += 1

side_length = 300

i: int = 0
while(i < 3):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(122)
    i += 1
bob.end_fill()

done()
