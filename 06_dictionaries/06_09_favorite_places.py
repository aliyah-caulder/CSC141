# Nests lists of people's favorite places inside a dictionary. Loops through the dictionary and each list to print all the places.

favorite_places = {
    'aliyah' : ['Hongdae' ,  'Itaewon' , 'Elicott City'] , 
    'barbie' : ['Denver' ,  'Omaha' , 'Nami Island'] , 
    'daniel' : ['Okinawa' , 'Bethesda', 'Oaxaca']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places:")
    for place in places:
        print(f"\t{place}")