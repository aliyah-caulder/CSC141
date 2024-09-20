# Aliyah Caulder 
# 9/12/24
# Lab 5 part 1 challenge

import os

weight = float(input("How much does one Lion bar weigh, in ounces? > "))
numberOfBars = int(input("How many Lion Bars were made last month? > "))

totalWeight = numberOfBars * weight
ounces = totalWeight % 16
weightInPounds = (totalWeight - ounces) / 16

os.system("cls")

print()
print("Lion Bars Production Report")
print("-----------------------------")
print(f"\nMonthly Production = {numberOfBars} Lion Bars @ {weight} oz per bar.")
print(f"\nTotal Weight Produced = {totalWeight} oz, which is {weightInPounds} lb(s), {ounces} oz.")
print()

