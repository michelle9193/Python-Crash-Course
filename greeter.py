# Writing Clear Prompts
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# Writing a prompt longer than one line. Assign the prompt to a variable and pass that variable to the input() function.
prompt = "If you share your name, we can personalize the messages you see."
# Multi-line string
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")