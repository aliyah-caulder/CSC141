# uses a while loop to repeat back pizza toppings unless a user enters quit

prompt = "\nPlease enter pizza toppings you would like."
prompt += "\nEnter 'quit' when you are finished. > "

while True:
    topping = input(prompt)

    if topping.lower() == 'quit':
        break
    else:
        print(f"\n{topping.title()} added to the pizza.")