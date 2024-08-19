# Creating and Using a Class
# Creating the Dog Class
# Each instance created from the Dog class will store a name and an age, and
# we’ll give each dog the ability to sit() and roll_over():
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Making an Instance of a Class
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling Methods
my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances