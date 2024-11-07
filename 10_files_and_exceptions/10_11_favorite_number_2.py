# Reads favorite number from a json file.
# I'd give this assignment a 4 on difficulty because it was simple but involved multiple python files.

from pathlib import Path
import json

path = Path('10_files_and_exceptions/favorite_number.json')
contents = path.read_text()
number = json.loads(contents)

print(f"I know your favorite number! It's {number}")