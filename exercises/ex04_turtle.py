"""EX04 - Happy Valentine's Day!"""

__author__ = "730508266"

from turtle import Turtle, done


def main() -> None:
    """The entrypoint of my scene."""
    heart: Turtle = Turtle()
    pattern: Turtle = Turtle()
    edge: Turtle = Turtle()
    triangle: Turtle = Turtle()
    a_heart(heart, -12, 100)
    star(pattern, -12, 100)
    star(pattern, -205, 100)
    side(edge, 0, -145)
    a_triangle(triangle, 300, 300)
    a_triangle(triangle, -300, -300)
    a_triangle(triangle, 300, -300)
    a_triangle(triangle, -300, 300)
    done()


def a_heart(heart: Turtle, x: float, y: float) -> None:
    """A beautiful heart."""
    heart.pensize(3)
    heart.color("red", "pink")
    heart.speed(10)
    heart.up()
    heart.goto(x, y)
    heart.down()
    heart.begin_fill()
    heart.left(90)
    heart.circle(120, 180)
    heart.circle(360, 70.529)
    heart.left(38.942)
    heart.circle(360, 70.529)
    heart.circle(120, 180)
    heart.end_fill()
    heart.up()
    heart.goto(-250, -150)
    heart.down()
    

def star(pattern: Turtle, x: float, y: float) -> None:
    """A colorful star."""
    pattern.pensize(4)
    color = ['yellow', 'orange', 'green', 'cyan', 'blue']
    pattern.speed(10)
    pattern.up()
    pattern.goto(x, y)
    pattern.down()
    for i in range(5):
        pattern.pencolor(color[i])
        pattern.forward(200)
        pattern.right(144)
    pattern.up()
    pattern.goto(x + 100, y - 140)
    pattern.down()
    pattern.pencolor("Black")
    pattern.down()


def side(edge: Turtle, x: float, y: float) -> None:
    """Different sides patterns."""
    edge.pensize(3)
    edge.color("blue", "red")
    edge.speed(10)
    edge.up()
    edge.goto(x, y)
    edge.down()
    edge.begin_fill()
    edge.forward(-400)
    for i in range(3, 10):
        edge.circle(40, steps=i)  
        edge.forward(100)  
    edge.circle(40)  
    edge.end_fill() 
    edge.hideturtle()  


def a_triangle(triangle: Turtle, x: float, y: float) -> None:
    """A triangle."""
    triangle.pensize(3)
    triangle.color("blue")
    triangle.speed(10)
    triangle.up()
    triangle.goto(x, y)
    triangle.down()
    triangle.begin_fill()
    triangle.forward(100)
    triangle.left(120)
    triangle.forward(100)

    triangle.left(120)
    triangle.forward(100)


if __name__ == "__main__":
    main()