# # Importing Multiple Classes from a Module
# from car import Car, ElectricCar

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# # Importing an Entire Module
# import car

# my_mustang = car.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# Importing All Classes from a Module - NOT RECOMMENDED
# from module_name import *

# Importing a Module into a Module
from car import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Using Aliases
from electric_car import ElectricCar as EC
my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Giving a module an alias
import electric_car as ec
my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())