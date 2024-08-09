#favorite_languages = {
    #'jen': 'python',
    #'sarah': 'c',
    #'edward': 'rust',
    #'phil': 'python',
    #}

#language = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is {language}.")

#Looping through all key-value pairs
#for name, language in favorite_languages.items():
    #print(f"{name.title()}'s favorite language is {language.title()}")

#Looping through all the keys in a dictionary
#The keys() method is useful when you don't need to work with all of the values 
# in a dictionary
#for name in favorite_languages.keys():
    #print(name.title())

#Looping through the keys is actually the default behavior when looping through 
# a dictionary
#for name in favorite_languages:
#rather than:
#for name in favorite_languages.keys()

#friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
    #print(f"Hi {name.title()}")

    #if name in friends:
        #language = favorite_languages[name].title()
        #print(f"\t{name.title()}, I see you love {language}!")

# keys() method isn't just for looping: it actually returns all the keys
#if 'erin' not in favorite_languages.keys():
    #print(f"Erin, please take our poll!")

#Looping through a dictionary's keys in a particular order
#To achieve this sort the keys as they returned in the for loop
#for name in sorted(favorite_languages.keys()):
    #print(f"{name.title()}, thank you for taking the poll.")

#Looping through all values in a dictionary
#Use the values() method to return a sequence of values without any keys.
#print("The following langauages have been mentioned:")
#for language in favorite_languages.values():
    #print(language.title())

#To check if each language is unique, use a set. A set is a collection in which 
# each item must be unique:
#print("The following languages have been mentioned:")
#for language in set(favorite_languages.values()):
    #print(language.title())

# Inside the dictionary's for loop, use another for loop to run through the list
#  of languages associated with each person.
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    # Check whether each person one favorite language
    if len(languages) == 1:
        print(f"\n{name.title()}' favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

