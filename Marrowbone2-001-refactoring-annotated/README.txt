Marrowbone Island 2 – 001

Project Summary:
This is the starting version of our Python 2 course game, Marrowbone Island
We are refactoring the final Python 1 game by organizing the code into separate files and modules.
The game works the same way, but the code is now easier to organize, read, and expand
We’ll be building on this structure throughout the course


Folder Structure:

main.py             - Starts the game and runs the main game loop

assets/
    intro.txt        - Intro text shown at the start
    log.txt          - Records locations visited by the player

game/
    __init__.py      - Makes game a Python package
    locations.py     - Stores location functions and game logic
    player.py        - Stores player name and inventory


How to Play:        Run main.py to start the game