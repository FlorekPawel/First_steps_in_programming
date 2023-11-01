import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        check_city_country = city_country('warszawa', 'polska')
        self.assertEqual(check_city_country, 'Warszawa, Polska')
    
    def test_city_country_population(self):
        check_city_country_pop = city_country('paryż', 'francja', 2100000)
        self.assertEqual(check_city_country_pop,'Paryż, Francja - populacja 2100000')

unittest.main()