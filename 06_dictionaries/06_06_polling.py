favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

should_poll = ['jen', 'josh', 'phil', 'ben']

for person in should_poll:
    print(person.title())
    if person in favorite_languages.keys():
        print("\tThanks for taking the poll!")
    else:
        print("\tPlease take the poll.")