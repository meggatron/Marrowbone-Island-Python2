# Marrowbone2-004-pygame-GUI / main.py


# import the files this program needs from the game folder
from game import gui, locations, player


# start pygame and create the game window
gui.start()


# ask the player for their name and save it in player.py
player.player_name = gui.get_input("What is your name, adventurer?")


# display a welcome message using the saved player name
gui.display(f"Welcome, {player.player_name}. Your quest begins now.")


# pause for 1500 milliseconds so the player has time to read = 1.5 seconds
gui.pause(1500)


# this variable keeps track of where the player currently is
# the game always begins at the dock
current_location = "dock"


# keep running location functions until one of them returns "end"
while current_location != "end":

    # locations.locations is the dictionary at the bottom of locations.py
    # current_location is used as the dictionary key
    # the dictionary gives us the correct location function
    # () runs that function
    # whatever the function returns becomes the next current_location
    current_location = locations.locations[current_location]()


# once current_location becomes "end" the while loop stops
gui.display("Game over.")


# keep the final message on screen for 3 seconds
gui.pause(3000)


# close pygame and end the program
gui.quit()