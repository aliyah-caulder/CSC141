from city_functions import get_formatted_city

def test_city_country():
    """Does a city like Santiago, Chile work?"""
    formatted_city = get_formatted_city('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'

def test_city_country_population():
    """Does Santiago, Chile population 5000 work?"""
    formatted_city = get_formatted_city('santiago', 'chile', 'population=5000')
    assert formatted_city == 'Santiago, Chile, Population=5000'