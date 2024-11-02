from turtle import Turtle

# Define the Wall class
class Wall:
    def __init__(self):
        self.create_wall()
        self.middle_line()

    def create_wall(self):
        border_turtle = Turtle()
        border_turtle.color("white")
        border_turtle.hideturtle()  # Hide the turtle shape
        border_turtle.pensize(5)
        border_turtle.penup()  # Don't draw while moving to the starting position
        border_turtle.goto(-290, 290)
        border_turtle.speed("fastest")
        border_turtle.pendown()

        for _ in range(4):
            border_turtle.forward(580)  # 600px screen size with 10px padding on each side
            border_turtle.right(90)  # Turn 90 degrees to form the square


    def middle_line(self):
        middle_turtle = Turtle()
        middle_turtle.color("white")
        middle_turtle.hideturtle()  # Hide the turtle shape
        middle_turtle.pensize(5)
        middle_turtle.penup()  # Don't draw while moving to the starting position
        middle_turtle.goto(0, 290)
        middle_turtle.setheading(270)
        middle_turtle.speed("fastest")
        middle_turtle.pendown()

        for i in range(40):
            middle_turtle.forward(5)
            middle_turtle.penup()
            middle_turtle.forward(10)
            middle_turtle.pendown()



