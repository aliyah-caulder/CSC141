# Aliyah Caulder
# Date: 9/5/24
# This is the challenge for CSC141 lab day 3

print("To generate your introduction, I will need some information from you...")
print()

name = input("What is your name? > ")
age = input("How old are you? > ")
major = input("What is your major? > ")

message = f"\nHi, my name is {name.title()} and I am {age} years old! At Albright college, I study {major.title()}."

print(message)