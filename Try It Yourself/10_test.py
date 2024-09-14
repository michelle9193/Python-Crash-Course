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

# 10-9 Silent Cats and Dogs
from pathlib import Path

path = Path('cats.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    pass
else:
    # Count the approximate number of words in the file:
    print(contents)
from pathlib import Path

path = Path('dog.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    pass
else:
    # Count the approximate number of words in the file:
    print(contents)