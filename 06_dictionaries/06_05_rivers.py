# Stores names of rivers and their respective countries in a dictionary, prints them in sentences as well as individual key and values

rivers = {
    'mississippi' : 'america' ,
    'seine' : 'france' ,
    'han' : 'korea' ,
}

for river, country in rivers.items():
    print(f"\nThe {river.title()} river runs through {country.title()}.")

print("\nThese are all the rivers in the dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nThese are all the countris in the dictionary:")
for country in rivers.values():
    print(country.title())