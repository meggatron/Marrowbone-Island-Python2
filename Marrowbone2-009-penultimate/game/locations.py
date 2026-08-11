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

    gui.display(
        "The giant shrimp folds a towel and looks at you.\n"
        "\"I'm from Bremerton,\" he says, for no obvious reason."
    )
    gui.pause(1200)

    gui.display(shrimp.speak())
    gui.pause(1000)

    if "slingshot" not in player.inventory:
        gui.display(
            "The shrimp holds out a slingshot."
        )

        choice = gui.choose(
            west="LEAVE",
            east="TAKE SLINGSHOT"
        )

        if choice == "east":
            player.inventory.append("slingshot")
            audio.play_sound("pickup.mp3")

            gui.display(
                shrimp.give_gift()
            )

        elif choice == "west":
            gui.display(
                "The shrimp shrugs and keeps the slingshot."
            )

        gui.pause(1000)
        gui.reset_player()

    else:
        gui.display(
            "The shrimp waves an antenna.\n"
            "You already have the slingshot."
        )
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
        "Another orca waits quietly among the rocks.\n"
        "Her name is Cedar."
    )

    gui.pause(1500)

    if "courage" not in player.inventory:
        gui.display(
            "Cedar looks toward the cliffs.\n"
            "\"You can't always see what is ahead of you,\" she says."
        )

        gui.pause(2000)

        gui.display(
            "\"That doesn't mean you stop moving.\""
        )

        gui.pause(2000)

        player.inventory.append("courage")

        gui.display(
            "You think about the cliff and whatever waits there.\n"
            "You have gained courage."
        )

        gui.pause(1500)

    else:
        gui.display(
            "Cedar looks toward the cliffs.\n"
            "\"Remember. Don't stop moving.\""
        )

        gui.pause(1500)

    gui.display("Return to the forest.")

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

        choice = gui.choose(
            west="TAKE MAP",
            east="LEAVE"
        )

        if choice == "west":
            player.inventory.append("map")
            audio.play_sound("pickup.mp3")

            gui.display(
                "You take the pirate's map."
            )

            gui.pause(1000)
            gui.reset_player()

        elif choice == "east":
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

    gui.display(
        "Return to the trail."
    )

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

    # Check that the player has the tools needed to continue.
    if not (
        "map" in player.inventory
        and "slingshot" in player.inventory
        and "shovel" in player.inventory
    ):
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

    # The player has everything needed.
    gui.pause(1000)

    gui.display(
        "You study the pirate's map.\n"
        "The X marks a hollow beneath an old cedar."
    )
    gui.pause(1500)

    gui.display(
        "Suddenly, the ground begins to shake.\n"
        "The Despair Squid rises from below the cliff."
    )
    gui.pause(2000)

    gui.display(
        "Its enormous tentacles surround you.\n"
        "For a moment, you feel completely paralyzed."
    )
    gui.pause(2000)

    # Cedar's courage helps during the final encounter.
    if "courage" in player.inventory:
        gui.display(
            "Then you remember Cedar's words:\n"
            "\"That doesn't mean you stop moving.\""
        )
        gui.pause(2000)

        gui.display(
            "You force yourself to move."
        )
        gui.pause(1500)

    else:
        gui.display(
            "You force yourself to move,\n"
            "but fear slows you down."
        )
        gui.pause(1500)

    gui.display(
        "The Despair Squid blocks the path to the treasure."
    )

    attack = gui.choose(
        west="DODGE",
        east="SLINGSHOT"
    )

    if attack == "west":
        gui.display(
            "You dodge a sweeping tentacle\n"
            "and circle around the squid."
        )

    elif attack == "east":
        gui.display(
            "You fire the slingshot.\n"
            "The stone strikes the Despair Squid in the eye!"
        )

    gui.pause(1500)

    gui.display(
        "The Despair Squid recoils and disappears\n"
        "over the edge of the cliff."
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
        f"Congratulations {player.player_name},\n"
        "you found the treasure of Marrowbone Island!"
    )

    gui.pause(3000)

    return "end"

locations = {
    "dock": dock,
    "boathouse": boathouse,
    "trail": trail,
    "forest": forest,
    "tidepools": tidepools,
    "shipwreck": shipwreck,
    "cliff": cliff,
}