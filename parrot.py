# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# Letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end program. "

# We define message as an empty string, "", so Python has something to check the 
# first time it reaches the while line.
# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

# Using a flag
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)