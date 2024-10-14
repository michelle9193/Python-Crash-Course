from city_functions import get_formatted_name as gfn

def test_city_country():
    """Populate a City and Country."""
    formatted_name = gfn('santiago', 'chile', '5000000')
    assert formatted_name == 'Santiago, Chile - population: 5000000'

# def test_city_country_population:
#     """Verify """