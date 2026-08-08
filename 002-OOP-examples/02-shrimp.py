# 02-shrimp.py

class Shrimp:
    def __init__(self, name):
        # Data
        self.name = name

    def speak(self):
        # Action
        print(f"{self.name} says blub blub")


# Create an object
my_shrimp = Shrimp("Sammy")

# Run an action
my_shrimp.speak()