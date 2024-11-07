# Attempts to read two files using a for loop. If one file is missing, the exception will be handled.
# This project was a 3 in difficulty. IT wasn't difficult but required some thinking,

from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(f'10_files_and_exceptions/{filename}')
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        print(contents)