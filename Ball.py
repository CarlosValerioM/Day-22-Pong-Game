from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # Represent the ball as a circle
        self.penup()
        self.color("white")
        self.speed("fastest")  # Set the fastest speed
        self.setheading(random.randrange(-365, 365))  # Start with a random direction

    def bounce_y(self):
        """Bounce the ball when it hits the top or bottom walls."""
        if -250 >= self.ycor() or self.ycor() >= 250:
            bounce = self.heading() * -1  # Reverse the angle
            self.setheading(bounce)

    def score(self):
        """Reset the ball to the center if it passes the left or right boundary."""
        if -400 >= self.xcor() or self.xcor() >= 400:
            self.goto(0, 0)  # Reset position to the center

    def collision(self, player):
        """Bounce the ball when it collides with a player's paddle."""
        distance = self.distance(player)
        if (-350 >= self.xcor() or self.xcor() >= 350) and distance < 50:
            bounce = 180 - self.heading()  # Reflect the angle
            self.setheading(bounce)
