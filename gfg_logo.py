from turtle import Turtle, Screen

timy = Turtle()
my_screen = Screen()
timy.color("green")
timy.width(10)
my_screen.bgcolor("black")


def arc():
    for _ in range(180):
        timy.rt(1)
        timy.fd(2)



def gfg():
    arc()
    timy.rt(90)
    timy.fd(114)
    timy.rt(90)
    timy.fd(245)
    timy.rt(90)
    timy.fd(114)
    timy.rt(90)
    arc()


gfg()
my_screen.exitonclick()