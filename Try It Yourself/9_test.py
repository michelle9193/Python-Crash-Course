# # 9-1 Restaurant
# class Restaurant:
#     """Model a restaurant"""

#     def __init__(self, restaurant_name, cuisine_type):
#         "Initialize name and cuisine type attributes"
#         self.name = restaurant_name.title()
#         self.type = cuisine_type

#     def describe_restaurant(self):
#         """Describe a restaurant"""
#         message = f"{self.name} serves the best {self.type}."
#         print(f"\n{message}")

#     def open_restaurant(self):
#         """Show the working hours of a restaurant"""
#         message = f"{self.name} is open til late!"
#         print(f"\n{message}")

# # Make an instance called restaurant from the class
# restaurant = Restaurant('spur', 'steak')
# print(restaurant.name)
# print(restaurant.type)

# # Calling methods
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# # 9-2 Three Restaurants
# class Restaurant:
#     """Model a restaurant"""

#     def __init__(self, restaurant_name, cuisine_type):
#         "Initialize name and cuisine type attributes"
#         self.name = restaurant_name.title()
#         self.type = cuisine_type

#     def describe_restaurant(self):
#         """Describe a restaurant"""
#         message = f"{self.name} serves the best {self.type}."
#         print(f"\n{message}")

#     def open_restaurant(self):
#         """Show the working hours of a restaurant"""
#         print(f"{self.name} is now open!")

# # Make an instance called restaurant from the class
# spur = Restaurant('spur', 'steak')
# spur.describe_restaurant()

# mcds = Restaurant('mcdonalds', 'burger')
# mcds.describe_restaurant()

# kfc = Restaurant('kfc', 'fried chicken')
# kfc.describe_restaurant()

# # 9-3 Users
# class Users:
#     """This is how to add users"""

#     def __init__(self, first_name, last_name, email, location, username):
#         """Initialize a user"""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.email = email
#         self.location = location.title()
#         self.username = username

#     def describe_user(self):
#         """Print a summary of the user's information"""
#         # summary = f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nLocation: {self.location}\nUsername: {self.username}"
#         # print(f"\n{summary}")
#         print(f"\n{self.first_name} {self.last_name}")
#         print(f"{self.email}")
#         print(f"{self.location}")
#         print(f"{self.username}")

#     def greet_user(self):
#         """A personalize greeting to the user"""
#         greeting = f"Hello, {self.first_name} {self.last_name}!"
#         print(f"\n{greeting}")

# # Make an instance called users from the class
# michelle = Users('michelle', 'scholtz', 'michelle@yahoo.com', 'cape town', 'michelle003')
# michelle.describe_user()
# michelle.greet_user()

# gershwin = Users('gershwin', 'scholtz', 'gscholtz@hotmail.com', 'langebaan', 'gdog99')
# gershwin.describe_user()
# gershwin.greet_user()

# # 9-4 Number Served
# class Restaurant:
#     """Model a restaurant"""

#     def __init__(self, restaurant_name, cuisine_type):
#         "Initialize name and cuisine type attributes"
#         self.name = restaurant_name.title()
#         self.type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """Describe a restaurant"""
#         message = f"{self.name} serves the best {self.type}."
#         print(f"\n{message}")

#     def open_restaurant(self):
#         """Show the working hours of a restaurant"""
#         message = f"{self.name} is open til late!"
#         print(f"\n{message}")

#     def read_number_served(self):
#         """Print how many customers are being served"""
#         print(f"We are serving {self.number_served} customers.")

#     def set_number_served(self, number_served):
#         """
#         Set the number of customers served to the given value.
#         Reject the change if it attempts to descrease the number served.
#         """
#         if number_served >= self.number_served:
#             self.number_served = number_served
#         else:
#             print("You can't decrease number served")

#     def increment_number_served(self, served):
#         """Add the given amount to the customers served."""
#         self.number_served += served

# # Make an instance called restaurant from the class
# restaurant = Restaurant('spur', 'steak')
# # print(restaurant.name)
# # print(restaurant.type)

# # Print number of customers the restaurant has served.
# restaurant.read_number_served()
# # Change the value and print again
# restaurant.number_served = 23
# restaurant.read_number_served()
# # Set number served
# restaurant.set_number_served(50)
# restaurant.read_number_served()
# # Increment how many guests were served
# restaurant.increment_number_served(100)
# restaurant.read_number_served()

# # 9-5 Login Attempts
# class Users:
#     """This is how to add users"""

#     def __init__(self, first_name, last_name, email, location, username):
#         """Initialize a user"""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.email = email
#         self.location = location.title()
#         self.username = username
#         self.login_attempts = 0

#     def describe_user(self):
#         """Print a summary of the user's information"""
#         # summary = f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nLocation: {self.location}\nUsername: {self.username}"
#         # print(f"\n{summary}")
#         print(f"\n{self.first_name} {self.last_name}")
#         print(f"{self.email}")
#         print(f"{self.location}")
#         print(f"{self.username}")

#     def greet_user(self):
#         """A personalize greeting to the user"""
#         greeting = f"Hello, {self.first_name} {self.last_name}!"
#         print(f"\n{greeting}")

#     def increment_login_attempts(self):
#         """Increment the value of login attempts by 1"""
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         """Rest login attempts"""
#         self.login_attempts = 0

# # Make an instance called users from the class
# michelle = Users('michelle', 'scholtz', 'michelle@yahoo.com', 'cape town', 'michelle003')
# michelle.describe_user()
# michelle.greet_user()

# print("\nMaking Login Attempts... ")
# michelle.increment_login_attempts()
# michelle.increment_login_attempts()
# michelle.increment_login_attempts()
# print(f"  Login attempts: {michelle.login_attempts}")

# print("\nReset login attempts...")
# michelle.reset_login_attempts()
# print(f"  Login reset: {michelle.login_attempts}")

# 9-6 Ice Cream Stand
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
    
    def IceCreamStand(Restaurant):
        """Respect an ice cream stand specific to a certain restaurant."""
        


# Make an instance called restaurant from the class
restaurant = Restaurant('spur', 'steak')
# print(restaurant.name)
# print(restaurant.type)

# Print number of customers the restaurant has served.
restaurant.read_number_served()
# Change the value and print again
restaurant.number_served = 23
restaurant.read_number_served()
# Set number served
restaurant.set_number_served(50)
restaurant.read_number_served()
# Increment how many guests were served
restaurant.increment_number_served(100)
restaurant.read_number_served()