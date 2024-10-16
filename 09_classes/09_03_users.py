# Make a class called User which stores attributes, describes and greets the user. Call both methods 3 different instances.

class User:
    """Create user info"""
    def __init__(self, first, last, age, major, location):
        """Define several user attributes."""
        self.first_name = first
        self.last_name = last
        self.age = age
        self.major = major
        self.location = location

    def describe_user(self):
        """List off information about a user."""
        print()
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print()
        print(f"Hello {self.first_name} {self.last_name}!")

user_1 = User('Aliyah', 'Caulder', 17, 'Theatre', 'Reading')
user_2 = User('Penelope', 'Park', 18, 'Economics', 'Atlanta')
user_3 = User('Faith', 'Chin', 18, 'English', 'Singapore')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
