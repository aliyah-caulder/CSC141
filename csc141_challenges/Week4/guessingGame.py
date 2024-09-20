# Aliyah Caulder
# 9/19/24
# Lab 8 challenge part 1

import random, os, time
os.system('cls')

name = input("What is your name? > ")

# I need to define these values outside of the loop because I don't want them to be reset every time
num = random.randint(1, 20)
attempts = 0

while True:
    os.system('cls')
    print(f"Hello {name}, today we will play a guessing game. To play, guess a number between 1 and 20. We will let you know if you guess was too low or too high, or if you guessed the correct number. You will have five attempts to guess the correct number. Let's begin!")
    
    if attempts >= 5:
        print("\nYou ran out of guesses. Sorry.")
        time.sleep(3)
        break
    else:
        guess = int(input("\nPlease guess a number. > "))
        attempts = attempts + 1
        if guess >= 1 and guess <= 20:
            if guess == num:
                print(f"\nYou guessed it! It took you {attempts} attempts.")
                time.sleep(3)
                break
            elif guess > num:
                print("\nToo high.")
                time.sleep(3)
            elif guess < num:
                print("\nToo low.")
                time.sleep(3)
        else:
            print("The number is between 1 and 20, silly.")
            time.sleep(3)

print("\nThanks for playing! Rerun the program to try again.")