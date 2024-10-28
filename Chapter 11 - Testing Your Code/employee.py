# 11-3 Employee
class Employee:
    """Determine how much increase an employee receives."""

    def __init__(self, first_name, last_name, annual_salary):
        """Store employee information."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = input("Please enter your annual salary")

    def give_raise(self, default_value, custom_raise):
        """Determine how much the raise amount is."""
        self.default_value = 5000
        self.custom_raise = input("Enter custom value")