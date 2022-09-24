from turtle import Turtle, Screen
import random

timy = Turtle()
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=400, height=400)
timy.fillcolor("yellow")
def draw_star():
    timy.begin_fill()
    for _ in range(5):
        timy.fd(20)
        timy.right(144)
    timy.end_fill()


num_stars = 20

while num_stars>0:
    draw_star()
    x_ = random.randint(-180, 180)
    y_ = random.randint(-180, 180)
    timy.penup()
    timy.goto(x=x_,y=y_)
    timy.pendown()
    num_stars -= 1






my_screen.exitonclick()

