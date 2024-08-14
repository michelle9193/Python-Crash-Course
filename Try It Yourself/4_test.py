# # 4-1 Pizzas
# pizzas = ['pepperoni', 'vegatarian', 'chicken and mushroom']
# for pizza in pizzas:
#     print(f"I could eat {pizza} pizza everyday!")

# print('\nThat is how much I love pizza.')

# 4-2 Animals
#animals = ['cat', 'snake', 'meerkat']
# for animal in animals:
#    print(f"A {animal} would be a great pet!")

# print("These animals don't make a sound.")

# 4-3 Counting to Twenty
# Print number from 1 to 20, inclusive
# for value in range(1, 21):
#    print(value)

# 4-4 One Million
# Make a list of numbers from one to one million and then use a for loop to 
# print the numbers
# millions = list(range(1, 1000002))
# for million in millions:
#    print(million)

# 4-5 Summing a million
# millions = list(range(1,1000002))
# print(min(millions))
# print(max(millions))
# print(sum(millions))

# 4-6 Odd Numbers
# odd_numbers = range(1, 21, 2)
# for odd_number in odd_numbers:
#    print(odd_number)

# 4-7 Threes
# threes = range(3, 31, 3)
# for three in threes:
#    print(three)

# 4-8 Cubes
# cubes = []
# for value in range(1, 11):
#    cube = value ** 3
#    cubes.append(cube)

# print(cubes)

# 4-9 Cube Comprehension
# cube = [value**3 for value in range(1,11)]
# print(cube)

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

# # 4-12 More loops
# foods = ['pizza', 'falafel', 'carrot cake', 'mac&cheese', 'pie']
# print("These are my favorite foods:")
# for food in foods:    
#     print(food.title())

# # 4-13 Buffet
# buffets = ('lobster', 'wagyu', 'sashimi', 'corn', 'potatoes')
# for buffet in buffets:
#     print(buffet)

# # Modify an item - error
# # buffets[2] = "risotto"
# # print(buffet)

# # Revised menu
# updates = ('lobster', 'crab', 'wagyu', 'sashimi', 'chicken')
# for update in updates:
#     print(update)

# 4-14 PEP 8

# 4-15 Code review
famous_person = "dalai lama"
quote = "When you\n\ttalk, you are only repeating\n\twhat you already know.\n\t"
" But if you listen, you may\n\tlearn something new."
message = f'\t{famous_person.title()} once said, "{quote}"'
print(message)