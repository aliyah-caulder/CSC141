# uses a while loop with an if statement to determine a ticket price based on age

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