# Imports the random module to choose from a list of possible lottery numbers and print out 4 random ones.

import random

lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

print("Any ticket matching these 4 letters or numbers wins a prize!")

for i in range (1, 5):
    lottery = random.choice(lottery_numbers)
    print(lottery)