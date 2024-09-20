# Aliyah Caulder
# 9/18/24
# Lab 7 challenge part 1

import os

os.system('cls')

limit = int(input("What is the speed limit? > "))
speed = int(input("How fast were you driving? > "))

os.system('cls')

if speed >= limit + 30:
    print("Woah woah woah that is some EXCESSIVE speeding.")
    print("License suspended. Walk home or get an Uber.")
elif speed > limit:
    print("You are speeding. Here is a ticket.")
else:
    print("You're good! Thanks for driving safely.")