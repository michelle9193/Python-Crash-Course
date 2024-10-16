# 11-1 City, Country
# def city_country(city, country):
#     """Generate a City and Country."""
#     city_country = f"{city}, {country}"
#     return city_country.title() 

# 11-2 Population
# Modify your function so it requires a third parameter, population.
def city_country(city, country, population):
    """Return a string of city, country - population 5_000_000."""
    output_string = f"{city.title()}, {country.title()}"
    output_string += f" -population {population}"
    return output_string

# City Functions Optional
def city_country(city, country, population='5000000'):
    """Generate a City, Country and population."""
    if population:
        city_country = f"{city.title()}, {country.title()} - population: {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country