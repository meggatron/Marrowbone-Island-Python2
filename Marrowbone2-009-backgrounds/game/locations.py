# Marrowbone2-009-backgrounds/game/locations.py

import random

from game import gui, player, audio
from game.creatures import GiantShrimp


weather = ["foggy", "rainy", "sunny"]


def log_room(location):
    with open("assets/log.txt", "a") as log:
        log.write(f"Entered {location}\n")


def dock():
    log_room("dock")

    gui.display(
        f"You are on a {random.choice(weather)} dock.\n"
        "Explore Marrowbone Island."
    )

    if "compass" not in player.inventory:
        gui.display(
            "You see a compass resting on a post."
        )

        take = gui.choose(
            west="LEAVE",
            east="TAKE COMPASS"
        )

        if take == "east":
            player.inventory.append("compass")
            audio.play_sound("pickup.mp3")
            gui.display("You take the compass.")

        elif take == "west":
            gui.display("You leave the compass.")

        gui.pause(1000)
        gui.reset_player()

    else:
        gui.display(
            "The post is empty. You already took the compass."
        )
        gui.pause(1000)

    gui.display("Choose a destination.")

    move = gui.choose(
        west="BOATHOUSE",
        north="TRAIL"
    )

    if move == "west":
        gui.reset_player()
        return "boathouse"

    elif move == "north":
        gui.reset_player()
        return "trail"


def boathouse():
    log_room("boathouse")

    shrimp = GiantShrimp()

    gui.display(shrimp.describe())
    gui.pause(1000)

    gui.display(shrimp.speak())
    gui.pause(1000)

    if "slingshot" in player.inventory:
        gui.display(
            "The shrimp waves an antenna.\n"
            "You already have the slingshot."
        )

    elif "token" in player.inventory:
        gui.display(
            "The shrimp offers a slingshot for your brass token."
        )

        trade = gui.choose(
            west="LEAVE",
            east="TRADE"
        )

        if trade == "east":
            player.inventory.remove("token")
            player.inventory.append("slingshot")

            audio.play_sound("pickup.mp3")

            gui.display(
                shrimp.give_gift()
            )

        elif trade == "west":
            gui.display(
                "The shrimp shrugs and keeps polishing the slingshot."
            )

        gui.reset_player()

    gui.pause(1000)

    gui.display("Return to the dock.")

    move = gui.choose(
        east="DOCK"
    )

    if move == "east":
        gui.reset_player()
        return "dock"


def trail():
    log_room("trail")

    gui.display(
        f"You are on a {random.choice(weather)} trail.\n"
        "The path branches across the island."
    )

    move = gui.choose(
        west="SHIPWRECK",
        east="FOREST",
        north="CLIFF",
        south="DOCK"
    )

    if move == "west":
        gui.reset_player()
        return "shipwreck"

    elif move == "east":
        gui.reset_player()
        return "forest"

    elif move == "north":
        gui.reset_player()
        return "cliff"

    elif move == "south":
        gui.reset_player()
        return "dock"


def forest():
    log_room("forest")

    gui.display(
        f"You step into a {random.choice(weather)} forest.\n"
        "The trees are thick and mossy.\n"
        "A Sasquatch watches you from behind a cedar."
    )

    if "shovel" not in player.inventory:
        gui.display(
            "The Sasquatch holds out an old shovel."
        )

        move = gui.choose(
            west="TRAIL",
            east="TAKE SHOVEL"
        )

        if move == "east":
            player.inventory.append("shovel")

            audio.play_sound("pickup.mp3")

            gui.display(
                "The Sasquatch gives you the shovel."
            )

            gui.pause(1000)
            gui.reset_player()

            return "forest"

        elif move == "west":
            gui.reset_player()
            return "trail"

    else:
        gui.display(
            "The Sasquatch nods.\n"
            "You already have the shovel."
        )

        move = gui.choose(
            west="TRAIL",
            east="TIDEPOOLS"
        )

        if move == "west":
            gui.reset_player()
            return "trail"

        elif move == "east":
            gui.reset_player()
            return "tidepools"


def tidepools():
    log_room("tidepools")

    gui.display(
        f"You reach the {random.choice(weather)} tidepools.\n"
        "Water shimmers between the rocks."
    )

    gui.display(
        "Something ancient moves beneath the surface."
    )

    move = gui.choose(
        west="FOREST"
    )

    if move == "west":
        gui.reset_player()
        return "forest"


def shipwreck():
    log_room("shipwreck")

    gui.display(
        f"You reach a {random.choice(weather)} shore.\n"
        "An old shipwreck leans against the rocks.\n"
        "A pirate waits beside the broken hull."
    )

    if "map" not in player.inventory:
        gui.display(
            "The pirate offers you an old treasure map."
        )

        take = gui.choose(
            west="LEAVE",
            east="TAKE MAP"
        )

        if take == "east":
            player.inventory.append("map")

            audio.play_sound("pickup.mp3")

            gui.display(
                "You take the pirate's map."
            )

        elif take == "west":
            gui.display(
                "The pirate keeps hold of the map."
            )

        gui.pause(1000)
        gui.reset_player()

    else:
        gui.display(
            "The pirate points toward the cliff."
        )
        gui.pause(1000)

    gui.display("Return to the trail.")

    move = gui.choose(
        east="TRAIL"
    )

    if move == "east":
        gui.reset_player()
        return "trail"


def cliff():
    log_room("cliff")

    gui.display(
        f"You reach the edge of a {random.choice(weather)} cliff.\n"
        "The wind howls through the cedar trees."
    )

    if (
        "map" in player.inventory
        and "slingshot" in player.inventory
        and "shovel" in player.inventory
    ):
        gui.pause(1000)

        gui.display(
            "You study the map.\n"
            "The X marks a hollow beneath the cedar."
        )
        gui.pause(1500)

        gui.display(
            "You use the slingshot to knock loose\n"
            "a branch above the marked ground."
        )
        gui.pause(1500)

        gui.display(
            "You use the Sasquatch's shovel to dig\n"
            "beneath the cedar roots."
        )
        gui.pause(1500)

        gui.display(
            "The shovel strikes an old metal chest."
        )
        gui.pause(1500)

        audio.play_sound("winner.mp3")

        gui.display(
            f"Congratulations {player.player_name}, "
            "you win Marrowbone Island!"
        )
        gui.pause(1500)

        return "end"

    else:
        gui.display(
            "The treasure is close... but you are not ready.\n"
            "You need the pirate's map,\n"
            "the shrimp's slingshot,\n"
            "and the Sasquatch's shovel."
        )

        move = gui.choose(
            south="TRAIL"
        )

        if move == "south":
            gui.reset_player()
            return "trail"


locations = {
    "dock": dock,
    "boathouse": boathouse,
    "trail": trail,
    "forest": forest,
    "tidepools": tidepools,
    "shipwreck": shipwreck,
    "cliff": cliff,
}