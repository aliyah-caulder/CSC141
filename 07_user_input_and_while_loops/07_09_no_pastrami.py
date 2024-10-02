# uses a while loop to remove all instances of 'pastrami' from the list.

sandwich_orders = ['peanut butter', 'pastrami', 'italian', 'pastrami', 'falafel', 'pastrami']
print(sandwich_orders)

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)