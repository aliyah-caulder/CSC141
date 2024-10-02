# Asks user for a number, converts it from a string to a number.  Uses an if statement to compare it to the number 8.

guests = int(input("How many people are in your group? > "))

if guests > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready!")