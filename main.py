from turtle import Screen
from ball import Ball
from wall import Wall

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("PONG - GAME")

wall = Wall()
ball = Ball()
ball.ball_move()

screen.mainloop()

screen.exitonclick()
