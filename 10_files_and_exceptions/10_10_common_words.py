# Reads the Metamorphosis from a text file and counts the number of times "the" is used.
# I'd give this assignment a 5 in difficulty because I had to find and copy an entire book to a file, as well as using a new method.

from pathlib import Path

path = Path("10_files_and_exceptions/metamorphosis.txt")

contents = path.read_text(encoding='utf-8')

number_of_the = contents.lower().count(" the ")

print(f"The word 'the' appears {number_of_the} times in Kafka's Metamorphosis.")