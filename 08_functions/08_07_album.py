# Defines a function to make a dictionary storing info about an album including one optional parameter. Calls this function 4 times.

def make_album(artist, title, number=None):
    """create a dictionary storing music albums and their artist"""
    album = {'artist' : artist , "title" : title}
    if number:
        album['number of songs'] = number

    return album

message = make_album('My Chemical Romance', 'Three Cheers for Sweet Revenge')
print(message)

message = make_album('Sir Chloe', 'I am the Dog')
print(message)

message = make_album('Lady Gaga', 'The Fame Monster')
print(message)

message = make_album('Stray Kids', 'NOEASY', 14)
print(message)