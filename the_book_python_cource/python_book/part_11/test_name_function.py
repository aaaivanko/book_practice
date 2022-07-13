import unittest
from tests import country_city


class CountryTestCase(unittest.TestCase):
    """Country city tests!"""
    def test_country_city(self):
        formatted_name = country_city('zboriv', 'ukraine')
        self.assertEqual(formatted_name, 'Zboriv Ukraine')

    def test_country_city_population(self):
        formatted_name = country_city('zboriv', 'ukraine', 5_000)
        self.assertEqual(formatted_name, 'Zboriv Ukraine. Population - 5000')
