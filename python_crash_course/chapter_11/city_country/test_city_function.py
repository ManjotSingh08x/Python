from c11_city_function import get_city_country

def test_city_country_name():
    """Do names like Santiago, Chile work?"""
    formatted_name = get_city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'
    """Does name like Delhi, India work?"""
    formatted_name1 = get_city_country('delhi', 'india')
    assert formatted_name1 == 'Delhi, India'
    
def test_city_country_population():
    """Do parameters like santiago, chile - population 5,000,000 work?"""
    formatted_name2 = get_city_country('santiago', 'chile', 5000000)
    assert formatted_name2 == 'Santiago, Chile - population 5000000'