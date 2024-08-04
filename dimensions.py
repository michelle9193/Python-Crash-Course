# Tuples use parenthesis () instead of square brackets []
dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# Try to change one of the items
# Error
# dimensions[0] = 250

# Looping through all values in a tuple
# for dimension in dimensions:
#    print(dimension)

# You can assign a new value to a tuple
# print("Original dimensions:")
# for dimension in dimensions:
#    print(dimension)

# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)

# 4-13 Buffet
buffets = ('lobster', 'wagyu', 'sashimi', 'corn', 'potatoes')
for buffet in buffets:
    print(buffet)

# Modify an item - error
# buffets[2] = "risotto"
# print(buffet)

# Revised menu
updates = ('lobster', 'crab', 'wagyu', 'sashimi', 'chicken')
for update in updates:
    print(update)
