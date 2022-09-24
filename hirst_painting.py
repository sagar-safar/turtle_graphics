import turtle as t
import random
def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r,g,b


timy = t.Turtle()
timy.penup()
timy.ht()
t.colormode(255)
timy.setheading(225)
timy.fd(300)
timy.setheading(0)
current_heading = list(timy.pos())
x = current_heading[0]
y = current_heading[1]


for dots in range(1, 101):
    timy.dot(20, random_color())

    timy.fd(50)

    if dots % 10 == 0:
        timy.setx(x)
        y += 50
        timy.sety(y)




my_screen = t.Screen()
my_screen.exitonclick()
