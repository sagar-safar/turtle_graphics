from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="make your bet", prompt="which turtle will win? enter the color : ")



colors = ["red", "blue", "green", "orange", "yellow", "purple"]


start_y = -120
all_turtle = []
is_race_on = True



for player in colors:
    tim = Turtle(shape="turtle")
    tim.color(player)
    tim.penup()
    tim.goto(x=-230, y=start_y)
    start_y += 50
    all_turtle.append(tim)



while is_race_on:

    for turtle in all_turtle:
        random_dist = random.randint(0, 10)
        turtle.fd(random_dist)
    for turtle in all_turtle:

        if turtle.xcor() >= 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"you won the bet! {user_bet} turtle won the race")

            else:
                print(f"you loose the bet! {turtle.pencolor()} turtle won tha match")











my_screen.exitonclick()
