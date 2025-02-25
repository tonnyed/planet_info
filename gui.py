import tkinter as tk
from planets import PlanetQuery


class PlanetApp:
    """
    A Tkinter-based GUI application for querying and displaying information about planets in the solar system.  # noqa: E501

    Attributes:
        root (tk.Tk): The main window of the application.
        planets (PlanetQuery): An instance of the PlanetQuery class to interact with planet data.  # noqa: E501
        menu (tk.Menu): The menu bar for the application.
        frame (tk.Frame): The main frame containing input and result widgets.
        button_frame (tk.Frame): A frame containing buttons for specific queries.  # noqa: E501
    """

    def __init__(self, root):
        """
        Initializes the PlanetApp GUI.

        Args:
            root (tk.Tk): The root window for the Tkinter application.
        """
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

        # Main Frame
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
        """
        Queries the planet information based on the name entered in the input field.  # noqa: E501
        Updates the result label with the retrieved information.
        """
        planet_name = self.entry.get().strip()
        result = PlanetQuery.get_info(self.planets, planet_name)
        self.result.config(text=result)

    def display_planet_info(self):
        """
        Displays the planet information by calling the `query_planet` method.
        """
        self.query_planet()

    def show_planet_info(self):
        """
        Displays detailed information about the planet entered in the input field.  # noqa: E501
        """
        planet_name = self.entry.get().strip()
        result = PlanetQuery.get_info(self.planets, planet_name)
        self.result.config(text=result)

    def show_planet_mass(self):
        """
        Displays the mass of the planet entered in the input field.
        """
        planet_name = self.entry.get().strip()
        result = PlanetQuery.get_planet_mass(self.planets, planet_name)
        self.result.config(text=result)

    def check_planet_in_list(self):
        """
        Checks if the entered planet name exists in the list of planets.
        Updates the result label with a confirmation message.
        """
        planet_name = self.entry.get().strip()
        result = PlanetQuery.is_planet_in_list(self.planets, planet_name)
        self.result.config(text=result)

    def show_moon_count(self):
        """
        Displays the number of moons for the planet entered in the input field.
        """
        planet_name = self.entry.get().strip()
        result = PlanetQuery.get_moon_count(self.planets, planet_name)
        self.result.config(text=result)
