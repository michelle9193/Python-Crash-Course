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