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
#         # summary = f"First Name: {self.first_name}\nLast Name: 
#         {self.last_name}\nEmail: {self.email}\nLocation: {self.location}\n
#         Username: 
#         {self.username}"
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
# michelle = Users('michelle', 'scholtz', 'michelle@yahoo.com', 'cape town', 
# 'michelle003')
# michelle.describe_user()
# michelle.greet_user()

# gershwin = Users('gershwin', 'scholtz', 'gscholtz@hotmail.com', 'langebaan', 
# 'gdog99')
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
#         # summary = f"First Name: {self.first_name}\nLast Name: 
#         {self.last_name}\nEmail: {self.email}\nLocation: 
#         {self.location}\nUsername: {self.username}"
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
# michelle = Users('michelle', 'scholtz', 'michelle@yahoo.com', 'cape town', 
# 'michelle003')
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

# # 9-6 Ice Cream Stand
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
    
# class IceCreamStand(Restaurant):
#     """Respresent an ice cream stand specific to a certain restaurant."""
#     def __init__(self, restaurant_name, cuisine_type='ice cream'):
#         """
#         Initialize attributes of the parent class
#         Then initialize attributes that is specific to the ice cream stand
#         """
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = []

#     def show_flavors(self):
#         """Display all the ice cream flavors."""
#         print("We have the following flavors available:")
#         for flavor in self.flavors:
#             print(f"- {flavor.title()}")

# spur = IceCreamStand('Spur')
# spur.flavors = ['chocolate', 'strawberry', 'vanilla']

# spur.describe_restaurant()
# spur.show_flavors()

# # 9-7 Admin
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
#         # summary = f"First Name: {self.first_name}\nLast Name: {self.last_name}
#         # \nEmail: {self.email}\nLocation: {self.location}\nUsername: 
#         # {self.username}"
#         # print(f"\n{summary}")
#         print(f"\n{self.first_name} {self.last_name}")
#         print(f"{self.email}")
#         print(f"{self.location}")
#         print(f"{self.username}")

#     def greet_user(self):
#         """A personalize greeting to the user"""
#         greeting = f"Hello, {self.first_name} {self.last_name}!"
#         print(f"\n{greeting}")

# class Admin(Users):
#     """Initialize admin privileges."""
#     def __init__(self, first_name, last_name, email, location, username):
#         """
#         Initialize attributes of the parent class.
#         Then initiliaze attributes specific to an administrator.
#         """
#         super().__init__(first_name, last_name, email, location, username)
#         self.privileges = []
    
#     def show_privileges(self):
#         """Display all the admin privileges."""
#         print("The admin has the following privileges:")
#         for privilege in self.privileges:
#             print(f"- {privilege}")

# # Make an instance called users from the class
# admin = Admin('billy', 'james', 'billy@hotmail.com', 'claremont', 
# 'admin_billy')
# admin.privileges = [ ]

# admin.describe_user()
# admin.show_privileges()

# # 9-8 Privileges
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
#         # summary = f"First Name: {self.first_name}\nLast Name: {self.last_name}
#         # \nEmail: {self.email}\nLocation: {self.location}\nUsername: 
#         # {self.username}"
#         # print(f"\n{summary}")
#         print(f"\n{self.first_name} {self.last_name}")
#         print(f"{self.email}")
#         print(f"{self.location}")
#         print(f"{self.username}")

#     def greet_user(self):
#         """A personalize greeting to the user"""
#         greeting = f"Hello, {self.first_name} {self.last_name}!"
#         print(f"\n{greeting}")

# class Privileges:
#     """Model privileges to the admin user."""
#     def __init__(self, privileges=[]):
#         """Initialize privileges attribute"""
#         self.privileges = privileges

#     def show_privileges(self):
#         """Display all the admin privileges."""
#         print(f"The admin has the following privileges: ")
#         if self.privileges:
#             for privilege in self.privileges:
#                 print(f"- {privilege}")
#         else:
#             print("- This user has no privileges.")

# class Admin(Users):
#     """Initialize admin priexcvileges."""
#     def __init__(self, first_name, last_name, email, location, username):
#         """
#         Initialize attributes of the parent class.
#         Then initiliaze attributes specific to an administrator.
#         """
#         super().__init__(first_name, last_name, email, location, username)
        
#         # Initialize an empty set of privileges.
#         self.privileges = Privileges()
    
# # Make an instance called users from the class
# billy = Admin('billy', 'james', 'billy@hotmail.com', 'claremont', 
#                         'admin_billy')
# billy.describe_user

# billy.privileges.show_privileges()

# print("\nAdding privileges:")
# billy_privileges = [
#     'can add post', 
#     'can delete post', 
#     'can ban user'
#     ]

# billy.privileges.privileges = billy_privileges
# billy.privileges.show_privileges()

# # 9-9 Battery Update
# class Car:
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

# # Instances as Attributes
# class Battery:
#     """A simple attempt to model a battery for an electric car."""
#     def __init__(self, battery_size=40):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 40:
#             range = 15
#         elif self.battery_size == 65:
#             range = 25
#         print(f"This car can go about {range} miles on a full charge.")

#     def upgrade_battery(self):
#         """Upgrade the size of the battery."""
#         self.battery_size = 65
#         """Print a statement to show the battery size has upgraded."""
#         print(f"This car has a {self.battery_size}-kWh battery.")


# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     # Overriding Methods form the Parent Class
#     def fill_gas_tank(self):
#         """Electric cars don't have gas tanks."""
#         print("This car doesn't have a gas tank!")

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()
# my_leaf.battery.upgrade_battery()
# my_leaf.battery.get_range()

# 9-10 Imported Restaurant
# Create separate file that imports Restaurant (imported_restaurant.py)

# 9-11 Imported Admin
# Start with your work from Exercise 9-8. Store the classes User, Privileges, 
# and Admin in one module. Create a separate file, make an Admin instance, and 
# call show_privileges() to show that everything is working correctly.
