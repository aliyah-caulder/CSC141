# Defines a function which describes a city and its country with a default country. Calls the function three times.

def describe_city(city, country='America'):
    print(f"{city} is in {country}.")

describe_city('New York')

describe_city('Seoul', 'South Korea')

describe_city(country='Russia', city='Moscow')