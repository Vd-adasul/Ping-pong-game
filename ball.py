from turtle import Turtle, Screen
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fast")
        self.set_random_heading()

    def set_random_heading(self):
        # Set a random heading in a range that ensures it moves diagonally
        self.setheading(random.randint(22, 45))  # Angles for initial movement

    def bounce_ball(self, wall):
        # Bounce at 90 degrees based on the wall hit
        if wall == 'horizontal':
            self.setheading((self.heading() + 270) % 360)  # Reverse the angle for horizontal
        elif wall == 'vertical':
            self.setheading((self.heading() + 270) % 360)


    def ball_move(self):
        self.forward(3)  # Move the ball forward

        # Check for collision with the walls
        if self.xcor() > 290:  # Right wall
            self.bounce_ball('vertical')  # Bounce back from vertical wall
            self.setx(290)  # Reset position to avoid getting stuck
        elif self.xcor() < -290:  # Left wall
            self.bounce_ball('vertical')  # Bounce back from vertical wall
            self.setx(-290)  # Reset position to avoid getting stuck
        elif self.ycor() > 290:  # Upper wall
            self.bounce_ball('horizontal')  # Bounce back from horizontal wall
            self.sety(290)  # Reset position to avoid getting stuck
        elif self.ycor() < -290:  # Lower wall
            self.bounce_ball('horizontal')  # Bounce back from horizontal wall
            self.sety(-290)  # Reset position to avoid getting stuck

        # Schedule the next movement
        self.getscreen().ontimer(self.ball_move, 2)
