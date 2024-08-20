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