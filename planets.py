class Planet:
    """
    Represents a planet in the solar system.

    Attributes:
        name (str): The name of the planet.
        mass (float): The mass of the planet in Earth masses.
        distance_from_sun (float): The distance of the planet from the Sun in million kilometers.  # noqa: E501
        moons (list): A list of the planet's moons.
    """

    def __init__(self, name, mass, distance_from_sun, moons):
        """
        Initializes a Planet object.

        Args:
            name (str): The name of the planet.
            mass (float): The mass of the planet in Earth masses.
            distance_from_sun (float): The distance of the planet from the Sun in million kilometers.  # noqa: E501
            moons (list): A list of the planet's moons.
        """
        self.name = name
        self.mass = mass
        self.distance_from_sun = distance_from_sun
        self.moons = moons

    def __str__(self):
        """
        Returns a string representation of the planet.

        Returns:
            str: A formatted string containing the planet's name, mass, distance from the Sun, and moons.  # noqa: E501
        """
        return (f"Name: {self.name}\n"
                f"Mass: {self.mass} kg\n"
                f"Distance from Sun: {self.distance_from_sun} million km\n"
                f"Moons: {', '.join(self.moons) if self.moons else 'None'}")


class PlanetQuery:
    """
    A class to query and retrieve information about planets in the solar system.  # noqa: E501

    Attributes:
        load_data (str or bool): Path to a file containing planet data or False to use hardcoded data.  # noqa: E501
        planets (dict): A dictionary of Planet objects, keyed by planet name.
    """

    def __init__(self, load_data=False):
        """
        Initializes the PlanetQuery object.

        Args:
            load_data (str or bool): Path to a file containing planet data or False to use hardcoded data.  # noqa: E501
        """
        self.load_data = load_data
        self.planets = self.load_planets_hardcode()

        # If a file is provided, override hardcoded data
        if load_data:
            self.planets = self.load_file()

    def load_file(self):
        """
        Reads planet data from a file and returns a dictionary of Planet objects.  # noqa: E501

        Returns:
            dict: A dictionary of Planet objects, keyed by planet name.
        """
        load_data = self.load_data
        planets = {}
        try:
            with open(load_data, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    name = data[0]
                    mass = float(data[1])
                    distance = float(data[2])
                    moons = data[4:] if int(data[3]) > 0 else []
                    planets[name.lower()] = Planet(name, mass, distance, moons)
            return planets
        except (FileNotFoundError, IOError):
            print(f"Error: The file {self.load_data} was not found.")
            return None

    def load_planets_hardcode(self):
        """
        Loads hardcoded planet data and returns a dictionary of Planet objects.

        Returns:
            dict: A dictionary of Planet objects, keyed by planet name.
        """
        planets = {}
        data = [
            Planet("Mercury", 0.055, 57.9, []),
            Planet("Venus", 0.815, 108.2, []),
            Planet("Earth", 1.0, 149.6, ["Moon"]),
            Planet("Mars", 0.107, 227.9, ["Phobos", "Deimos"]),
            Planet("Jupiter", 317.8, 778.5, ["Io", "Europa", "Ganymede", "Callisto"]),  # noqa: E501
            Planet("Saturn", 95.2, 1433.5, ["Titan", "Rhea", "Iapetus", "Dione"]),  # noqa: E501
            Planet("Uranus", 14.5, 2872.5, ["Titania", "Oberon", "Umbriel", "Ariel"]),  # noqa: E501
            Planet("Neptune", 17.1, 4495.1, ["Triton", "Proteus", "Nereid"]),
            Planet("Pluto", 0.0022, 5906.4, ["Charon"])
        ]

        for planet in data:
            name = planet.name
            mass = float(planet.mass)
            distance = float(planet.distance_from_sun)
            moons = planet.moons[4:] if len(planet.moons) > 0 else []
            planets[name.lower()] = Planet(name, mass, distance, moons)

        return planets

    def get_planet_mass(self, planet_name):
        """
        Retrieves the mass of a planet.

        Args:
            planet_name (str): The name of the planet.

        Returns:
            str: A string containing the planet's mass or an error message if the planet is not found.  # noqa: E501
        """
        planet_name = planet_name.lower()
        self.planet_name = planet_name
        planets = self.planets
        if self.planet_name in planets:
            return f"The mass of {planets[planet_name].name} is {planets[planet_name].mass} kg."  # noqa: E501
        else:
            return f"Planet '{planet_name}' not found!"

    def is_planet_in_list(self, planet_name):
        """
        Checks if a planet is in the list of planets.

        Args:
            planet_name (str): The name of the planet.

        Returns:
            str: A string indicating whether the planet is in the list.
        """
        planet_name = planet_name.lower()
        self.planet_name = planet_name
        planets = self.planets
        return f"{planet_name.capitalize()} {'is' if planet_name in planets else 'is not'} in the list of planets."  # noqa: E501

    def get_moon_count(self, planet_name):
        """
        Retrieves the number of moons for a planet.

        Args:
            planet_name (str): The name of the planet.

        Returns:
            str: A string containing the number of moons or an error message if the planet is not found.  # noqa: E501
        """
        planet_name = planet_name.lower()
        self.planet_name = planet_name
        planets = self.planets
        if self.planet_name in planets:
            moon_count = len(planets[planet_name].moons)
            return f"{planets[planet_name].name} has {moon_count} moon(s)."
        else:
            return f"Planet '{planet_name}' not found!"

    def get_info(self, planet_name):
        """
        Retrieves detailed information about a planet.

        Args:
            planet_name (str): The name of the planet.

        Returns:
            str: A formatted string containing the planet's name, mass, distance from the Sun, and moons,  # noqa: E501
                 or an error message if the planet is not found.
        """
        planet_name = planet_name.lower()
        self.planet_name = planet_name
        planets = self.planets
        if self.planet_name in planets:
            return (f"Name: {planets[planet_name].name}\n"
                    f"Mass: {planets[planet_name].mass} Earth masses\n"
                    f"Distance from Sun: {planets[planet_name].distance_from_sun} million km\n"  # noqa: E501
                    f"Moons: {', '.join(planets[planet_name].moons) if planets[planet_name].moons else 'None'}")  # noqa: E501
        else:
            return f"Planet '{planet_name}' not found!"
