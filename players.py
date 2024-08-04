# Slicing a list
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])

# Output the second third and fourth , start index at 1
# print(players[1:4])

# Output the third item to the last, start with index 2 and omit the second index
# print(players[2:])

# Output the last three players
# print(players[-3:]) 

# Adding third value to indicate how many to skip between items
# print(players[1:4:2])

# Looping through a slice
# print("Here are the first three players on my team:")
# for player in players[:3]:
#    print(player.title())

# Copying a list
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# Add new food to each list
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# 4-10 Slices
# my_foods = ['pizza', 'falafel', 'carrot cake', 'mac&cheese', 'pie']

# The first three items
# print("The first three items in the list are")
# print(my_foods[:3])

# Three items from the middle
# print("Three items from the middle of the list")
# print(my_foods[1:4])

# Last three items
# print("The last three items in the list are:")
# print(my_foods[-3:])

# 4-11 My Pizzas, You Pizzas
# pizzas = ['pepperoni', 'vegatarian', 'margherita']
# friends_pizzas = pizzas[:]
# Add new pizza to list
# pizzas.append('sausage')
# friends_pizzas.append('breakfast')

# print('My favorite pizzas are:')
# for pizza in pizzas:
#    print(pizza.title())

# print("My friend's favorite pizzas are:")
# for friend_pizza in friends_pizzas:
#    print(friend_pizza.title())

# 4-12 More loops
foods = ['pizza', 'falafel', 'carrot cake', 'mac&cheese', 'pie']
print("These are my favorite foods:")
for food in foods:    
    print(food.title())