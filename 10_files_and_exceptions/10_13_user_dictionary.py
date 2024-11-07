# Saves user info to a dictionary in a json file and calls it if the file already exists.
# I'd give this a 7 on difficulty because I had to remember how to use dictionaries.

from pathlib import Path
import json

path = Path('10_files_and_exceptions/user_info.json')
if path.exists():
    contents = path.read_text()
    user_info = json.loads(contents)
    print(f"Welcome back, {user_info['username']}!")
    print(f"You are {user_info['age']} years old.")
    print(f"Your major is {user_info['major']}.")

else:
    user_info = {}
    user_info['username'] = input("What is your name? ")
    user_info['age'] = input("How old are you? ")
    user_info['major'] = input("What is your major? ")
    contents = json.dumps(user_info)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {user_info['username']}!")