from turtle import Turtle, Screen
import random

def turtle_race(number_of_turtle, colors, speed):

    screen = Screen()
    screen.setup(width=1000, height=800)
    # 用户下注，获取输入
    user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
    # 打乱颜色顺序
    random.shuffle(colors)
    turtles = []
    for turtle_index in range(1, number_of_turtle + 1): # number of turtles
        turtle_name = Turtle(shape="turtle")
        turtles.append(turtle_name)

        turtle_name.color(colors[turtle_index - 1])
        turtle_name.speed(speed)
        turtle_name.penup()
        turtle_name.goto(10 - screen.window_width() / 2, screen.window_height() * (turtle_index / (number_of_turtle + 1) - 1 / 2))

    while True:
        for turtle in turtles:
            turtle.dot( turtle.color()[1]) # 绘制行动点图
            random_move = random.randint(0,25)
            turtle.forward(random_move)
            if turtle.xcor() >= screen.window_width()/2:
                winner = turtle
                break
        try:
            if winner.color()[1] == user_bet:
                print("You Win!")
            else:
                print(f"The winner is the {winner.color()[1]} turtle. You lose!")
            break
        except NameError:
            pass

    screen.bye()

number_of_turtle = 7
colors = ["red", "blue", "green", "yellow", "purple", "orange", "indigo"]
turtle_race(7, colors, 5)
