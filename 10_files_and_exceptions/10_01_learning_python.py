# Reads a text file by reading the whole file and each individual line.

from pathlib import Path

path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text()

print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)