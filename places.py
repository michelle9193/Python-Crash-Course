# 3-8 Seeing the World
# locations = ['bora bora', 'fiji', 'spain', 'amsterdam', 'thailand']
# Print list in OG order
# print(locations)

# Use sorted() to print list in alphabetical order
# print(sorted(locations))

# Show list is in original order
# print(locations)

# Use sorted() to print list in reverse-alphabetical order
# locations.sort(reverse=True)
# print(locations)

# Show list (again) is in original order
# print(locations)

# Show is in original order
# print(locations)

# Use reverse() to change the order of the list
# locations.reverse()
# print(locations)

# Use reverse() to change the order back to the original
# locations.reverse()
# print(locations)

# Use sort() to change the list to alphabetical order
# locations.sort()
# print(locations)

# Use sort to change list to reverse-alphabetical order
# locations.sort(reverse=True)
# print(locations)

# 3-9 Dinner Guests
# guests = ['gershwin', 'charlene', 'henry', 'lucy', 'rene']
# print(len(guests))

# 3-10 Every Function
languages = ['english', 'afrikaans', 'isixhosa', 'isizulu', 'sesotho', 'tswane', 'swahili']

# Accessing elements in a list
# print(languages[2].title())

# Access last item in a list
# message = (f'I do not know anyone who speaks {languages[-1].title()}!')
# print(message)

# Modifying elements 
# print(languages)
# languages[0] = 'venda'
# print(languages)

# Adding elements
# languages.append('tsonga')
# print(languages)

# Insert elements
# languages.insert(4, 'swati')
# print(languages)

# Removing elements
# del languages[0]
# print(languages)

# Remove item using pop() method
# popped_language = languages.pop()
# print(languages)
# print(popped_language.title())

# pop() items from any position
# languages.pop(6)
# print(languages)

# Remove item by value
# languages.remove('afrikaans')
# print(languages)

# Sort list permanently
# languages.sort()
# print(languages)

# Reverse sort() list
#languages.sort(reverse=True)
# print(languages)

# Sort list temporarily
# print(sorted(languages))

# Reverse list temporarily
# languages.reverse()
# print(languages)

# Intentional error
# print(languages[7].title())