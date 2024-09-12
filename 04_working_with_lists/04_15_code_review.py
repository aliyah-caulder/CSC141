# program 1
pizzas = ["cheese", "buffalo", "pepperoni"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append("pesto")
friend_pizzas.append("hawaiian")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# program 2
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

# program 3
foods = ("pizza", "pasta", "salad", "steak", "cake")
print("\nHere are the foods the restaurant offers:")
for food in foods:
    print(food)

foods = ("burgers", "pasta", "salad", "tacos", "cake")
print("\nHere is the modified menu for the restaurant:")
for food in foods:
    print(food)