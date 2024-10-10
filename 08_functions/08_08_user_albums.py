# Uses the make_album function from 8-7 but uses a while loop and user input to create the albums.
def make_album(artist, title, number=None):
    """create a dictionary storing music albums and their artist"""
    album = {'artist' : artist , "title" : title}
    if number:
        album['number of songs'] = number

    return album

while True:
    print("Create a music album.")
    print("Enter 'quit' at any time to quit.")
    
    entered_artist = input("What is the artist name? > ")
    if entered_artist == 'quit':
        break

    entered_title = input("What is the title of the album? > ")
    if entered_title == 'quit':
        break

    entered_number = input("How many songs are on the album? > ")
    if entered_number == 'quit':
        break

    message = make_album(entered_artist, entered_title, entered_number)
    print(message)