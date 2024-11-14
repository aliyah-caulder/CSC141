class Employee:
    """Representing an employee."""

    def __init__(self, first, last, salary):
        """Initialize attributes of an employee including first and last name and salary."""
        self.first = first
        self.last = last
        self.salary = salary


    def give_raise(self, increase = 5000):
        """Increase salary by 5000 or an entered amount."""
        self.salary += increase