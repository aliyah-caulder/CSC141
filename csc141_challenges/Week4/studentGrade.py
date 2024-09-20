# Aliyah Caulder
# 9/19/24
# Lab 7 challenge part 2

import os
os.system('cls')

grade = int(input("What is your final grade score? > "))

os.system('cls')

if grade >= 0 and grade < 60:
    letter = "F"
elif grade >= 0 and grade < 70:
    letter = "D"
elif grade >= 0 and grade < 80:
    letter = "C"
elif grade >= 0 and grade < 90:
    letter = "B"
elif grade >= 0 and grade <= 100:
    letter = "A"
else:
    letter = False

if letter:
    print(f"Your grade is {letter}.")
else:
    print("Please enter a grade between 0 and 100.")
