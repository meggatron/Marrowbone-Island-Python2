# creatures.py
# Creature classes for Marrowbone Island

class Creature:
    def __init__(self, name, gift):
        self.name = name
        self.gift = gift

    def speak(self):
        return f"{self.name} says something mysterious."

    def give_gift(self):
        return f"{self.name} gives you a {self.gift}."

    def describe(self):
        return f"You meet {self.name}."


class GiantShrimp(Creature):
    def __init__(self):
        super().__init__("Giant Shrimp", "slingshot")

    def speak(self):
        return "The Giant Shrimp says: Got a token? I might have something for you."

    def describe(self):
        return "A Giant Shrimp sits beside a washing machine in the boathouse."


class Loowit(Creature):
    def __init__(self):
        super().__init__("Loowit the Orca", "underwater breathing")

    def speak(self):
        return "Loowit says: The tide remembers every path."

    def describe(self):
        return "Loowit the Orca surfaces in the dark water."


class Sasquatch(Creature):
    def __init__(self):
        super().__init__("Sasquatch", "magnetism")

    def speak(self):
        return "Sasquatch says: The forest pulls what it wants closer."

    def describe(self):
        return "A Sasquatch steps from behind the mossy trees."


class GhostPirate(Creature):
    def __init__(self):
        super().__init__("Ghost Pirate", "lantern")

    def speak(self):
        return "The Ghost Pirate says: Light is a map for the lost."

    def describe(self):
        return "A Ghost Pirate flickers beside the shipwreck."