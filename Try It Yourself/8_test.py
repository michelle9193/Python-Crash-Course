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

# With tracks
def make_album(artist_name, album_name, songs=None):
    """A dictionary that returns artist details"""

    artist_details = {
        'artist': artist_name.title(), 
        'album': album_name.title(),
        }
    
    if songs:
        artist_details['songs'] = songs
    return artist_details

artist_info = make_album('taylor swift', 'folklore')
print(artist_info)

artist_info = make_album('maren morris', 'girl')
print(artist_info)

artist_info = make_album('ariana grande', 'eternal sunshine')
print(artist_info)

artist_info = make_album('heritage singers', 'forgiven', 13)
print(artist_info)