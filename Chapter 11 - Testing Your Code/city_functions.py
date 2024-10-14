# 11-1 City, Country
# def get_formatted_name(city, country):
#     """Generate a City and Country."""
#     city_country = f"{city}, {country}"
#     return city_country.title() 

# 11-2 Population
def get_formatted_name(city, country, population='5000000'):
    """Generate a City, Country and population."""
    if population:
        city_country = f"{city.title()}, {country.title()} - population: {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country