# Allows each person to have more than one favorite number and prints both their name and their favorite numbers.

favorite_numbers = {
    'aliyah' : [8 , 5] , 
    'mera' : [95 , 2] , 
    'kassia' : [1119 , 7] , 
    'jillian' : [3 , 94] , 
    'hudson' : [10 , 11] , 
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")