## 6-1 Person
#person = {
    #'first_name': 'lindsay',
    #'last_name': 'brown',
    #'age': 28,
    #'city': "new york"
    #}

#print(person['first_name'].title())
#print(person['last_name'].title())
#print(person['age'])
#print(person['city'].title())

## 6-2 Favorite numbers
#favorite_numbers = {'brandy': 13, 'marshall': 22, 'stephanie': 16, 'kelly': 92 
# , 'kimberley': 69}

#print(f"Brandy's favorite number is {favorite_numbers['brandy']}.")
#print(f"Marshall's favorite number is {favorite_numbers['marshall']}.")
#print(f"Stephanie's favorite number is {favorite_numbers['stephanie']}.")
#print(f"Kelly's favorite number is {favorite_numbers['kelly']}.")
#print(f"Kimberley's favorite number is {favorite_numbers['kimberley']}.")

## 6-3 Glossary
#new_words = {'strip': 'remove whitespace from both sides of a string', 
#'nostarch_url': 'remove prefix from a url', 'multiple assignment': 'assign 
# values to more than one variable using a single line of code', 'list': 'a 
# collection of items in a particular order', 'slicing': 'specify the index of 
# the first and last elements you want to work with', 'tuple': 'cannot change 
# once they are created, immutable list.', 'if statements': 'conditional test 
# which allow yout to check any condition', 'list comprehension': 'allows you to 
# generate the same list in just one line of code', 'if-elif-else': 'python 
# executes only one block of code and it runs each conditional test in order, 
# until one passes','method': 'functions that are associated with an object and 
# can manipulate its data or perform actions on it.' }


#print(f"Strip: {new_words['strip']}\n")
#print(f"Nostarch_url: {new_words['nostarch_url']}\n")
#print(f"Multiple Assignment: {new_words['multiple assignment']}\n")
#print(f"List: {new_words['list']}\n")
#print(f"Slicing: {new_words['slicing']}")

#6-4 Glossary 2
#Looping through a dictionary
#for key, value in new_words.items():
    #print(f"{key.title()}: {value}\n")

#6-5 Rivers
rivers = {
    #'zambezi': 'zambia',
    #'orange': 'free state',
    #'nile': 'egypt'
    }

#Use a loop to print a sentence about each river
#for river, country in rivers.items():
    #print(f"The {river.title()} runs through {country.title()}.")

#Use a loop to print the name of each river included in the dictionary
#for river in rivers.keys():
    #print(river.title())

#Use a loop to print the name of each country included in the dictionary
#for country in rivers.values():
    #print(country.title())

#6-6 Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

#Make a list of people who should take the favorite languages poll.
friends = ['samantha', 'amy', 'glenda', 'jen', 'edward', 'phil']

#Loop through the list of people who should take the poll. 
for name in friends:
    print(name.title())

# If they have taken the poll, print a message thanking them for responding.
    if name in favorite_languages:
        print(f"\t{name.title()}, thank you for responding!")
# If they have not yet taken the poll, print message invitiing them to take the
# poll.
    if name not in favorite_languages:
        print(f"\t{name.title()}, please take our poll!")

# 6-7 People
# person_0 = {'first_name': 'lindsay', 'last_name': 'brown', 'age': 28, 'city': 
#             "new york"}
# person_1 = {'first_name': 'tim', 'last_name': 'lopez', 'age': 22, 'city': 
#             "california"}
# person_2 = {'first_name': 'nelly', 'last_name': 'smith', 'age': 26, 'city': 
#             "hamptons"}

# people = [person_0, person_1, person_2]

# for people in people:
#     print(people)

# 6-8 Pets
# vicky = {'type': 'tortoise', 'owner': 'wendy harper'}
# todd = {'type': 'dog', 'owner': 'holly mcintyre'}
# keith = {'type': 'cat', 'owner': 'spencer mallow'}

# pets = [vicky, todd, keith]

# for pet in pets:
#     print(f'{pet}')

# 6-9 Favorite Places
# favorite_places = {
#     'harper': ['bali', 'switzerland'],
#     'james': ['singapore', 'germany'],
#     'lenny': ['paris', 'london'],
#     'josh': ['new zealand', 'italy']
#     }

# for name, places in favorite_places.items():
#     print(f"{name.title()} favorite places are:")
#     for place in places:
#         print(f"\t{place.title()}")

# 6-10 Favorite Numbers
# favorite_numbers = {
#     'brandy': [13, 5, 33], 
#     'marshall': [22, 11], 
#     'stephanie': [16, 30, 2], 
#     'kelly': [92, 14, 88],
#     'kimberley': [69, 26 ,1]
#     }

# for name, numbers in favorite_numbers.items():
#     print(f"\n{name.title()} favorite numbers are:")
#     for number in numbers:
#         print(f"{number}")

# 6-11
# cities = {
#     'cape town' : {
#         'country': 'south africa',
#         'population': 4618000,
#         'fact': 'Table Mountain is one of the New 7 Wonders of Nature.',
#         },

#     'yishun' : {
#         'country': 'singapore',
#         'population': 240000,
#         'fact': ' The worlds first nocturnal zoo-cum- safari is located here.'
# ,
#         },

#     'mauritius' : {
#         'country': 'east africa',
#         'population': 1263000,
#         'fact': 'the only African nation with Hinduism as the dominant 
# religion.',
#         }   
#     }

# for name, city_info in cities.items():
#     print(f"\n{name.title()}")
#     print(f"\tCountry: {city_info['country'].title()}")
#     print(f"\tApproximate Population: {city_info['population']}")
#     print(f"\tFun Fact: {city_info['fact'].title()}")

# 6-12 Extensions   



