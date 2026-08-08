# Marrowbone Island 2
# Python 2, UW Continuum College, Written by Meghan Thréinfhir
# Marrowbone2-001-refactoring/ main.py

from game import locations, player


def intro():
    with open("assets/intro.txt", "r") as f:
        for line in f:
            print(line.strip())

    player.player_name = input("What is your name, adventurer? > ")
    print(f"Welcome, {player.player_name}. Your quest begins now...")


def main():
    intro()
    current_location = "dock"

    while current_location != "end":
        current_location = locations.locations[current_location]()

    print("\nGame Over")


if __name__ == "__main__":
    main()