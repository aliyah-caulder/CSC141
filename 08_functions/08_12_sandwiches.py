# Defines a function to print the toppings on a sandwich using an arbitrary argument.

def make_sandwich(*toppings):
    """Printing the toppings on a sandwich"""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('cheese')

make_sandwich('peanut butter', 'jelly')

make_sandwich('salami', 'cheese', 'lettuce')