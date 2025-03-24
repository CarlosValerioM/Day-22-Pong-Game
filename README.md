# Pong Game  
A simple Pong game using the Turtle module.  

## Author:  
Carlos Valerio (CarlosValerioM)  

## Date:  
2025/03/23  

## License:  
MIT License  

## Dependencies:  
None (built-in functions only)  

## Description:  
`pong.py` is a simple Python implementation of the classic Pong game.  
It includes:  
1. A game window with a black background.  
2. Two player-controlled paddles (left and right).  
3. A ball that moves and bounces off the walls and paddles.  
4. A scoring system where the ball resets upon crossing the left or right boundary.  

## Controls:  
- **Player 1 (Left Paddle):**  
  - Move Up: `"Up"` arrow key  
  - Move Down: `"Down"` arrow key  

- **Player 2 (Right Paddle):**  
  - Move Up: `"W"` key  
  - Move Down: `"S"` key  

## Usage:  

1. Clone this repository:  

```bash
git clone https://github.com/CarlosValerioM/Pong-Game.git
```
Navigate to the project directory:

```bash
cd Pong-Game
```
Run the script:

```bash
python pong.py
```
## How It Works:
The ball moves automatically at the start of the game.

Players use their assigned keys to move the paddles up and down.

The ball bounces off the top and bottom walls.

If the ball touches a paddle, it bounces back.

If the ball passes a paddle, it resets to the center.

## License:
This project is licensed under the MIT License.
