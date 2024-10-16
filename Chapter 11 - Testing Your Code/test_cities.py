from city_functions import city_country

# # Failed test
def test_city_country():
    """Does a simple city and country pair work?"""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'

def test_city_country():
    """Populate a City and Country."""
    formatted_name = city_country('santiago', 'chile', '5000000')
    assert formatted_name == 'Santiago, Chile - population: 5000000'

# def test_city_country_population:
#     """Verify """