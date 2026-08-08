# Marrowbone2-003-pygame-GUI/game/locations.py

import random

from game import gui, player

weather = ["foggy", "rainy", "sunny"]


def log_room(location):
    with open("assets/log.txt", "a") as log:
        log.write(f"Entered {location}\n")


def dock():
    log_room("dock")

    gui.display(
        f"You are on a {random.choice(weather)} dock.\n"
        "Paths lead north to a trail or east to a boathouse."
    )

    if "compass" not in player.inventory:
        take = gui.get_input(
            "You see a compass resting on a post.\n"
            "Take the compass? yes/no"
        )

        if take == "yes":
            player.inventory.append("compass")
            gui.display("You tuck the compass into your coat.")
            gui.pause(1000)
        else:
            gui.display("You leave the compass resting on the post.")
            gui.pause(1000)
    else:
        gui.display("The post is empty. You already took the compass.")
        gui.pause(1000)

    move = gui.get_input("Where do you go?")

    if move == "north" or move == "go north":
        return "trail"

    elif move == "west" or move == "go west":
        return "boathouse"

    else:
        gui.display("Try typing 'north' or 'west'.")
        gui.pause(1000)
        return "dock"


def trail():
    log_room("trail")

    gui.display("You begin walking up the trail.")

    for step in range(1, 4):
        gui.display(f"Step {step}...")
        gui.pause(500)

    gui.display(
        f"You are on a {random.choice(weather)} trail.\n"
        "Paths lead west into a forest, north to a cliff,\n"
        "or south back to the dock."
    )

    move = gui.get_input("Where do you go?")

    if move == "west" or move == "go west":
        return "forest"

    elif move == "south" or move == "go south":
        return "dock"

    elif move == "north" or move == "go north":
        return "cliff"

    else:
        gui.display("Try 'west', 'north', or 'south'.")
        gui.pause(1000)
        return "trail"


def forest():
    log_room("forest")

    gui.display(
        f"You step into a {random.choice(weather)} forest.\n"
        "The trees are thick and mossy."
    )

    if "map" not in player.inventory:
        take = gui.get_input(
            "You find a crumpled old map.\n"
            "Take it? yes/no"
        )

        if take == "yes":
            player.inventory.append("map")
            gui.display("You take the map and tuck it into your coat.")
        else:
            gui.display("You leave the map in the tree hollow.")

    else:
        gui.display("The forest is quiet. You've already taken the map.")

    gui.pause(1000)

    move = gui.get_input("Where do you go?")

    if move == "east" or move == "go east":
        return "trail"

    else:
        gui.display("Try typing 'east' or 'go east'.")
        gui.pause(1000)
        return "forest"


def cliff():
    log_room("cliff")

    gui.display(
        f"{player.player_name}, you arrive at the edge of a steep cliff."
    )

    has_map = "map" in player.inventory
    has_compass = "compass" in player.inventory

    if has_map and has_compass:
        gui.display(
            "The compass points toward the old cedar.\n"
            "The map reveals a hidden path down the cliff.\n"
            "Using both tools, you reach the buried treasure."
        )
        gui.pause(2000)

        gui.display(
            f"Congratulations, {player.player_name}!\n"
            "You win Marrowbone Island!"
        )
        gui.pause(1500)

        return "end"

    if has_map or has_compass:
        lines = [
            "You have part of what you need, but not everything."
        ]

        if not has_map:
            lines.append("You still need to find the map in the forest.")

        if not has_compass:
            lines.append("You still need to find the compass at the dock.")

        lines.append("You return to the trail.")

        gui.display("\n".join(lines))
        gui.pause(2000)

        return "trail"

    gui.display(
        "You have neither the map nor the compass.\n"
        "A damp note is wedged between two rocks.\n"
        "'You seem to have lost your way.\n"
        "Ask the shrimp in the laundry room for life advice,' it reads.\n"
        "You return to the trail."
    )
    gui.pause(2500)

    return "trail"


def boathouse():
    log_room("boathouse")

    gui.display(
        f"You enter a {random.choice(weather)} boathouse.\n"
        "The air smells like mildew and salt.\n\n"
        "A broken canoe leans against the wall.\n"
        "In the corner, a warped door leads to a small room."
    )

    move = gui.get_input(
        "Do you enter the laundry room?\n"
        "Type 'yes' or 'no'."
    )

    if move == "yes":
        return "laundry_room"

    else:
        gui.display("You return to the dock.")
        gui.pause(1000)
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
        gui.display(action)
        gui.pause(1000)

    choice = gui.get_input(
        "Do you give the shrimp three words?\n"
        "Type 'yes' or 'no'."
    )

    if choice == "yes":
        noun = gui.get_input("Give the shrimp a noun.")
        emotion = gui.get_input("How do you feel today?")
        adjective = gui.get_input("Describe the sea in one word.")

        poem = [
            "The shrimp bows and recites:",
            "",
            f"{noun} in moonlight",
            f"{emotion} flows through the tidepool",
            f"the sea is {adjective}"
        ]

        gui.display("\n".join(poem))
        gui.pause(3000)

    else:
        gui.display(
            "The shrimp nods solemnly and returns to his towels."
        )
        gui.pause(1500)

    gui.display("You leave the laundry room.")
    gui.pause(1000)

    return "boathouse"


locations = {
    "dock": dock,
    "trail": trail,
    "forest": forest,
    "cliff": cliff,
    "boathouse": boathouse,
    "laundry_room": laundry_room
}