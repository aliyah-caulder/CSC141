# Takes 9-7 and adds Priveleges as a separate class. Makes an instance of this class an attribute in the Admin class.

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

class Privileges:
    """An attempt to model the privileges an admin has."""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        """Show the admin priveleges."""
        print("Your admin privileges are:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    """Create Admin info."""
    def __init__(self, first, last, age, major, location):
        """Initialize attributes from the user class."""
        super().__init__(first, last, age, major, location)
        self.privileges = Privileges()

user = Admin('aliyah', 'caulder', 17, 'theatre', 'reading')
user.describe_user()
user.privileges.show_privileges()