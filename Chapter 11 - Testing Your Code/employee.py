# 11-3 Employee
class Employee:
    """Determine how much increase an employee receives."""

    def __init__(self, first_name, last_name, salary):
        """Store employee information."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give employee a raise."""
        self.salary += amount