# # Writing to a File
# # Writing a Single Line
# from pathlib import Path

# path = Path('programming.txt')
# path.write_text("I love programming!")

# Writing Multiple Lines
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)