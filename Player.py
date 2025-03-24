from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")  # Represent the paddle as a square
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)  # Stretch into a rectangle
        self.speed("fastest")
        self.setheading(90)  # Default heading upwards

    def move_up(self):
        """Move the paddle up."""
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        """Move the paddle down."""
        self.setheading(270)
        self.forward(20)
