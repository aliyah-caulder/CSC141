# Uses the make_shirt function but adds two default arguments. Calls it three times using each default argument two times.

def make_shirt(size='large', message='I love Python'):
    print(f'This size {size} shirt says "{message}".')

make_shirt()

make_shirt(size='medium')

make_shirt(message='I love cats')