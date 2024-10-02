# Asks user for a number and uses the modulo operator to determine if the number is a multiple of 10.

number = int(input("Enter a number: "))

if number % 10 == 0:
    print("That number is a multiple of 10.")
else:
    print("That is not a multiple of 10.")