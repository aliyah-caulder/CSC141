# Create a class for a restaurant with two attributes and two methods. Call all of these.

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

restaurant = Restaurant('Honey Pig', 'Korean')

print(f"The restaurant is called {restaurant.restaurant_name}")
print(f"They serve {restaurant.cuisine_type} food.")
restaurant.describe_restaurant()
restaurant.open_restaurant()