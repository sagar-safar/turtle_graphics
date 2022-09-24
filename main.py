from turtle import Turtle, Screen
import random

timy = Turtle()
colors = ["green yellow", "dark orange", "pink", "firebrick", "medium spring green", "medium turquoise"]
for side in range(3,11):
    angle = 360//side
    timy.pencolor(random.choice(colors))

    for _ in range(side):
        timy.rt(angle)
        timy.fd(100)

my_screen = Screen()
my_screen.exitonclick()




