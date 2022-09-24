from turtle import Turtle, Screen

timy = Turtle()
timy.speed(0)

my_screen = Screen()



my_screen.setup(width=500, height=500)

def arrow():
    timy.penup()
    timy.width(5)
    timy.color("black")
    timy.goto(x=-125, y=40)
    timy.pendown()
    timy.setheading(0)
    timy.lt(29)
    timy.fd(325)
    timy.lt(150)
    timy.fd(60)
    timy.bk(60)
    timy.lt(60)
    timy.fd(60)


def arc():
    for _ in range(200):
        timy.fd(1)
        timy.rt(1)


def heart():
    timy.fillcolor("red")
    timy.begin_fill()

    timy.lt(140)
    timy.fd(113)
    arc()
    timy.lt(120)
    arc()
    timy.fd(113)
    timy.end_fill()


heart()
arrow()







my_screen.exitonclick()

