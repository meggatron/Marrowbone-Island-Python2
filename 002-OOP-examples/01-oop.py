# What is Object-Oriented Programming?
# 01-oop.py

class Crab:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says click click")


class Shrimp:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says blub blub")


# Create objects
crab1 = Crab("Carl")
shrimp1 = Shrimp("Sammy")

# Call methods
crab1.speak()      # Carl says click click
shrimp1.speak()    # Sammy says blub blub