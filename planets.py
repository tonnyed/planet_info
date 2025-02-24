class Planet:
    def __init__(self, name, mass, distance_from_sun, moons):
        self.name = name
        self.mass = mass
        self.distance_from_sun = distance_from_sun
        self.moons = moons

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Mass: {self.mass} kg\n"
                f"Distance from Sun: {self.distance_from_sun} million km\n"
                f"Moons: {', '.join(self.moons) if self.moons else 'None'}")


class PlanetQuery():
    def __init__(self, load_data=False):
        # self.planets = Planet
        self.load_data = load_data
        self.planets = self.load_planets_hardcode()

        # If file is uploaded, override hard coded
        if load_data:
            self.planets = self.load_file()

    def load_file(self):
        """Reads the text file and returns its contents."""
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
        except:
            print(f"Error: The file {self.load_data} was not found.")
            return None


    def load_planets_hardcode(self):
        planets = {}
        data = [
            Planet("Mercury", 0.055, 57.9, []),
            Planet("Venus", 0.815, 108.2, []),
            Planet("Earth", 1.0, 149.6, ["Moon"]),
            Planet("Mars", 0.107, 227.9, ["Phobos", "Deimos"]),
            Planet("Jupiter", 317.8, 778.5, ["Io", "Europa", "Ganymede", "Callisto"]),
            Planet("Saturn", 95.2, 1433.5, ["Titan", "Rhea", "Iapetus", "Dione"]),
            Planet("Uranus", 14.5, 2872.5, ["Titania", "Oberon", "Umbriel", "Ariel"]),
            Planet("Neptune", 17.1, 4495.1, ["Triton", "Proteus", "Nereid"]),
            Planet("Pluto", 0.0022, 5906.4, ["Charon"])]

        for planet in data:
            name = planet.name
            mass = float(planet.mass)
            distance = float(planet.distance_from_sun)
            moons = planet.moons[4:] if len(planet.moons) > 0 else []
            planets[name.lower()] = Planet(name, mass, distance, moons)

        return planets

    def get_planet_mass(self, planet_name):
        planet_name = planet_name.lower()
        self.planet_name = planet_name
        planets = self.planets
        if self.planet_name in planets:
            return f"The mass of {planets[planet_name].name} is {planets[planet_name].mass} kg."
        else:
            return f"Planet '{planet_name}' not found!"

    def is_planet_in_list(self, planet_name):
        planet_name = planet_name.lower()
        self.planet_name = planet_name
        planets = self.planets
        return f"{planet_name.capitalize()} {'is' if planet_name in planets else 'is not'} in the list of planets."

    def get_moon_count(self, planet_name):
        planet_name = planet_name.lower()
        self.planet_name = planet_name
        planets = self.planets
        if self.planet_name in planets:
            moon_count = len(planets[planet_name].moons)
            return f"{planets[planet_name].name} has {moon_count} moon(s)."
        else:
            return f"Planet '{planet_name}' not found!"


    def get_info(self, planet_name):
        planet_name = planet_name.lower()
        self.planet_name = planet_name
        planets = self.planets
        if self.planet_name in planets:
            return (f"Name: {planets[planet_name].name}\n"
                    f"Mass: {planets[planet_name].mass} Earth masses\n"
                    f"Distance from Sun: {planets[planet_name].distance_from_sun} million km\n"
                    f"Moons: {', '.join(planets[planet_name].moons) if planets[planet_name].moons else 'None'}")
        else:
            return f"Planet '{planet_name}' not found!"

# def load_planets():
#     with open("data/planets.json", "r") as file:
#         data = json.load(file)
#     return [Planet(**planet) for planet in data]