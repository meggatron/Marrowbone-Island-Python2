# Marrowbone Island 2
# Python 2, UW Continuum College, Written by Meghan Thréinfhir
# Marrowbone2-000-core-game.py

import random
import time


# global game data
weather = ["foggy", "rainy", "sunny"]
inventory = []


# read the introduction from intro.txt
def intro():
    with open("intro.txt", "r") as f:
        for line in f:
            print(line.strip())

    name = input("What is your name, adventurer? > ")
    print(f"Welcome, {name}. Your quest begins now...")

    return name


# record each room the player visits
def log_room(location):
    with open("log.txt", "a") as log:
        log.write(f"Entered {location}\n")


def dock():
    log_room("dock")

    print(
        f"\nYou are on a {random.choice(weather)} dock. "
        "Paths lead north to a trail or west to a boathouse."
    )

    if "compass" not in inventory:
        print("You see a compass resting on a post.")
        take = input("Take the compass? > ").lower()

        if take == "yes":
            inventory.append("compass")
            print("You tuck the compass into your coat.")
        else:
            print("You leave the compass resting on the post.")
    else:
        print("The post is empty. You already took the compass.")

    move = input("Where do you go? > ").lower()

    if move == "north" or move == "go north":
        return "trail"

    elif move == "west" or move == "go west":
        return "boathouse"

    else:
        print("Try typing 'north' or 'west'.")
        return "dock"


def trail():
    log_room("trail")

    print("\nYou begin walking up the trail.")

    for step in range(1, 4):
        print(f"Step {step}...")
        time.sleep(0.5)

    print(
        f"You are on a {random.choice(weather)} trail. "
        "Paths lead west into a forest, north to a cliff, "
        "or south back to the dock."
    )

    move = input("Where do you go? > ").lower()

    if move == "west" or move == "go west":
        return "forest"

    elif move == "south" or move == "go south":
        return "dock"

    elif move == "north" or move == "go north":
        return "cliff"

    else:
        print("Try 'west', 'north', or 'south'.")
        return "trail"


def forest():
    log_room("forest")

    print(
        f"\nYou step into a {random.choice(weather)} forest. "
        "The trees are thick and mossy."
    )

    if "map" not in inventory:
        take = input("You find a crumpled old map. Take it? > ").lower()

        if take == "yes":
            inventory.append("map")
            print("You take the map and tuck it into your coat.")
        else:
            print("You leave the map in the tree hollow.")

    else:
        print("The forest is quiet. You've already taken the map.")

    move = input("Where do you go? > ").lower()

    if move == "east" or move == "go east":
        return "trail"

    else:
        print("Try typing 'east' or 'go east'.")
        return "forest"


def cliff():
    global player_name

    log_room("cliff")

    print(f"\n{player_name}, you arrive at the edge of a steep cliff.")

    # Boolean variables
    has_map = "map" in inventory
    has_compass = "compass" in inventory

    if has_map and has_compass:
        print("The compass points toward the old cedar.")
        print("The map reveals a hidden path down the cliff.")
        print("Using both tools, you reach the buried treasure.")
        print(f"Congratulations, {player_name}! You win Marrowbone Island!")
        return "end"

    if has_map or has_compass:
        print("You have part of what you need, but not everything.")

        if not has_map:
            print("You still need to find the map in the forest.")

        if not has_compass:
            print("You still need to find the compass at the dock.")

        print("You return to the trail.")
        return "trail"

    print("You have neither the map nor the compass.")
    print("A damp note is wedged between two rocks.")
    print(
        "'You seem to have lost your way. "
        "Ask the shrimp in the laundry room for life advice,' it reads."
    )
    print("You return to the trail.")

    return "trail"


def boathouse():
    log_room("boathouse")

    print(
        f"\nYou enter a {random.choice(weather)} boathouse. "
        "The air smells like mildew and salt."
    )

    print(
        "A broken canoe leans against the wall. "
        "In the corner, a warped door leads to a small room."
    )

    move = input(
        "Do you enter the laundry room? Type 'yes' or 'no'. > "
    ).lower()

    if move == "yes":
        return "laundry_room"

    else:
        print("You return to the dock.")
        return "dock"


def laundry_room():
    log_room("laundry_room")

    actions = [
        "You open the warped door.",
        "Water seeps across the floor.",
        "A washing machine rattles in the corner.",
        "An enormous antenna rises from behind it.",
        "A giant shrimp steps into view, folding a towel.",
        "He turns to you, antennae twitching.",
        "'Would you like a poem?' he asks."
    ]

    for action in actions:
        print(action)
        time.sleep(1)

    choice = input(
        "Do you give the shrimp three words? Type 'yes' or 'no'. > "
    ).lower()

    if choice == "yes":
        noun = input("Give the shrimp a noun. > ")
        emotion = input("How do you feel today? > ")
        adjective = input("Describe the sea in one word. > ")

        print("\nThe shrimp bows and recites:\n")

        poem = [
            f"{noun} in moonlight",
            f"{emotion} flows through the tidepool",
            f"the sea is {adjective}"
        ]

        for line in poem:
            print(line)

    else:
        print("The shrimp nods solemnly and returns to his towels.")

    print("\nYou leave the laundry room.")
    return "boathouse"


# dictionary of location names mapped to functions
locations = {
    "dock": dock,
    "trail": trail,
    "forest": forest,
    "cliff": cliff,
    "boathouse": boathouse,
    "laundry_room": laundry_room
}


# start the game
player_name = intro()
current_location = "dock"


# main game loop
while current_location != "end":
    current_location = locations[current_location]()

print("\nGame Over")