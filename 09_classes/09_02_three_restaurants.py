# Uses the same restaurant class but calls it with three different instances.

class Restaurant:
    """Describe a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a statement describing the restaurant."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Print a statement saying the restaurant is open."""
        print(f"{self.restaurant_name} is open!")

restaurant_1 = Restaurant('Honey Pig', 'Korean')
restaurant_2 = Restaurant('Mi Pueblo', 'Mexican')
restaurant_3 = Restaurant('Squisitos', 'Italian')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()