from turtle import Turtle, Screen

timy = Turtle()
my_screen = Screen()
my_screen.listen()


def move_fd():
    timy.fd(10)


def move_bk():
    timy.bk(10)


def move_left():
    timy.lt(10)

def move_right():
    timy.rt(10)


def clear():
    timy.clear()
    timy.penup()
    timy.home()
    timy.pendown()

def red_color():
    timy.color("red")

def blue_color():
    timy.color("blue")

def green_color():
    timy.color("green")




my_screen.onkey(move_fd, "w")
my_screen.onkey(move_bk, "s")
my_screen.onkey(move_left, "a")
my_screen.onkey(move_right, "d")
my_screen.onkey(clear, "c")
my_screen.onkey(red_color, "r")
my_screen.onkey(blue_color, "b")
my_screen.onkey(green_color, "g")



my_screen.exitonclick()

