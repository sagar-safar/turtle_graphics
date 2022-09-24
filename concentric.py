from turtle import Turtle, Screen

timy = Turtle()
radius = 10

for i in range(1,5):
    timy.circle(radius*i)
    timy.up()
    timy.sety(-(radius*i))
    timy.down()



