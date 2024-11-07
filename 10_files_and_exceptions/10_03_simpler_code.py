# Removes the temporary variable used before the loop for more concise code.

from pathlib import Path

path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line.replace('Python', 'C'))