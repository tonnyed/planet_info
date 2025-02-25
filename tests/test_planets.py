import unittest
from planets import PlanetQuery


class TestPlanetInfo(unittest.TestCase):
    """Test cases for the PlanetQuery class and its methods."""

    def setUp(self):
        """Set up the test environment by initializing a PlanetQuery instance."""  # noqa: E501
        self.planets = PlanetQuery("data/planets.txt")

    def test_planet_data_loading(self):
        """Test if the planet data is loaded correctly by checking the names of Earth and Mars."""   # noqa: E501
        self.assertIn("Earth", self.planets.planets["earth"].name)
        self.assertIn("Mars", self.planets.planets["mars"].name)

    def test_planet_data(self):
        """Test the attributes of the Earth planet object."""
        earth = self.planets.planets["earth"]
        self.assertEqual(earth.name, "Earth")
        self.assertEqual(earth.mass, 5.97237e24)
        self.assertEqual(earth.distance_from_sun, 149.6)
        self.assertEqual(earth.moons, ["Moon"])

    def test_planet_in_list(self):
        """Test if the is_planet_in_list method correctly identifies Earth and Mars."""  # noqa: E501
        self.assertIn("Earth", self.planets.is_planet_in_list("earth"))
        self.assertIn("Mars", self.planets.is_planet_in_list("mars"))

    def test_invalid_planet(self):
        """Test if the is_planet_in_list method correctly handles an invalid planet name."""  # noqa: E501
        self.assertNotIn("plutoo", self.planets.is_planet_in_list("plutoo"))


def run_tests():
    """Run all the test cases without exiting the program."""
    unittest.main(exit=False)


if __name__ == "__main__":
    run_tests()
