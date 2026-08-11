# Marrowbone Island 2
# Python 2, UW Continuum College, Written by Meghan Thréinfhir
# Marrowbone2-001-refactoring/ main.py


# REFACTORING: import locations and player from the game folder
from game import locations, player


# display the intro and get the player's name
def intro():

    # open the intro text file for reading
    with open("assets/intro.txt", "r") as f:

        # loop through each line in the file
        for line in f:

            # remove extra whitespace and print each line
            print(line.strip())

    # REFACTORING: player_name now lives in player.py
    # use player.player_name because player refers to player.py
    # and player_name is the variable inside that file
    player.player_name = input("What is your name, adventurer? > ")

    # welcome the player using their name from player.py
    print(f"Welcome, {player.player_name}. Your quest begins now...")


# control the main flow of the game
def main():

    # run the intro
    intro()

    # start the player at the dock
    current_location = "dock"

    # keep running locations until a location returns "end"
    while current_location != "end":

        # REFACTORING: location functions now live in locations.py
        # the first locations refers to the locations.py file we imported
        # the second locations refers to the dictionary named locations inside that file
        # current_location finds the matching function in that dictionary
        # () runs the function and the return value becomes the new current_location
        current_location = locations.locations[current_location]()

    # run after the game loop ends
    print("\nGame Over")


# run main() only when this file is started directly
if __name__ == "__main__":
    main()