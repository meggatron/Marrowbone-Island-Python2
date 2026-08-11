# Marrowbone2-009-backgrounds/main.py

from game import audio, gui, locations, player


BACKGROUND_FILES = {
    "landing": "assets/images/map.png",
    "dock": "assets/images/dock.png",
    "boathouse": "assets/images/boathouse.png",
    #"trail": "assets/images/trail.png",
    #"forest": "assets/images/forest.png",
    #"shipwreck": "assets/images/shipwreck.png",
    #"tidepools": "assets/images/tidepools.png",
    #"cliff": "assets/images/cliff.png",
    "trail": None,
    "forest": None,
    "shipwreck": None,
    "tidepools": None,
    "cliff": None,
}


def main():

    gui.start()
    gui.hide_player()

    audio.start_audio()
    audio.play_music("ocean.mp3")

    # Landing page
    gui.set_background(
        BACKGROUND_FILES["landing"]
    )

    gui.display(
        "You arrive by ferry at Marrowbone Island.\n"
        "Rumors say a treasure is hidden somewhere on the island."
    )

    gui.pause(1800)

    # Get the player's name
    player.player_name = gui.get_input(
        "What is your name, adventurer?"
    )

    gui.display(
        f"Welcome, {player.player_name}.\n"
        "The ferry disappears into the fog behind you."
    )

    gui.pause(1500)

    # Transformation
    gui.display(
        "A strange light moves across the water.\n"
        "Your body begins to change."
    )

    gui.pause(1500)

    gui.display(
        "Your arms become fins.\n"
        "A black dorsal fin rises behind you."
    )

    gui.pause(1500)

    gui.display(
        "You have become an orca."
    )

    gui.pause(1800)

    # Reveal the player
    gui.show_player()

    gui.display(
        "Somewhere on Marrowbone Island, treasure is waiting."
    )

    gui.pause(1500)

    # Clear the introduction before gameplay begins
    gui.clear_text()

    current_location = "dock"

    # Main game loop
    while current_location != "end":

        gui.set_background(
            BACKGROUND_FILES[current_location]
        )

        current_location = locations.locations[
            current_location
        ]()

    # End game
    gui.display("Game over.")
    gui.pause(3000)

    audio.stop_music()
    gui.quit()


if __name__ == "__main__":
    main()