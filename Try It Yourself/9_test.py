# 9-1 Restaurant
class Restaurant:
    """Model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        "Initialize name and cuisine type attributes"
        self.name = restaurant_name.title()
        self.type = cuisine_type

    def describe_restaurant(self):
        """Describe a restaurant"""
        print(f"{self.name} has fresh flowers on display.")
        print(f"{self.name} ships in fresh lobster daily.")

    def open_restaurant(self):
        """Show the working hours of a restaurant"""
        print(f"{self.name} is now open!")

# Make an instance called restaurant from the class
the_restaurant = Restaurant('spur', 'steak')


print(f"They sell the best {the_restaurant.type}.")

# Calling methods
the_restaurant.describe_restaurant()
the_restaurant.open_restaurant()
