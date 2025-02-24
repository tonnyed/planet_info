import tkinter as tk
from planets import PlanetQuery


class PlanetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solar System Information")
        self.planets = PlanetQuery("data/planets.txt")

        # Menu
        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        self.planet_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Planets", menu=self.planet_menu)
        self.planet_menu.add_command(label="Query Planet", command=self.query_planet)  # noqa: E501
        self.planet_menu.add_command(label="Exit", command=root.quit)

        # Main Frame # noqa: E731
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Please Enter Planet Name:")
        self.label.grid(row=0, column=0, padx=10)

        self.entry = tk.Entry(self.frame, width=60)
        self.entry.grid(row=0, column=1, padx=10)

        self.search_button = tk.Button(self.frame, text="Search", command=self.display_planet_info)  # noqa: E501
        self.search_button.grid(row=0, column=2, padx=10)

        self.result = tk.Label(self.frame, text="", justify=tk.LEFT)
        self.result.grid(row=1, column=0, columnspan=3, pady=10)

        # Query Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.info_button = tk.Button(self.button_frame, text="Tell me everything about", command=self.show_planet_info)  # noqa: E501
        self.info_button.grid(row=0, column=0, padx=5)

        self.mass_button = tk.Button(self.button_frame, text="Planet Size...?", command=self.show_planet_mass)  # noqa: E501
        self.mass_button.grid(row=0, column=1, padx=5)

        self.list_button = tk.Button(self.button_frame, text="check if this is a planet ?", command=self.check_planet_in_list)  # noqa: E501
        self.list_button.grid(row=0, column=2, padx=5)

        self.moon_button = tk.Button(self.button_frame, text="How many moons does this planet have?", command=self.show_moon_count)  # noqa: E501
        self.moon_button.grid(row=0, column=3, padx=5)

    def query_planet(self):
        planet_name = self.entry.get().strip()
        result = PlanetQuery.get_info(self.planets, planet_name)
        self.result.config(text=result)

    def display_planet_info(self):
        self.query_planet()

    def show_planet_info(self):
        planet_name = self.entry.get().strip()
        result = PlanetQuery.get_info(self.planets, planet_name)
        self.result.config(text=result)

    def show_planet_mass(self):
        planet_name = self.entry.get().strip()
        result = PlanetQuery.get_planet_mass(self.planets, planet_name)
        self.result.config(text=result)

    def check_planet_in_list(self):
        planet_name = self.entry.get().strip()
        result = PlanetQuery.is_planet_in_list(self.planets, planet_name)
        self.result.config(text=result)

    def show_moon_count(self):
        planet_name = self.entry.get().strip()
        result = PlanetQuery.get_moon_count(self.planets, planet_name)
        self.result.config(text=result)
