# Expands on 9-14 by using a loop to see how many tries it would take to pull the same lottery ticket.

import random

lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_lottery = []

print("Any ticket matching these 4 letters or numbers wins a prize!")

for i in range (1, 5):
    lottery = random.choice(lottery_numbers)
    winning_lottery.append(lottery)

print(winning_lottery)

tries = 0

while True:
    tries += 1
    my_ticket = []
    for i in range(1, 5):
        my_number = random.choice(lottery_numbers)
        my_ticket.append(my_number)

    if my_ticket == winning_lottery:
        print(f"It took {tries} tries to win that lottery.")
        break
    else:
        continue