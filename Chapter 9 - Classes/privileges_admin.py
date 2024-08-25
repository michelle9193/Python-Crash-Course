from user import Users

class Privileges:
    """Model privileges to the admin user."""
    def __init__(self, privileges=[]):
        """Initialize privileges attribute"""
        self.privileges = privileges

    def show_privileges(self):
        """Display all the admin privileges."""
        print(f"The admin has the following privileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

class Admin(Users):
    """Initialize admin priexcvileges."""
    def __init__(self, first_name, last_name, email, location, username):
        """
        Initialize attributes of the parent class.
        Then initiliaze attributes specific to an administrator.
        """
        super().__init__(first_name, last_name, email, location, username)
        
        # Initialize an empty set of privileges.
        self.privileges = Privileges()