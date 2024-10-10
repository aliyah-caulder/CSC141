# Defines a function that prints the size and message on a t-shirt. Calls these functions using positional and keyword arguments.

def make_shirt(size, message):
    print(f'This size {size} shirt says "{message}".')

make_shirt('medium', 'I love cats')

make_shirt(size='medium', message='I love cats')