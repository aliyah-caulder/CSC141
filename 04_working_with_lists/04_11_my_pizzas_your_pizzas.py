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