import turtle as t
import random
direction = [0, 90, 180, 270]

timy = t.Turtle()
timy.width(15)
timy.speed(10)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    return r, g, b


for _ in range(200):
    timy.color(random_color())
    timy.setheading(random.choice(direction))
    timy.fd(30)










my_screen = t.Screen()
my_screen.exitonclick()