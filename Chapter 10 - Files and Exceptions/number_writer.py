# Storing Data
# Using json.dumps() and json.loads()
# json.dumps() to generate a string containing the JSON representation of the 
# data we're working with
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)