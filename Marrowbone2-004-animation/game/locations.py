import random
from game import gui, player

weather = ["foggy", "rainy", "sunny"]


def log_room(location):
    with open("assets/log.txt", "a") as log:
        log.write(f"Entered {location}\n")


def dock():
    log_room("dock")

    gui.display(f"""
You are on a {random.choice(weather)} dock.
Paths lead north to a trail.
""")

    move = gui.get_input("Where do you go?")

    if move == "go north" or move == "north":
        return "trail"
    else:
        gui.display("Try typing 'go north'.")
        gui.pause(1000)
        return "dock"


def trail():
    log_room("trail")

    gui.display("You begin walking up the trail.")
    gui.pause(1000)

    gui.display(f"""
You are on a {random.choice(weather)} trail.
Paths lead west into a forest,
north to a cliff,
or south back to the dock.
""")

    move = gui.get_input("Where do you go?")

    if move == "go west" or move == "west":
        return "forest"
    elif move == "go north" or move == "north":
        return "cliff"
    elif move == "go south" or move == "south":
        return "dock"
    else:
        gui.display("Try 'west', 'north', or 'south'.")
        gui.pause(1000)
        return "trail"


def forest():
    log_room("forest")

    gui.display(f"""
You step into a {random.choice(weather)} forest.
The trees are thick and mossy.
""")

    if "map" not in player.inventory:
        take = gui.get_input("You find a crumpled old map. Take it? yes/no")

        if take == "yes":
            player.inventory.append("map")
            gui.display("You take the map and tuck it into your coat.")
        else:
            gui.display("You leave the map in the tree hollow.")
    else:
        gui.display("The forest is quiet. You've already taken the map.")

    gui.pause(1000)

    move = gui.get_input("You can go east to return to the trail.")

    if move == "go east" or move == "east":
        return "trail"
    else:
        gui.display("Try typing 'east'.")
        gui.pause(1000)
        return "forest"


def cliff():
    log_room("cliff")

    gui.display(f"""
You reach the edge of a {random.choice(weather)} cliff.
A strange chest is buried here.
""")

    if "map" in player.inventory:
        gui.pause(1000)
        gui.display("You study the map. \nThe X marks a hollow beneath the cedar.")
        gui.pause(1500)
        gui.display("Digging carefully, your fingers strike metal.")
        gui.pause(1500)
        gui.display(f"Congratulations {player.player_name}, you win Marrowbone Island!")
        gui.pause(1500)
        return "end"

    else:
        gui.display("The chest is here... but without the map, its meaning is lost.")
        move = gui.get_input("Go south to return to the trail.")

        if move == "go south" or move == "south":
            return "trail"
        else:
            gui.display("Try typing 'south'.")
            gui.pause(1000)
            return "cliff"


locations = {
    "dock": dock,
    "trail": trail,
    "forest": forest,
    "cliff": cliff,
}