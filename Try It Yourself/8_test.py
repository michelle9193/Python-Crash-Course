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

# # 8-6 City Names
# def city_country(city, country):
#     """Return city and country name"""
#     get_city_country = f'"{city}, {country}"'
#     return get_city_country.title()

# formatted_string = city_country('cape town', 'south africa')
# print(formatted_string)

# formatted_string = city_country('london', 'england')
# print(formatted_string)

# formatted_string = city_country('brisbane', 'australia')
# print(formatted_string)

# # 8-7 Album
# def make_album(artist_name, album_name):
#     """A dictionary that returns artist details"""
#     artist_details = {
#         'artist': artist_name, 
#         'album': album_name,
#         }
    
#     return artist_details

# # Make three dictionaries representing different albums
# artist_info = make_album('taylor swift', 'folklore')
# print(artist_info)

# artist_info = make_album('maren morris', 'girl')
# print(artist_info)

# artist_info = make_album('ariana grande', 'eternal sunshine')
# print(artist_info)

# # With tracks
# def make_album(artist_name, album_name, songs=None):
#     """A dictionary that returns artist details"""

#     artist_details = {
#         'artist': artist_name.title(), 
#         'album': album_name.title(),
#         }
    
#     if songs:
#         artist_details['songs'] = songs
#     return artist_details

# artist_info = make_album('taylor swift', 'folklore')
# print(artist_info)

# artist_info = make_album('maren morris', 'girl')
# print(artist_info)

# artist_info = make_album('ariana grande', 'eternal sunshine')
# print(artist_info)

# artist_info = make_album('heritage singers', 'forgiven', 13)
# print(artist_info)

# # 8-9 Messages
# def show_messages(messages):
#     """A list containing a series of short text messages"""
#     for message in messages:
#         return message

# the_message = ['i love you', 'what are we having for dinner', 'please pick up some '
#            'milk']
# print(the_message)

# # 8-10 Sending messages
# def show_messages(messages):
#     """A list containing a series of short text messages"""
#     print("Show all messages:")
#     for message in messages:
#         print(message)
    
# def send_messages(messages, sent_messages):
#     """Print each message and then move it to sent_messages"""
#     print("\nSending all messages:")
#     while messages:
#         current_message = messages.pop()
#         print(current_message)
#         sent_messages.append(current_message)

# messages = ['i love you', 'what are we having for dinner', 'please pick up some'
# ' milk']
# show_messages(messages)

# sent_messages = []
# send_messages(messages, sent_messages)

# # Display both lists
# print("\nFinal list:")
# print(messages)
# print(sent_messages)

# # 8-11 Archived messages
# def show_messages(messages):
#     """A list containing a series of short text messages"""
#     print("Show all messages:")
#     for message in messages:
#         print(message)
    
# def send_messages(messages, sent_messages):
#     """Print each message and then move it to sent_messages"""
#     print("\nSending all messages:")
#     while messages:
#         current_message = messages.pop()
#         print(current_message)
#         sent_messages.append(current_message)

# messages = ['i love you', 'what are we having for dinner', 'please pick up some'
# ' milk']
# show_messages(messages)

# sent_messages = []
# send_messages(messages[:], sent_messages)

# # Display both lists
# print("\nOriginal list:")
# print(messages)
# print("\nNew list")
# print(sent_messages)

# # 8-12 Sandwiches
# def make_sandwich(*contents):
#     """Collect as many items to add to a sandwich."""
#     print(f"\nMaking your sandwich:")
#     for content in contents:
#         print(f"adding {content} to your sandwich")
#     print("Your sandwich is ready!")

# make_sandwich('pastrami', 'pickles')
# make_sandwich('cheese', 'avocdo', 'olives')

# # 8-13 User Profile
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('michelle', 'fortuin',
#                              location='cape town',
#                              color='green', hobby='hiking')

# print(user_profile)

# # 8-14 Cars
# def make_car(manufacturer, make, **features):
#     """Build a dicitionary about cars and its features"""
#     car = {
#         'manufacturer': manufacturer.title(),
#         'make': make.title(),
#         }
#     for feature, value in features.items():
#         car[feature] = value
        
#     return car

# first_car = make_car('volkswagen', 'polo', color='white', wheels='alloy')
# print(first_car)

# car_profile = make_car('suzuki', 'jimny', engine='1.8 l', fuel_type='petrol')
# print(car_profile)

# 8-15 Printing Models
# Put the functions for the example printing_models.py in a separate file called
# printing_functions.py. Write an import statement at the top of 
# printing_models.py, and modify the file to use the imported functions.