# Aliyah Caulder
# Date: 9/6/24
# This is the code challenge for CSC141 lab day 4.

state_tax = float(input("How much is your state tax? (Please enter as a decimal, not a percentage.) > "))
meal_cost = int(input("How much does each meal cost? > "))

tax = meal_cost * state_tax

total_no_tax = meal_cost * 5

total_with_tax = (meal_cost + tax) * 5

print("| Lunch Spending Habits |")
print("--------------------")
print(f"Tax per meal: {tax}")
print(f"Total without tax: {total_no_tax}")
print(f"Total with tax: {total_with_tax}")
print("--------------------")
