# 7-1 Rental Car
# car = input("What kind of car of you looking to rent? ")
# print(f"Let me check if we have a {car} available.")

# 7-2 Restaurant Seating
# group = input("How many people are in your dinner group? ")
# group = int(group)

# if group > 8:
#     print("You'll have to wait for a table.")
# else:
#     print("Your table is ready!")

# 7-3 Multiples of 10
# number = input("Pick a number.... ")
# number = int(number)

# if number % 10 == 0:
#     print(f"{number} is a multiple of 10!")
# else:
#     print("Try again!")

# 7-4 Pizza Toppings
# prompt = "\nWhich pizza topping would you like to add to your pizza?"
# prompt += "\nEnter 'quit' to exit program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# 7-5 Movie Tickets
# age = input("How old are you?")
# age = int(age)
# # If person is under the age of 3, ticket is free
# if age  < 3:
#     print("Free")
# # Age between 3 and 12, ticket is $10
# elif age < 12:
#     print("Price: $10")
# # Over age 12, ticker is $15
# else:
#     print("Price: $15")

# Three Exits
# 7-4
# Use a conditional test in the while statement to stop the loop.
# prompt = "\nWhich pizza topping would you like to add to your pizza?"
# prompt += "\nEnter 'quit' to exit program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# 7-5
# prompt = "\nHow old are you?"
# prompt += "\nPress 'quit' to exit. "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         print(prompt)
#     age = int(age)
# # If person is under the age of 3, ticket is free
#     if age  < 3:
#         print("Your ticket is free.")
#     # # Age between 3 and 12, ticket is $10
#     elif age > 3 and age < 12:
#         print("Ticket is $10")
#     # # Over age 12, ticker is $15
#     else:
#         print("Price: $15")

# Use an active variable to control how long the loop runs.
# 7-4 
# prompt = "\nWhich pizza topping would you like to add to your pizza?"
# prompt += "\nEnter 'quit' to exit program. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active == False
#     else:
#         print(message)

# 7-5 
# prompt = "\nHow old are you?"
# prompt += "\nEnter 'quit' to exit program. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active == False
# #If person is under the age of 3, ticket is free
#     elif int(message)  < 3:
#         print("Free")
# # Age between 3 and 12, ticket is $10
#     elif int(message) < 12:
#         print("Price: $10")
# # Over age 12, ticker is $15
#     else:
#         print("Price: $15")

# Use a break statement to exit the loop when the user enters a 'quit' value.

# 7-4 
# prompt = "\nWhich pizza topping would you like to add to your pizza?"
# prompt += "\nEnter 'quit' to exit program. "

# while True:
#     message = input(prompt)

#     if message == 'quit':
#         break
#     else:
#         print(message)

# 7-5 
# prompt = "\nHow old are you?"
# prompt += "\nPress 'quit' to exit. "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)
# # If person is under the age of 3, ticket is free
#     if age  < 3:
#         print("Your ticket is free.")
#     # # Age between 3 and 12, ticket is $10
#     elif age > 3 and age < 12:
#         print("Ticket is $10")
#     # # Over age 12, ticker is $15
#     else:
#         print("Price: $15")

# 7-7 Infinity
# current_number = 1
# while current_number < 10:
#     print(current_number)

# # 7-8 Deli
# sandwich_orders = ['steak', 'full house', 'tukey', 'club', 'caprese']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()

#     print(f"I made your {current_sandwich} sandwich!")
#     finished_sandwiches.append(current_sandwich)

# print("\nThe following sandwiches is ready for pick-up:")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())

# # 7-9 No Pastrami
# sandwich_orders = ['pastrami','steak', 'full house', 'pastrami', 'tukey','pastrami', 'club', 'caprese']
# print("\nWe have run out of pastrami, please choose a different sandwich.")

# while 'pastrami' in sandwich_orders:
#     pastrami = sandwich_orders.remove('pastrami')

# print(sandwich_orders)