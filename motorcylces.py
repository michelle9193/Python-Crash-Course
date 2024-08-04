# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# Modifying elements in a list
# motorcycles[0] = ('ducati')
# print(motorcycles)

# Appending elements to the end of a list
# motorcycles.append('ducati')
# print(motorcycles)

# Appending elements in an empty list
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suziki')

# print(motorcycles)

# Inserting elements in a list (takes 2 parameters - the index and the value)
# Insert shifts every other value in the list one position to the right
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducti')
# print(motorcycles)

# Removing elements from a list
# You need to know the position/ index of the item 
# Once del is used, you can no longer access the value
# motorcycles = ['honda', 'yamaha', 'suzuki']
# del motorcycles[0]
# print(motorcycles)

# Removing (the last) item using the pop() method
# Pop() allows you to use the value after you remove it from a list
# motorcycles = ['honda', 'yamaha', 'suzuki']
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# Popping items from any position in a list
# Include the index of the item
# motorcycles = ['honda', 'yamaha', 'suzuki']
# first_owned = motorcycles.pop(0)
# print(f"The first motorcyle I owned was a {first_owned.title()}.")

# Removing an item by value
# Used when you do not know the position of the value you want to remove 
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

# You can use the value from the remove() method
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(too_expensive)
# print(f"\nA {too_expensive.title()} is too expensive")