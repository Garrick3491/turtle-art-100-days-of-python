from turtle import Turtle, Screen
import random
import colorgram

directions = [0, 90, 180, 270]
colors = []
for color in colorgram.extract('image.jpg', 30):
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    colors.append((r, g, b))


def random_colour():
    return random.choice(colors)


def draw_dot(turtle):
    colour = random_colour()
    turtle.pencolor(colour)
    turtle.dot(20, colour)
    turtle.forward(50)

def new_row(turtle):
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)


screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.hideturtle()
turtle.pensize(1)
turtle.speed("fastest")
turtle.penup()
turtle.setheading(220)
turtle.forward(500)
turtle.setheading(0)


for dot_count in range(1, 101):
    draw_dot(turtle)
    if dot_count % 10 == 0:
        new_row(turtle)

screen.exitonclick()