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