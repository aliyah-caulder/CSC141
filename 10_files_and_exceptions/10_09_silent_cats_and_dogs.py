# Modifies 10-8 to fail silently rather than printing a message that an exception occurred.
# This project was a 1 in difficulty because I simply had to paste code from the last assignment and change one line of code to "pass"

from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(f'10_files_and_exceptions/{filename}')
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(contents)