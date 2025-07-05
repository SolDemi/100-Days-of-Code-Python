from turtle import Turtle, Screen
from random import *
from hirst_painting import extract_hirst_painting

class TurtleChallenge:
    def __init__(self, speed):
        self.screen = Screen()
        self.turtle = Turtle()
        self.turtle.speed(speed)

    def move(self, distance, change_angle):
        """
        Challenge 3
        :param distance:
        :param change_angle:
        :return:
        """
        self.turtle.pencolor(random(), random(), random())

        for i in range(change_angle):
            self.turtle.forward(distance)
            self.turtle.left(360/change_angle)


    def random_work(self, steps,distance):
        """
        Challenge 4
        :param steps:
        :param distance:
        :return:
        """

        for step in range(steps):
            self.turtle.pencolor(random(), random(), random())
            self.turtle.setheading(choice([0, 90, 180, 270]))
            self.turtle.forward(distance)
        self.turtle.end_fill()

    def spirograph(self, radius, angle):
        """
        Challenge 5
        :return:
        """
        n = 0
        while True:
            self.turtle.pencolor(random(), random(), random())
            self.turtle.setheading(self.turtle.heading() + angle)
            n = n+1
            self.turtle.circle(radius)
            if n == int(360/angle):
                break

    def dot_plot(self, scale):
        """
        final project
        :param scale: int
        :return:
        """
        self.screen.colormode(255)
        hirst_rpg = extract_hirst_painting()
        self.turtle.hideturtle()

        self.turtle.teleport(-240,-100)
        original_x = self.turtle.xcor() # solution 2


        for _ in range(scale): # column
            for __ in range(scale): # row
                self.turtle.dot(20, choice(hirst_rpg))
                self.turtle.forward(50)

            # solution 1
            # turn_direction = 0
            # if self.turtle.heading() == 0:
            #     turn_direction = 180
            # elif self.turtle.heading() == 180:
            #     turn_direction = 0
            # self.turtle.setheading(90)
            # self.turtle.forward(50)
            # self.turtle.setheading(turn_direction)
            # self.turtle.forward(50)

            #solution 2
            y = self.turtle.ycor()
            self.turtle.setx(original_x)
            self.turtle.sety(y + 50)




turtle = TurtleChallenge(20)
# turtle.penup()
# turtle.sety(-350)
# turtle.shape("turtle")
# turtle.pendown()
# for num in range(3,21):
#     turtle.move(100, num)

# turtle.turtle.pensize(15)
# turtle.random_work(100,60)

# turtle.turtle.pensize(3)
# turtle.spirograph(200,5)

turtle.dot_plot(10)

turtle.screen.mainloop()
