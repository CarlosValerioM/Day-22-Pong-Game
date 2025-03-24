#!/usr/bin/env python3
"""
pong.py - A simple Pong game using the Turtle module.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/23
License: MIT
Dependencies: None (built-in functions only)

Description:
This script implements a basic Pong game with two players and a bouncing ball.
It includes:
1. A game window with a black background.
2. Two player-controlled paddles (one on the left, one on the right).
3. A ball that moves in a random direction at the start.
4. Collision detection with walls and paddles.
5. A scoring system that resets the ball when it goes out of bounds.

Controls:
- Player 1 (Left Paddle):
    - Move Up: "Up" arrow key
    - Move Down: "Down" arrow key
- Player 2 (Right Paddle):
    - Move Up: "W" key
    - Move Down: "S" key

Usage:
Run the script:
    python pong.py

Example Gameplay:
- The ball moves automatically and bounces off the top and bottom walls.
- Players control the paddles to hit the ball.
- If the ball passes a paddle, it resets to the center.

"""
import turtle as t
from Player import Player
from Ball import Ball

def main():
    # Game screen setup
    screen = t.Screen()
    screen.bgcolor("black")  # Set background color to black
    screen.setup(width=800, height=500)  # Define window size
    screen.listen()  # Enable key event detection

    # Create players (paddles)
    player = Player()
    player.goto(-380, 0)  # Position player 1 on the left side

    player2 = Player()
    player2.goto(380, 0)  # Position player 2 on the right side

    # Create the ball
    ball = Ball()

    # Assign key controls for Player 1 (arrow keys)
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")

    # Assign key controls for Player 2 (W and S keys)
    screen.onkey(player2.move_up, "w")
    screen.onkey(player2.move_down, "s")

    # Start game loop
    game_active = True

    while game_active:
        ball.forward(3)  # Move ball forward
        ball.bounce_y()  # Check for collision with top/bottom walls
        ball.score()  # Reset ball if it goes out of bounds

        # Check for collision with players (paddles)
        ball.collision(player)
        ball.collision(player2)

    screen.exitonclick()  # Keep the game window open until clicked


# Run the game only if the script is executed directly
if __name__ == '__main__':
    main()
