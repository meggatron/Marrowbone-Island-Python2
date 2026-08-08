import random
from game import gui, player, audio
from game.creatures import GiantShrimp

weather = ["foggy", "rainy", "sunny"]


def log_room(location):
    with open("assets/log.txt", "a") as log:
        log.write(f"Entered {location}\n")


def dock():
    log_room("dock")

    gui.display(f"""
You are on a {random.choice(weather)} dock.
Paths lead north to a trail.
Paths lead east to a boathouse.
""")

    if "token" not in player.inventory and "slingshot" not in player.inventory:
        take = gui.get_input("You spot a brass token between the dock boards. \nTake it? yes/no")

        if take == "yes":
            player.inventory.append("token")
            audio.play_sound("pickup.mp3")
            gui.display("You pocket the brass token.")
            gui.pause(1000)
        else:
            gui.display("You leave the token between the boards.")
            gui.pause(1000)

    move = gui.get_input("Where do you go?")

    if move == "go north" or move == "north":
        return "trail"
    elif move == "go east" or move == "east":
        return "boathouse"
    else:
        gui.display("Try typing 'north' or 'east'.")
        gui.pause(1000)
        return "dock"


def boathouse():
    log_room("boathouse")

    shrimp = GiantShrimp()

    gui.display(shrimp.describe())
    gui.pause(1000)

    gui.display(shrimp.speak())
    gui.pause(1000)

    if "slingshot" in player.inventory:
        gui.display("The shrimp waves an antenna. You already have the slingshot.")

    elif "token" in player.inventory:
        trade = gui.get_input("The shrimp offers a slingshot for your brass token. \nTrade? yes/no")

        if trade == "yes":
            player.inventory.remove("token")
            player.inventory.append("slingshot")
            audio.play_sound("pickup.mp3")
            gui.display(shrimp.give_gift())
        else:
            gui.display("The shrimp shrugs and keeps polishing the slingshot.")

    else:
        gui.display(shrimp.speak())

    gui.pause(1000)

    move = gui.get_input("Type west to return to the dock.")

    if move == "go west" or move == "west":
        return "dock"
    else:
        gui.display("Try typing 'west'.")
        gui.pause(1000)
        return "boathouse"


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
            audio.play_sound("pickup.mp3")
            gui.display("You take the map and tuck it into your coat.")
        else:
            gui.display("You leave the map in the tree hollow.")
    else:
        gui.display("The forest is quiet. You've already taken the map.")

    gui.pause(1000)

    move = gui.get_input("Type east to return to the trail.")

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

    if "map" in player.inventory and "slingshot" in player.inventory:
        gui.pause(1000)
        gui.display("You study the map.\nThe X marks a hollow beneath the cedar.")
        gui.pause(1500)
        gui.display("You use the slingshot to knock loose \na branch above the buried chest.")
        gui.pause(1500)
        gui.display("Digging carefully, your fingers strike metal.")
        gui.pause(1500)
        audio.play_sound("winner.mp3")
        gui.display(f"Congratulations {player.player_name}, you win Marrowbone Island!")
        gui.pause(1500)
        return "end"

    else:
        gui.display("""
The chest is here... but you are not ready.
You need both the map and the shrimp's slingshot.
""")

        move = gui.get_input("Type south to return to the trail.")

        if move == "go south" or move == "south":
            return "trail"
        else:
            gui.display("Try typing 'south'.")
            gui.pause(1000)
            return "cliff"


locations = {
    "dock": dock,
    "boathouse": boathouse,
    "trail": trail,
    "forest": forest,
    "cliff": cliff,
}