# edited the many_users example code to have a working username and password login system.

passwords = {
 'aeinstein': 'e=mc^2'  ,
 'mcurie': 'radiumrocks',
 }

entered_username = input("username: ")
entered_password = input("password: ")

if entered_username not in passwords.keys():
    print("That username does not exist.")

for username, password in passwords.items():
    if entered_username == username:
        if entered_password == password:
            print(f"Welcome, {username}!")
        else:
            print("That password is incorrect.")
