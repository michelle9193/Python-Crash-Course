# 3-4 Creating a guest list
guests = ['gershwin', 'charlene', 'henry']
print(guests)

# print(f"Will you, {guests[0].title()}, join me for dinner at 7pm on Thursday?")
# print(f"Will you, {guests[1].title()}, join me for dinner at 7pm on Thursday?")
# print(f"Will you, {guests[2].title()}, join me for dinner at 7pm on Thursday?")

# 3-5 Changing Guest List
# print(guests)
# guests.remove('henry')
# print(guests)
# guests.append('florence')
# print(guests)
# print(f"Will you, {guests[0].title()}, join me for dinner at 7pm on Thursday?")
# print(f"Will you, {guests[1].title()}, join me for dinner at 7pm on Thursday?")
# print(f"Will you, {guests[2].title()}, join me for dinner at 7pm on Thursday?")

# 3-6 More guests
# print(f"Great news, {guests[0].title()}! I have found a bigger table and I will be inviting more guests!")
# print(f"Great news, {guests[1].title()}! I have found a bigger table and I will be inviting more guests!")
# print(f"Great news, {guests[2].title()}! I have found a bigger table and I will be inviting more guests!")

guests.insert(0, 'florence')
guests.insert(3, 'melvin')
guests.append('heather')
print(guests)
# print(f"Will you, {guests[0].title()}, join me for dinner at 7pm on Thursday?")
# print(f"Will you, {guests[1].title()}, join me for dinner at 7pm on Thursday?")
# print(f"Will you, {guests[2].title()}, join me for dinner at 7pm on Thursday?")
# print(f"Will you, {guests[3].title()}, join me for dinner at 7pm on Thursday?")
# print(f"Will you, {guests[4].title()}, join me for dinner at 7pm on Thursday?")
# print(f"Will you, {guests[5].title()}, join me for dinner at 7pm on Thursday?")

# 3-7 Shrinking guest list
print("Sorry, guys I can only invite 2 people for dinner")
# Remove Heather
popped_guests = guests.pop().title()
print(popped_guests)
print(f'I regret to inform you that I cannot host you for my dinner party. I am so sorry, {popped_guests}!')
print(guests)
# Remove Henry
popped_guests = guests.pop().title()
print(popped_guests)
print(f'I regret to inform you that I cannot host you for my dinner party. I am so sorry, {popped_guests}!')
print(guests)
# Remove Melvin
popped_guests = guests.pop().title()
print(popped_guests)
print(f'I regret to inform you that I cannot host you for my dinner party. I am so sorry, {popped_guests}!')
print(guests)
# Remove Charlene
popped_guests = guests.pop().title()
print(popped_guests)
print(f'I regret to inform you that I cannot host you for my dinner party. I am so sorry, {popped_guests}!')
print(guests)

# Invite last 2 guests
print(f'{guests[0].title()}, you are invited to join me for dinner on Thursday at 7pm!')
print(f'{guests[1].title()}, you are invited to join me for dinner on Thursday at 7pm!')
print(guests)

# Delete last 2 names
del guests[0]
print(guests)
del guests[0]
print(guests)