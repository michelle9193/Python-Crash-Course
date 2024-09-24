# # 10-1 Learning Python
# # Write a program that reads the file and prints what you wrote.
# filename = 'learning_python.txt'

# print("Reading an entire file:")
# with open(filename) as file_object:
#     contents = file_object.read()
# print(contents)

# print("\nLooping over the lines:")
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.strip())

# print("\nStoring the lines in a list")
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

# # 10-2 Learning C
# filename = 'learning_python.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     line = line.rstrip()
#     print(line.replace('Python', 'C'))

# # 10-3 Simpler Code
# from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()

# for line in contents.splitlines():
#     print(line)

# # 10-4 Guest
# from pathlib import Path

# prompt = input("What is your name? ")
# path = Path('guest.txt')
# path.write_text(prompt)

# # 10-5 Guest Book
# from pathlib import Path

# path = Path('guest_book.txt')

# prompt = "\nHi, what's your name? "
# prompt += "\nEnter 'quit' if you're the last guest. "

# guest_names = []
# while True:
#     name = input(prompt)
#     if name == 'quit':
#         break

#     print(f"Thanks {name}, we'll add you to the guest book.")
#     guest_names.append(name)

# # Build a string where "\n" is added after each name.
# file_string = ''
# for name in guest_names:
#     file_string += f"{name}\n"

# path.write_text(file_string.strip())

# # 10-6 Addition
# print("Give me two numbers, and I'll add them.")

# first_number = input("\nFirst number: ")
# second_number = input("Second number: ")
# try:
#     answer = int(first_number) + int(second_number)
# except ValueError:
#     print("Enter a valid number!")
# else:   
#     print(answer)

# # 10-7 Addition Calculator
# print("Give me two numbers, and I'll add them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) + int(second_number)
#     except ValueError:
#         print("Enter a valid number!")
#     else:   
#         print(answer)

# # 10-8 Cats and Dogs
# from pathlib import Path

# path = Path('cats.txt')
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry, the file {path} does not exist.")
# else:
#     # Count the approximate number of words in the file:
#     print(contents)
# from pathlib import Path

# path = Path('dogs.txt')

# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry, the file {path} does not exist.")
# else:
#     # Count the approximate number of words in the file:
#     print(contents)

# # 10-9 Silent Cats and Dogs
# from pathlib import Path

# path = Path('cats.txt')
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     pass
# else:
#     # Count the approximate number of words in the file:
#     print(contents)
# from pathlib import Path

# path = Path('dog.txt')

# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     pass
# else:
#     # Count the approximate number of words in the file:
#     print(contents)

# 10-10 Common Words
# from pathlib import Path

# path = Path('gutenberg.txt')
# try:
#     contents = path.read_text(encoding='utf-8')
#     read = contents.lower().count('the')
# except FileNotFoundError:
#     print(f"Sorry, the file {path} does not exist.")
# else:
#     # Count the approximate number of words in the file:
#     print(read)

# # Correct way of writing the 10-10 exercise
# from pathlib import Path

# def count_common_words(filename, word):
#     """Count how many times a specific word appears in the text."""
#     path = Path(filename)
#     try:
#         contents = path.read_text()
#     except FileNotFoundError:
#         pass
#     else:
#         word_count = contents.lower().count(word)
#         msg = f"'{word}' appears in {filename} about {word_count} times."
#         print(msg)

# filename = 'alice.txt'
# count_common_words(filename, 'the')

# # 10-11 Favorite Number
# # Prompt for favorite number
# from pathlib import Path
# import json

# favorite_number = input("What is your favorite number? ")

# path = Path('favorite_number.json')
# contents = json.dumps(favorite_number)
# path.write_text(contents)

# print("Thanks! I'll remember that.")

# # Read the value and print a message
# from pathlib import Path
# import json

# path = Path('favorite_number.json')
# contents = path.read_text()
# number = json.loads(contents)

# print(f"I know your favorite number! It's {number}!")

# # 10-12 Favorite Number Remebered
# from pathlib import Path
# import json

# path = Path('favorite_number.json')
# if path.exists():
#     contents = path.read_text()
#     favorite_number = json.loads(contents)
#     print(f"I know your favorite number! It's {favorite_number}!")
# else:
#     favorite_number = input("What is your favorite number? ")
#     contents = json.dumps(favorite_number)
#     path.write_text(contents)
#     print(f"We'll rememeber you when you come back, {favorite_number}!")

# # Excercise Solution
# from pathlib import Path
# import json

# path = Path('favorite_number.json')
# try:
#     contents = path.read_text()
# except FileNotFoundError:
#     number = input("What's your favorite number? ")
#     contents = json.dumps(number)
#     path.write_text(contents)
#     print("Thanks, I'll remember that!")
# else:
#     number = json.loads(contents)
#     print(f"I know your favorite number! It's {number}!")

# 10-13 User Dictionary
# add two or more pieces of information about the user
# Store all information in a dictionary
# from pathlib import Path
# import json

# path = Path('username.json')
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}!")
# else:
#     username = input("What is your name? ")
#     location = input("What is your location? ")
#     horoscope = input("What is your star-sign? ")
#     dictionary = {
#         'username': username,
#         'location': location,
#         'horoscope': horoscope,
#         }
#     contents = json.dumps(dictionary)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")

# # Second solution
# from pathlib import Path
# import json

# def get_stored_user_info(path):
#     """Get stored username if available."""
#     if path.exists():
#         contents = path.read_text()
#         user_dict = json.loads(contents)
#         return user_dict
#     else:
#         return None

# def get_new_user_info(path):
#     """Get information from a new user."""
#     username = input("What is your name? ")
#     location = input("What is your location? ")
#     animal = input("What is your favorite animal? ")

#     user_dict = {
#         'username': username,
#         "location": location,
#         "animal": animal,
#     }

#     contents = json.dumps(user_dict)
#     path.write_text(contents)
#     return user_dict

# def greet_user():
#     """Greet the user by name, and state what we know about them."""
#     path = Path('user_info.json')
#     user_dict = get_stored_user_info(path)  
#     if user_dict:
#         print(f"Welcome back, {user_dict['username']}!")
#         print(f"Lovely weather in {user_dict['location']}")
#         print(f"I see that you like {user_dict['animal']}")

#     else:
#         user_dict = get_new_user_info(path)
#         msg = f"We'll remember you when you come back, {user_dict['username']}!"
#         print(msg)

# greet_user()

# # 10-14 Verify User
# from pathlib import Path
# import json

# def get_stored_username(path):
#     """Get stored username if available."""
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         return None

# def get_new_username(path):
#     """Prompt for a new username."""
#     username = input("What is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     return username

# def get_current_username(path):
#     """Check if current user is the last person to use the program."""
#     current_user = input("What is your name? ")
#     contents = json.dumps(current_user)
#     path.write_text(contents)
#     return current_user

# def greet_user():
#     """Greet the user by name."""
#     path = Path('username.json')
#     username = get_stored_username(path)
#     current_user = get_current_username(path)
#     if username == current_user:
#         print(f"Welcome back, {username}!")
#     else:
#         print(f"We'll remember you when you come back, {current_user}!")

# # Cleaner version of greet_user()
# def greet_user():
#     """Greet the user by name."""
#     path = Path('username.json')
#     username = get_stored_username(path)
#     if username:
#         correct = input(f"Are you {username}? (y/n) ")
#         if correct == 'y':
#             print(f"Welcome back, {username}!")
#             return
#     # We got a username, but it's not correct.
#     # Prompt for a new username.
#     username = get_new_username(path)
#     print(f"We'll remember you when you come back, {username}!")
# greet_user()