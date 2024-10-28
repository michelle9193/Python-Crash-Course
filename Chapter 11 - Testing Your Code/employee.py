# 11-3 Employee
class Employee:
    """Determine how much increase an employee receives."""

    def __init__(self, first_name, last_name, annual_salary):
        """Store employee information."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = input("Please enter your annual salary")

    def give_raise(self, add_raise):
        """Determine how much the raise amount is."""
        add_raise = input("Please enter '1' for default raise or '2' to add a different amount")
        if 1:
            print(int(self.annual_salary)  + 5000)
        else:
            diff_amount = input("Please enter a different amount: ")
            print(int(self.annual_salary)  + diff_amount)