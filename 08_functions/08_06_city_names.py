# Makes a function to format the name of a city and its country and returns it, then prints three different city-country pairs.

def city_country(city, country):
    """Format the city and country nicely"""
    formatted_city = f"{city.title()}, {country.title()}"
    return formatted_city

message = city_country('chicago', 'united states')
print(message)

message = city_country('seoul', 'south korea')
print(message)

message = city_country('sydney', 'australia')
print(message)