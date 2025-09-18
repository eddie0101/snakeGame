# Snake Game

## Overview
This is a classic Snake game implemented in Python using the Turtle graphics library. The game features a snake that moves around the screen and can be controlled with arrow keys.

## Current State
- **Language**: Python 3.12
- **Graphics Library**: Turtle
- **Game Status**: Fully functional and ready to play
- **Display Method**: VNC (Virtual Network Computing) for GUI display

## Project Architecture
- `main.py`: Entry point that sets up the game screen, handles user input, and starts the game
- `snake.py`: Contains the Snake class with movement logic and control methods
- `food.py`: Contains the Food class that handles food generation and positioning
- `constants.py`: Shared constants used across the game components

## How to Play
1. The game runs automatically when the workflow starts (VNC pane opens automatically)
2. Use arrow keys to control the snake:
   - Up arrow: Move up
   - Down arrow: Move down
   - Left arrow: Move left
   - Right arrow: Move right
3. Click on the game window to close it

## Technical Details
- Game window: 600x600 pixels
- Background: Black
- Snake segments: White squares
- Movement speed: Updates every 200ms
- Initial snake length: 5 segments

## Recent Changes
- **2025-09-11**: Imported from GitHub and configured for Replit environment
- **2025-09-11**: Set up VNC workflow for GUI display
- **2025-09-11**: Verified Python 3.12 environment compatibility

## User Preferences
- Project imported from GitHub and set up to run in Replit's VNC environment
- Maintains original game mechanics and appearance