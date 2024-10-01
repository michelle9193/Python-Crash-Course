# A Passing Test
from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Jannis Joplin' work?"""
    formatted_name = get_formatted_name('janis','marie', 'joplin')
    assert formatted_name == 'Janis Joplin'