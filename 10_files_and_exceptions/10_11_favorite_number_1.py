# Stores favorite number to a json file.
# I'd give this assignment a 4 on difficulty because it was simple but involved multiple python files.

from pathlib import Path
import json

number = input("What is your favorite number? ")

path = Path('10_files_and_exceptions/favorite_number.json')
contents = json.dumps(number)
path.write_text(contents)

print(f"We'll remember your favorite number is {number}!")