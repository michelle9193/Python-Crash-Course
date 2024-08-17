# # 8-1 Message 
# def display_message():
#     """What I am learning in this chapter"""
#     print("I am learning about functions in chapter 8.")

# display_message()

# # 8-2 Favorite Book
# def favorite_book(title):
#     """One of my favorite books"""
#     print(f"One of my favorite books is {title.title()}!")

# favorite_book("python crash course")

# # 8-3 T-Shirt
# def make_shirt(tshirt_size):
#     """Display shirt size"""
#     print(f"I need a {tshirt_size} size t-shirt, please!")

# # Positional argument
# # make_shirt("medium")
# # Keyword argument
# make_shirt(tshirt_size='medium')

# # 8-4 Large Shirts
# def make_shirt(size='large', message='I love Python'):
#     """Display shirt size"""
#     print(f"\nI need a {size} t-shirt, please!")
#     print(f"It should say '{message}'!")

# make_shirt()
# make_shirt('medium')
# make_shirt('small', 'Programmers Rule')

# # 8-5 Cities
# def describe_city(name, country='South Africa'):
#     """Simple sentence"""
#     print(f"{name.title()} is in {country.title()}.")

# describe_city('cape town')
# describe_city('johannesburg')
# describe_city('japan','singapore')

