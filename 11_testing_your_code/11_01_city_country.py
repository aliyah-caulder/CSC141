# Created a function to format a city name, as well as a test module. Running pytest returns that the code works.
# I'd give this assignment an 8 in difficulty because using separate modules as well as learning to run pytest was difficult.

from city_functions import get_formatted_city

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nGive me a city name: ")
    if city == 'q':
        break
    country = input("Give me a country: ")
    if country == 'q':
        break

    formatted_city = get_formatted_city(city, country)
    print(f"\tNeatly formatted city: {formatted_city}")