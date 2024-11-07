# Uses a while loop to ask for multiple names, then saves them all on separate lines in a text file.

from pathlib import Path

text = ''

while True:
    print("Enter your name, or press q to quit.")
    name = input("What is your name? > ")

    if name == 'q':
        break
    else:
        text += f"{name}\n"

path = Path('10_files_and_exceptions/guest_book.txt')
path.write_text(text)