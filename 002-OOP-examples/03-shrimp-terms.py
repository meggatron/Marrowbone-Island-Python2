# 03-shrimp-terms.py


# CLASS
# a class is a blueprint for creating objects
class Shrimp:

    # CONSTRUCTOR
    # __init__ runs automatically when a new object is created
    def __init__(self, name):

        # PARAMETER
        # name is a parameter that receives a value

        # ATTRIBUTE
        # an attribute is data stored in the object
        self.name = name

    # METHOD
    # a method is a function inside a class
    def speak(self):

        # use the object's attribute
        print(f"{self.name} says blub blub")


# OBJECT / INSTANCE
# create an object from the Shrimp class

# ARGUMENT
# "Sammy" is the argument passed into the parameter name
my_shrimp = Shrimp("Sammy")


# METHOD CALL
# call the speak method on the object
my_shrimp.speak()