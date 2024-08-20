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

# # 9-Three Restaurants
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