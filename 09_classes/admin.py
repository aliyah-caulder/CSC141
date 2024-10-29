from user import User

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