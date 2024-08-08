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

#A list of dictionaries
#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'yellow', 'points': 10}
#alien_2 = {'color': 'red', 'points': 15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
    #print(alien)

#Use range() to create a fleet of 30 aliens
#Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Make first three aliens yellow, medium-speed worth 10 points each
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# Elif block that turns yellow aliens into red, fast-moving ones worth 15 points each.
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
