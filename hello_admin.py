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