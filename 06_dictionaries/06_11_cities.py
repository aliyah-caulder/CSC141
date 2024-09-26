# Stored a dictionary of cities and made each value a nested dictionary storing information about each city. Looped and printed all.
cities = {
    'Seoul' : {
        'country' : 'Korea' ,
        'population' : '9.776 million' ,
        'fact' : 'Gyeongbokgung palace once had more than 7,000 rooms!' ,
        } , 
    'Paris' : {
        'country' : 'France' , 
        'population' : '2.161 million' , 
        'fact' : 'The Eiffel tower was built as an entrance to the 1889 world expo!'
        } , 
    'Sydney' : {
        'country' : 'Australia' , 
        'population' : '5.297 million' , 
        'fact' : "Sydney is 610 miles across, which is more than double New York's 301 square miles!"
        } , 
    }

for city, info in cities.items():
    print(f"\nCity: {city}")
    for key, value in info.items():
        print(f"{key.title()}: {value}")