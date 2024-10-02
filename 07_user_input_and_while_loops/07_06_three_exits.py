# runs the cose of 7-5 breaking the loop in 3 different ways using a break, conditional, and a flag.

# version 1

prompt = "\nPlease input your age."
prompt += "\nEnter 'quit' to end the program. > "

while True:
    age = input(prompt)
    
    if age == 'quit':
        break
    elif int(age) < 3:
        ticket = 0
    elif int(age) <= 12:
        ticket = 10
    elif int(age) > 12:
        ticket = 15

    print(f"\nYour ticket costs {ticket} dollars.")

# version 2

prompt = "\nPlease input your age."
prompt += "\nEnter 'quit' to end the program. > "

age = ''

while age != 'quit':
    age = input(prompt)
    
    if int(age) < 3:
        ticket = 0
    elif int(age) <= 12:
        ticket = 10
    elif int(age) > 12:
        ticket = 15

    print(f"\nYour ticket costs {ticket} dollars.")

# version 3

prompt = "\nPlease input your age."
prompt += "\nEnter 'quit' to end the program. > "

active = True

while active == True:
    age = input(prompt)
    

    if age == 'quit':
        active = False
    elif int(age) < 3:
        ticket = 0
    elif int(age) <= 12:
        ticket = 10
    elif int(age) > 12:
        ticket = 15

    print(f"\nYour ticket costs {ticket} dollars.")