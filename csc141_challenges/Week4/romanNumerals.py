# Aliyah Caulder
# 9/19/24
# Lab 8 challenge part 2

# clearing the terminal so that it looks nice
import os
os.system('cls')

while True:
    # inserts a new value every time the loop restarts
    num = int(input("\nEnter a number between 1-100 to be converted to roman numerals. > "))

    if num < 1 or num > 100:
        # makes sure the input is within range, otherwise it will prompt user to put a new number in
        print("\nThe number has to be between 1 and 100.")
    else:
        # evaluates whether the value is 100
        if (num - 100) >= 0:
            hundreds = "C"
            num = num - 100
        else:
            hundreds = ""
        # evaluates whether there is 90 in the number
        if num - 90 >= 0:
            nineties = "XC"
            num = num - 90
        else:
            nineties = ""
        # evaluates whether there is 50 in the number
        if num - 50 >= 0:
            fifties = "L"
            num = num - 50
        else:
            fifties = ""
        # evaluates if and what the tens place contains
        if num - 40 >= 0:
            tens = "XL"
            num = num - 40
        elif num - 30 >= 0:
            tens = "XXX"
            num = num - 30
        elif num - 20 >= 0:
            tens = "XX"
            num = num - 20
        elif num - 10 >= 0:
            tens = "X"
            num = num - 10
        else:
            tens = ""
        # evaluates if there is a 9 in the ones place
        if num - 9 >= 0:
            nines = "IX"
            num = num - 9
        else:
            nines = ""
        # evaluates if there is a 5 in the ones place
        if num - 5 >= 0:
            fives = "V"
            num = num - 5
        else:
            fives = ""
        # evalulates what the ones place contains, if anything
        if num - 4 >= 0:
            ones = "IV"
            num = num - 4
        elif num - 3 >= 0:
            ones = "III"
            num = num - 3
        elif num - 2 >= 0:
            ones = "II"
        elif num - 1 >= 0:
            ones = "I"
        else:
            ones = ""
        # prints each place value. if there is nothing in that place value, nothing will be printed in that value.
        print(f"\n{hundreds}{nineties}{fifties}{tens}{nines}{fives}{ones}")