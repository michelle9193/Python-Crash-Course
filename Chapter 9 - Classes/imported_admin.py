class Users:
    """This is how to add users"""

    def __init__(self, first_name, last_name, email, location, username):
        """Initialize a user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.location = location.title()
        self.username = username

    def describe_user(self):
        """Print a summary of the user's information"""
        # summary = f"First Name: {self.first_name}\nLast Name: {self.last_name}
        # \nEmail: {self.email}\nLocation: {self.location}\nUsername: 
        # {self.username}"
        # print(f"\n{summary}")
        print(f"\n{self.first_name} {self.last_name}")
        print(f"{self.email}")
        print(f"{self.location}")
        print(f"{self.username}")

    def greet_user(self):
        """A personalize greeting to the user"""
        greeting = f"Hello, {self.first_name} {self.last_name}!"
        print(f"\n{greeting}")

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
    
