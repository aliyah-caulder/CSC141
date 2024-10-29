# Adds an inherited class, IceCreamStand, to the 9-4 restaurant class and adds a method to print a list of flavors.

class Restaurant:
    """Describe a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a statement describing the restaurant."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Print a statement saying the restaurant is open."""
        print(f"{self.restaurant_name} is open!")

    def read_number(self):
        """Print a statement showing the number of people served."""
        print(f"{self.restaurant_name} has served {self.number_served} people.")

    def set_number_served(self, people):
        """Set the number served to the given value."""
        self.number_served = people

    def increment_number_served(self, people):
        """Add the given numbr to the people served."""
        self.number_served += people

class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant specific to ice cream stands."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
    
    def show_flavors(self):
        """Print all the ice cream flavors."""
        print(f"The available ice cream flavors at {self.restaurant_name} are:")
        for flavor in self.flavors:
            print(flavor)

icecream = IceCreamStand('Frozen Joy', 'Gelato')

icecream.show_flavors()