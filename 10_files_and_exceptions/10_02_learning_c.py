# Prints each line from the learning_python file but replaces the word Python with C using .replace()

from pathlib import Path

path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line.replace('Python', 'C'))