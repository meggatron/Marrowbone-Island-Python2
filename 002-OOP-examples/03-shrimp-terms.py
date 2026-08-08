# 03-shrimp-terms.py
# Class
# A class is a blueprint for creating objects

class Shrimp:

    # Constructor
    # __init__ runs automatically when a new object is created
    def __init__(self, name):

        # Parameter
        # 'name' is a parameter that receives a value

        # Attribute
        # An attribute is data stored in the object
        self.name = name

    # Method
    # A method is a function inside a class
    def speak(self):

        # Uses the object's attribute
        print(f"{self.name} says blub blub")


# Create an object (also called an instance)

# Argument
# "Sammy" is the argument passed into the parameter 'name'


# Call a method on the object
my_shrimp.speak()