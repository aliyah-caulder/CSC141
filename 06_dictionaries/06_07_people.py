# Stored info about people in 3 dictionaries which are nested inside a list. Looped through the list and printed all info.

person_1 = {
    'first_name' : 'Jaelyn' , 
    'last_name' : 'Hill' , 
    'age' : 18 , 
    'city' : 'Seoul' , 
    }
person_2 = {
    'first_name' : 'Penelope' , 
    'last_name' : 'Park' , 
    'age' : 18 , 
    'city' : 'Los Angeles' , 
    }
person_3 = {
    'first_name' : 'Faith' , 
    'last_name' : 'Chin' , 
    'age' : 18 , 
    'city' : 'Singapore' , 
    }

people = [person_1 , person_2 , person_3]

for person in people:
    print()
    print(person['first_name'] + ' ' + person['last_name'])
    print(person['age'])
    print(person['city'])