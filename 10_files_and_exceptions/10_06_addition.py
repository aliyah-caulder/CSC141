# Make an addition calculator that handles value errors.

print("Give me two numbers, and I'll add them. Press q to quit.")

while True:
    num1 = input("First number: ")
    if num1 == 'q':
            break
    num2 = input("Second number: ")
    if num2 == 'q':
            break
    
    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print("You can only enter numbers.")
    else:
        print(f"The sum is {sum}.")