# from imported_admin import Admin

# # Make an instance called users from the class
# billy = Admin('billy', 'james', 'billy@hotmail.com', 'claremont', 
#                         'admin_billy')
# billy.describe_user

# billy.privileges.show_privileges()

# print("\nAdding privileges:")
# billy_privileges = [
#     'can add post', 
#     'can delete post', 
#     'can ban user'
#     ]

# billy.privileges.privileges = billy_privileges
# billy.privileges.show_privileges()

from user import Users
from privileges_admin import Privileges, Admin

billy = Admin('billy', 'james', 'billy@hotmail.com', 'claremont', 
                        'admin_billy')
billy.describe_user

billy.privileges.show_privileges()

print("\nAdding privileges:")
billy_privileges = [
    'can add post', 
    'can delete post', 
    'can ban user'
    ]

billy.privileges.privileges = billy_privileges
billy.privileges.show_privileges()