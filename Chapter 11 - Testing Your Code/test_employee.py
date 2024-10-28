from employee import Employee

# def test_store_employee():
#     """Gather employee information."""
#     first_name = "What is your first name? "
#     last = "What is your last name? "
#     annual salary = "What is your annual salary? "

def test_give_default():
    """Add $5000 dollars to the annual salary."""
    default = input("Press '1' to confirm the default raise.")
    while True: 
        response = input("Would you like to use the default raise? y/n")
    if response == 'y':
        amount = int(annual_salary) + int(5000)