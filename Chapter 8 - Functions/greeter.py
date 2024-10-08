# # Defining a function
# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")

# greet_user()

# # Passing Information to a Function
# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")

# greet_user('jesse')

# Using a Function with a while loop
def get_foramtted_name(first_name, last_name):
    """Return full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# # This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_foramtted_name(f_name, l_name)
#     print(f"Hello, {formatted_name}!")

# # If the user wants to quit
# while True:
#     print(f"\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_foramtted_name(f_name, l_name)
#     print(f"Hello, {formatted_name}!")