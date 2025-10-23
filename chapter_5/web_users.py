# usernames = {'admin', 'apple', 'bobman123', 'dino', 'bigdill'}
# usernames = {}

# if usernames == {}:
# print("Users needed")

# for user in usernames:
# if user == 'admin':
# print(f'Welcome {user}, would you like to see a status page?')
# else:
# print(f"{user.lower()} welcome to the website!!!")

current_users = {'admin', 'apple', 'bobman123', 'dino', 'bigdill'}
new_users = {'apple', 'Dino', 'tommy#44', '77ducks', 'youngman99'}


if current_users == new_users:
    print("Username already in use. Please try again.")
else:
    print(f"{new_users} is free to use")
