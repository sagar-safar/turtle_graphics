import turtle as t
import random
timy = t.Turtle()
timy.speed("fastest")
t.colormode(255)


radius = 100

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r,g,b


for _ in range(360//5):
    timy.color(random_color())

    timy.circle(radius)
    timy.setheading(timy.heading()+5)











my_screen = t.Screen()
my_screen.exitonclick()
