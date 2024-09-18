current_users = ['laura', 'james', 'melanie', 'jessica', 'admin']

new_users = ['tracey', 'james', 'melanie', 'adam', 'paige']

for user in new_users:
    if user.lower() in current_users:
        print(f"Sorry, the username {user} is already taken. Please choose a new username.")
    else:
        print(f"The username {user} is available.")