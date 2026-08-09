# Marrowbone2-009-backgrounds/main.py

from game import audio, gui, locations, player


BACKGROUND_FILES = {
    "dock": "assets/images/dock.png",
    "boathouse": "assets/images/boathouse.png",
    "trail": "assets/images/trail.png",
    "forest": "assets/images/forest.png",
    "shipwreck": "assets/images/shipwreck.png",
    "tidepools": "assets/images/tidepools.png",
    "cliff": "assets/images/cliff.png",
}


def main():

    gui.start()

    audio.start_audio()
    audio.play_music("ocean.mp3")

    player.player_name = gui.get_input(
        "What is your name, adventurer?"
    )

    gui.display(
        f"Welcome, {player.player_name}. Your quest begins now."
    )
    gui.pause(1500)

    current_location = "dock"

    while current_location != "end":
        # Change the background before running the location
        gui.set_background(
            BACKGROUND_FILES[current_location]
        )

        current_location = locations.locations[current_location]()

    gui.display("Game over.")
    gui.pause(3000)

    audio.stop_music()
    gui.quit()


if __name__ == "__main__":
    main()