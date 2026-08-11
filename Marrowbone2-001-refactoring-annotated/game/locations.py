# game/locations.py

# import Python's built-in random module
import random

# import Python's built-in time module
import time

# REFACTORING: import player.py from the game folder
# player refers to the player.py file
from game import player


# possible weather descriptions used by multiple locations
weather = ["foggy", "rainy", "sunny"]


# record each location the player enters
def log_room(location):

    # open log.txt in append mode so new entries are added instead of replacing old ones
    with open("assets/log.txt", "a") as log:

        # write the current location to the log file
        log.write(f"Entered {location}\n")


# handle everything that happens at the dock
def dock():

    # record that the player entered the dock
    log_room("dock")

    # choose random weather and describe the available paths
    print(
        f"\nYou are on a {random.choice(weather)} dock. "
        "Paths lead north to a trail or west to a boathouse."
    )

    # REFACTORING: inventory now lives in player.py
    # check whether "compass" is NOT already in the player's inventory
    if "compass" not in player.inventory:

        print("You see a compass resting on a post.")

        # ask whether the player wants to take the compass
        take = input("Take the compass? > ").lower()

        # add the compass if the player types yes
        if take == "yes":

            # REFACTORING: change the inventory list stored in player.py
            player.inventory.append("compass")

            print("You tuck the compass into your coat.")

        else:
            print("You leave the compass resting on the post.")

    # this runs if the compass is already in the inventory
    else:
        print("The post is empty. You already took the compass.")

    # ask where the player wants to go next
    move = input("Where do you go? > ").lower()

    # return the name of the next location to main.py
    if move == "north" or move == "go north":
        return "trail"

    elif move == "west" or move == "go west":
        return "boathouse"

    # stay at the dock if the input does not match an available direction
    else:
        print("Try typing 'north' or 'west'.")
        return "dock"


# handle everything that happens on the trail
def trail():

    # record that the player entered the trail
    log_room("trail")

    print("\nYou begin walking up the trail.")

    # repeat the walking message three times
    for step in range(1, 4):
        print(f"Step {step}...")

        # pause for half a second between steps
        time.sleep(0.5)

    # choose random weather and describe the available paths
    print(
        f"You are on a {random.choice(weather)} trail. "
        "Paths lead west into a forest, north to a cliff, "
        "or south back to the dock."
    )

    # ask where the player wants to go next
    move = input("Where do you go? > ").lower()

    # return the matching location name to main.py
    if move == "west" or move == "go west":
        return "forest"

    elif move == "south" or move == "go south":
        return "dock"

    elif move == "north" or move == "go north":
        return "cliff"

    # stay on the trail if the input does not match an available direction
    else:
        print("Try 'west', 'north', or 'south'.")
        return "trail"


# handle everything that happens in the forest
def forest():

    # record that the player entered the forest
    log_room("forest")

    # choose random weather and describe the forest
    print(
        f"\nYou step into a {random.choice(weather)} forest. "
        "The trees are thick and mossy."
    )

    # REFACTORING: inventory now lives in player.py
    # check whether the map is already in the player's inventory
    if "map" not in player.inventory:

        # ask whether the player wants to take the map
        take = input("You find a crumpled old map. Take it? > ").lower()

        if take == "yes":

            # REFACTORING: change the inventory list stored in player.py
            player.inventory.append("map")

            print("You take the map and tuck it into your coat.")

        else:
            print("You leave the map in the tree hollow.")

    # this runs if the map is already in the inventory
    else:
        print("The forest is quiet. You've already taken the map.")

    # ask where the player wants to go next
    move = input("Where do you go? > ").lower()

    # return the trail if the player moves east
    if move == "east" or move == "go east":
        return "trail"

    # stay in the forest for any other input
    else:
        print("Try typing 'east' or 'go east'.")
        return "forest"


# handle everything that happens at the cliff
def cliff():

    # record that the player entered the cliff
    log_room("cliff")

    # REFACTORING: player_name now lives in player.py
    print(f"\n{player.player_name}, you arrive at the edge of a steep cliff.")

    # REFACTORING: inventory now lives in player.py
    # store the inventory checks as Boolean values
    has_map = "map" in player.inventory
    has_compass = "compass" in player.inventory

    # both conditions must be True to win
    if has_map and has_compass:

        print("The compass points toward the old cedar.")
        print("The map reveals a hidden path down the cliff.")
        print("Using both tools, you reach the buried treasure.")

        # REFACTORING: get the player's name from player.py
        print(
            f"Congratulations, {player.player_name}! "
            "You win Marrowbone Island!"
        )

        # return end to stop the main game loop
        return "end"

    # at least one of these conditions must be True
    if has_map or has_compass:

        print("You have part of what you need, but not everything.")

        # tell the player which item is missing
        if not has_map:
            print("You still need to find the map in the forest.")

        if not has_compass:
            print("You still need to find the compass at the dock.")

        print("You return to the trail.")

        # send the player back to the trail
        return "trail"

    # this section runs if the player has neither item
    print("You have neither the map nor the compass.")
    print("A damp note is wedged between two rocks.")

    print(
        "'You seem to have lost your way. "
        "Ask the shrimp in the laundry room for life advice,' it reads."
    )

    print("You return to the trail.")

    # send the player back to the trail
    return "trail"


# handle everything that happens in the boathouse
def boathouse():

    # record that the player entered the boathouse
    log_room("boathouse")

    # choose random weather and describe the boathouse
    print(
        f"\nYou enter a {random.choice(weather)} boathouse. "
        "The air smells like mildew and salt."
    )

    print(
        "A broken canoe leans against the wall. "
        "In the corner, a warped door leads to a small room."
    )

    # ask whether the player wants to enter the laundry room
    move = input(
        "Do you enter the laundry room? Type 'yes' or 'no'. > "
    ).lower()

    # move to the laundry room if the player says yes
    if move == "yes":
        return "laundry_room"

    # otherwise return to the dock
    else:
        print("You return to the dock.")
        return "dock"


# handle everything that happens in the laundry room
def laundry_room():

    # record that the player entered the laundry room
    log_room("laundry_room")

    # store the sequence of actions in a list
    actions = [
        "You open the warped door.",
        "Water seeps across the floor.",
        "A washing machine rattles in the corner.",
        "An enormous antenna rises from behind it.",
        "A giant shrimp steps into view, folding a towel.",
        "He turns to you, antennae twitching.",
        "'Would you like a poem?' he asks."
    ]

    # print each action one at a time
    for action in actions:
        print(action)

        # pause for one second between actions
        time.sleep(1)

    # ask whether the player wants the shrimp to make a poem
    choice = input(
        "Do you give the shrimp three words? Type 'yes' or 'no'. > "
    ).lower()

    if choice == "yes":

        # collect three words from the player
        noun = input("Give the shrimp a noun. > ")
        emotion = input("How do you feel today? > ")
        adjective = input("Describe the sea in one word. > ")

        print("\nThe shrimp bows and recites:\n")

        # create a poem using the player's input
        poem = [
            f"{noun} in moonlight",
            f"{emotion} flows through the tidepool",
            f"the sea is {adjective}"
        ]

        # print each line of the poem
        for line in poem:
            print(line)

    # this runs if the player does not want a poem
    else:
        print("The shrimp nods solemnly and returns to his towels.")

    print("\nYou leave the laundry room.")

    # return to the boathouse
    return "boathouse"


# REFACTORING: location functions are now stored together in locations.py
# the keys are the location names returned by each function
# the values are the functions that should run for those locations
# there are no () after the function names because we are storing the functions, not running them yet
locations = {
    "dock": dock,
    "trail": trail,
    "forest": forest,
    "cliff": cliff,
    "boathouse": boathouse,
    "laundry_room": laundry_room
}