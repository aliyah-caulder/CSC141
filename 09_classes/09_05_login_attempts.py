# Uses code from 9-3 but adds an attribute called login attempts. Adds a method to increment as well as reset login attempts.

class User:
    """Create user info"""
    def __init__(self, first, last, age, major, location):
        """Define several user attributes."""
        self.first_name = first
        self.last_name = last
        self.age = age
        self.major = major
        self.location = location
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User('Aliyah', 'Caulder', 17, 'Theatre', 'Reading')
user_1.describe_user()
user_1.greet_user()
print()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")
user_1.reset_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")