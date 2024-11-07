# Asks user for input, then writes it to a file.

from pathlib import Path

name = input("What is your name? > ")

path = Path('10_files_and_exceptions/guest.txt')
path.write_text(name)