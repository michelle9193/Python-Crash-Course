class Restaurant:
    """Model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        "Initialize name and cuisine type attributes"
        self.name = restaurant_name.title()
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe a restaurant"""
        message = f"{self.name} serves the best {self.type}."
        print(f"\n{message}")

    def open_restaurant(self):
        """Show the working hours of a restaurant"""
        message = f"{self.name} is open til late!"
        print(f"\n{message}")

    def read_number_served(self):
        """Print how many customers are being served"""
        print(f"We are serving {self.number_served} customers.")

    def set_number_served(self, number_served):
        """
        Set the number of customers served to the given value.
        Reject the change if it attempts to descrease the number served.
        """
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print("You can't decrease number served")

    def increment_number_served(self, served):
        """Add the given amount to the customers served."""
        self.number_served += served
    
class IceCreamStand(Restaurant):
    """Respresent an ice cream stand specific to a certain restaurant."""
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """
        Initialize attributes of the parent class
        Then initialize attributes that is specific to the ice cream stand
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display all the ice cream flavors."""
        print("We have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

# spur = IceCreamStand('Spur')
# spur.flavors = ['chocolate', 'strawberry', 'vanilla']

# spur.describe_restaurant()
# spur.show_flavors()