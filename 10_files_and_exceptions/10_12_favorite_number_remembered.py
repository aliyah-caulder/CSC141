# Combines the two programs from 10-11 using an if-else statement to find out if the favorite_number file exists yet.
# If yes, it loads the number. If not, it prompts the number and writes it.
# I'd give this difficulty a 4 because the code was already mostly written, I just had to put it in an if-else statement.

from pathlib import Path
import json

path = Path('10_files_and_exceptions/favorite_number.json')
if path.exists():
    contents = path.read_text()
    number = json.loads(contents)

    print(f"I know your favorite number! It's {number}!")
else:
    number = input("What is your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)

    print(f"We'll remember your favorite number is {number}!")