# TRUE CONDITIONAL TESTS

# Test 1
#car = 'mazda'
#print("Is car = 'mazda'? I predict True.")
#print(car == 'mazda')

# Test 2
#color = 'purple'
#print("Is color = 'purple'? I predit True.")
#print(color == 'purple')

# Test 3
#weather = 'cloudy'
#print("Is weather = 'cloudy'? I predit True")
#print(weather == 'cloudy')

# Test 4
#animal = 'cat'
#print("Is animal = 'cat'? I predict True")
#print(animal == 'cat')

# Test 5
#trainers = 'nike'
#print("Is trainers = 'nike'? I predict True")
#print(trainers == 'nike')

# FALSE CONDITIONAL TESTS

# Test 1
#brands = 'revlon'
#print("Is brands = 'Revlon'? I predit False.")
#print(brands == 'Revlon')

# Test 2
#motorcycles = 'ducati'
#print("Is motorcycles = 'bmw'? I predict False.")
#print(motorcycles == 'bmw')

# Test 3
#couch = 'leather'
#print("Is couch = 'mohair'? I predict False")
#print(couch == 'mohair')

# Test 4
#metal = 'gold'
#print("Is metal = 'silver'? I predict False")
#print(metal == 'silver')

# Test 5
#gem = 'diamond'
#print("Is gem = 'ruby'? I predict False.")
#print(gem == 'ruby')

# 5-2 More Conditional Tests
# Equality with strings
#flower = 'rose'
#print(flower == 'rose')

# Inequality with strings
#gas = 'petrol'
#print(gas == 'diesel')

# Test using lower method
#color = 'Purple'
#print(color.lower())

# Numerical Tests

#Equality
#age = 19
#print(age == 19)

#Inequality
#age = 19
#print(age == 18)

#Greater than & less than
#age = 19
#print(age > 70)

#Less than
#age = 19
#print(age < 20)

#Greater than or equal to
#age = 19
#print(age >= 19)

#Less than or equal to
#age = 19
#print(age <= 10)

#And keyword
#age = 19
#print(age <= 17 and age >= 16)
#print(age >= 13 and age <=20 )

#Or keyword
#age = 19
#print(age <= 17 or age > 50)
#print(age >= 13 or age <=20 )

#Test whether an items in a list
#burger_toppings = ['pickles', 'onions', 'ketchup']
#print('pickles' in burger_toppings)

#Test whether an items in a list
#burger_toppings = ['pickles', 'onions', 'ketchup']
#print('pineapple' not in burger_toppings)

#5-3 Alien Colors #1
alien_color = ['green', 'yellow', 'red']

#Pass
#if 'green' in alien_color:
    #print("You just earned 5 points!")

#Fail
#if 'pink' in alien_color:
    #print("")

#5-4 Alien colors #2
#If block
#if 'green' in alien_color:
    #print("You earned 5 points for shooting the alien!")
#elif 'pink' in alien_color:
    #print("You earned 10 points!")

#Else block
#if 'silver' in alien_color:
    #print("You earned 5 points for shooting the alien!")
#elif 'pink' not in alien_color:
    #print("You earned 10 points!")

#5-5 Alien Colors #3
#Alien is green
#if 'green' in alien_color:
    #print("You earned 5 points.")
#elif 'yellow' in alien_color:
    #print("You earned 10 points.")
#elif 'red' in alien_color:
    #print("You earned 15 points.")
#else:
    #print("No points for you.")

#Alien is yellow
#if 'pink' in alien_color:
    #print("You earned 5 points.")
#elif 'yellow' in alien_color:
    #print("You earned 10 points.")
#elif 'grey' in alien_color:
    #print("You earned 15 points.")
#else:
    #print("No points for you.")

#Alien is red
#if 'red' in alien_color:
    #print("You earned 15 points.")
#elif 'yellow' in alien_color:
    #print("You earned 10 points.")
#elif 'red' in alien_color:
    #print("You earned 15 points.")
#else:
    #print("No points for you.")    

#5-6 Stages of Life
#age = 20
#if age < 2:
    #print("You are a baby.")
#elif age < 4:
    #print("You are a toddler")
#elif age < 13:
    #print("You are a kid")
#elif age < 20 :
    #print("You are a teenager")
#elif age < 65:
    #print("You are an adult")
#else:
    #print("You are an elder")

#5-7 Favorite Fruit
#favorite_fruits = ['blueberries', 'mango', 'strawberries']
#if 'blueberries' in favorite_fruits:
    #print("I love blueberries")
#if 'mango' in favorite_fruits:
    #print("Mangoes are juicy and sweet!")
#if 'strawberries' in favorite_fruits:
    #print("Strawberries taste like summer!")

#print("\nI love fruit!")

#5-8 Hello Admin
#usernames = ['michelle', 'todd', 'admin', 'lisa', 'bradford']

#for username in usernames:
    #if username == 'admin':
        #print(f"Hello {username.title()}, would you like a status report?")
    #else:
        #print(f"Hello {username.title()}, thank you for logging in again.")

#5-9 No Users
#if usernames:
    #print("Hello Users!")
#else:
    #print("We need to find some users!")

#Remove all usernames from list and make sure correct message is printed.
#usernames = []

#if usernames:
    #print("Hello Users!")
#else:
    #print("We need to find some users!")

#5-10 Checking Usernames
#current_users = ['liam23', 'michellef', 'william_1', 'tony_sampson', 'gershwins1991', 'Holly']
#new_users = ['paxtonfire', 'holly', 'michelles', 'william_1', 'lopez_jlo', 'warreng']

#current_users_copy = ['liam23', 'michellef', 'william_1', 'tony_sampson', 'gershwins1991', 'holly']

#for new_user in new_users:
    #if new_user in current_users_copy:
        #print("Please enter a new username.")
    #else:
        #print("Username successful!")

#5-11 Ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Loop through the list
#for number in numbers:
    #print(number)

#Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")