from game import gui, locations, player, audio


def main():
    gui.start()
    audio.start_audio()
    audio.play_music("ocean.mp3")

    player.player_name = gui.get_input("What is your name, adventurer?")
    gui.display(f"Welcome, {player.player_name}. Your quest begins now.")
    gui.pause(1500)

    current_location = "dock"

    while current_location != "end":
        current_location = locations.locations[current_location]()

    gui.display("Game over.")
    gui.pause(3000)
    audio.stop_music()
    gui.quit()


if __name__ == "__main__":
    main()