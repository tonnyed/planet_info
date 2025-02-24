import unittest
from planets import PlanetQuery

class TestPlanetInfo(unittest.TestCase):
    def setUp(self):
        self.planets = PlanetQuery("data/planets.txt")

    def test_planet_data_loading(self):
        self.assertIn("Earth", self.planets.planets["earth"].name)
        self.assertIn("Mars", self.planets.planets["mars"].name)

    def test_planet_data(self):
        earth = self.planets.planets["earth"]
        self.assertEqual(earth.name, "Earth")
        self.assertEqual(earth.mass, 5.97237e24)
        self.assertEqual(earth.distance_from_sun, 149.6)
        self.assertEqual(earth.moons, ["Moon"])

    def test_planet_in_list(self):
        self.assertIn("Earth", self.planets.is_planet_in_list("earth"))
        self.assertIn("Mars", self.planets.is_planet_in_list("mars"))


    def test_invalid_planet(self):
        self.assertNotIn("plutoo", self.planets.is_planet_in_list("plutoo"))

def run_tests():
    unittest.main(exit=False)

if __name__ == "__main__":
    run_tests()