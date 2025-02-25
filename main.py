from gui import PlanetApp
import tkinter as tk

if __name__ == "__main__":
    """
    Main entry point for application.

    This script initializes the Tkinter root window and launches the `PlanetApp` GUI,  # noqa: E501
    allowing users to interactively query and display information about planets.  # noqa: E501
    """
    root = tk.Tk()  # Create the main Tkinter window
    app = PlanetApp(root)  # Initialize the PlanetApp GUI
    root.mainloop()  # Start the Tkinter event loop
