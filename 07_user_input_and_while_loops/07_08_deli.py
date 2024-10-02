# uses a while loop to loop through a list and move sandwiches from one list to the other

sandwich_orders = ['peanut butter', 'italian', 'falafel']
finished_sandwiches =[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nI am making your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nI have finished making sandwiches.")
print("Here are the sandwiches that have been made.")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)