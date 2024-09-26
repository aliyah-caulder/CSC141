# Stores information about pets in dictionaries. Nests these dictionaries in a list and loops through it to print all information.
pet_1 = {
    'name' : 'Jazzmynn' , 
    'animal' : 'lab mix' , 
    'color' : 'black' , 
    'owner' : 'Daniel' ,
    }
pet_2 = {
    'name' : 'Jax' , 
    'animal' : 'cat' , 
    'color' : 'black' , 
    'owner' : 'Barbie' ,
    }
pet_3 = {
    'name' : 'Rey' , 
    'animal' : 'cat' ,
    'color' : 'white and brown' , 
    'owner' : 'Barbie' ,
    }
pet_4 = {
    'name' : 'Charlie' , 
    'animal' : 'jindo terrier' , 
    'color' : 'white' , 
    'owner' : 'Sunhwa' , 
    }
pet_5 = {
    'name' : 'Ddeok' , 
    'animal' : 'rat' , 
    'color' : 'black and white' , 
    'owner' : 'Aliyah' ,
    }
pet_6 = {
    'name' : 'Bingsu' , 
    'animal' : 'rat' , 
    'color' : 'black and white' , 
    'owner' : 'Aliyah' ,
    }
pet_7 = {
    'name' : 'Wren' , 
    'animal' : 'boston terrier' , 
    'color' : 'brown' , 
    'owner' : 'Will' , 
    }

pets = [pet_1, pet_2, pet_3, pet_4, pet_5, pet_6, pet_7]

for pet in pets:
    print()
    print(f"Name: {pet['name']}")
    print(f"Animal: {pet['animal']}")
    print(f"Color: {pet['color']}")
    print(f"Owner: {pet['owner']}")