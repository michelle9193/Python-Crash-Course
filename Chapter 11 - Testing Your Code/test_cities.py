from city_functions import get_formatted_name as gfn

# Failed test
def test_city_country():
    """Does a simple city and country pair work?"""
    santiago_chile = output_string('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'

# def test_city_country():
#     """Populate a City and Country."""
#     formatted_name = gfn('santiago', 'chile', '5000000')
#     assert formatted_name == 'Santiago, Chile - population: 5000000'

# def test_city_country_population:
#     """Verify """