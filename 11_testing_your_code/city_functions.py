def get_formatted_city(city, country, population = ''):
    """Generate a neatly formatted city name."""
    if population:
        formatted_city = f"{city}, {country}, {population}"
    else:
        formatted_city = f"{city}, {country}"

    return formatted_city.title()