import unittest
from src.fetch_breweries import fetch_breweries

class TestBreweryAPI(unittest.TestCase):
    def test_fetch_breweries(self):
        data = fetch_breweries()
        self.assertTrue(isinstance(data, list))
        self.assertGreater(len(data), 0)

if __name__ == "__main__":
    unittest.main()
