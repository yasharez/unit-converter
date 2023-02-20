# Yashar Zafari
# GitHub: yasharez
# Date: 02/22/2023
# Main file for unit-converter program

# Import libraries
from tkinter import *
from tkinter import ttk

class UnitConverter:
  """Class definition of unit conversion app"""

  def __init__(self):
    """Initialize the application"""

    self._length_units        = (' millimeters', 
                                  ' meters', 
                                  ' kilometers', 
                                  ' inches', 
                                  ' feet', 
                                  ' miles')

    self._mass_units          = (' milligrams', 
                                  ' grams', 
                                  ' kilograms', 
                                  ' ounces', 
                                  ' pounds', 
                                  ' tons')

    self._volume_units        = (' cubic millimeters', 
                                  ' cubic centimeters', 
                                  ' cubic meters', 
                                  ' cubic kilometers', 
                                  ' liters', 
                                  ' fluid ounces',
                                  ' cups',
                                  ' pints',
                                  ' quarts',
                                  ' gallons')

    self._temperature_units   = (' Celsius', 
                                  ' Fahrenheit', 
                                  ' Kelvin')

    self._currency_units      = (' USD', 
                                  ' EUR', 
                                  ' JPY', 
                                  ' MXN', 
                                  ' CNY')

    self._root = Tk()
    self._root.title("Unit Converter")

    # Create mainframe to put widgets in
    self._root.columnconfigure(0, weight=1)
    self._root.rowconfigure(0, weight=1)
    self._root.config(height=500, width=500)

    # Create notebook widget to store all pages
    self._pages = ttk.Notebook(self._root)
    self._pages.grid(column=0, row=0, sticky=(N, W, E, S))

    # Create widget frame for each unit type
    self._main_page = ttk.Frame(self._pages)
    self._main_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
    length_page = ttk.Frame(self._pages)
    length_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
    mass_page = ttk.Frame(self._pages)
    mass_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
    volume_page = ttk.Frame(self._pages)
    volume_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
    temp_page = ttk.Frame(self._pages)
    temp_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
    currency_page = ttk.Frame(self._pages)
    currency_page.columnconfigure((0, 1, 2, 3, 4), weight=1)

    # Add tabs for each unit to pages
    self._pages.add(self._main_page, text='Main')
    self._pages.add(length_page, text='Length')
    self._pages.add(mass_page, text='Mass')
    self._pages.add(volume_page, text='Volume')
    self._pages.add(temp_page, text='Temperature')
    self._pages.add(currency_page, text='Currency')

    self._create_main_page()

    self._root.mainloop()

  def _create_main_page(self):
    """
    Create the widgets for the main page
    """

    main_label_1 = '* Welcome to Unit-Converter! Your one stop shop for quick and easy unit conversions'
    main_label_2 = '* Currently we support length, mass, volume, temperature, and currency conversions'
    main_label_3 = '* Any new features we add in future updates will be featured on this page'
    main_label_4 = '* For now, tap through the tabs at the top of this window to begin converting'

    ttk.Label(self._main_page, text=main_label_1).grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=(10, 5))
    ttk.Label(self._main_page, text=main_label_2).grid(column=0, row=1, sticky=(N, W, E, S), padx=5, pady=5)
    ttk.Label(self._main_page, text=main_label_3).grid(column=0, row=2, sticky=(N, W, E, S), padx=5, pady=5)
    ttk.Label(self._main_page, text=main_label_4).grid(column=0, row=3, sticky=(N, W, E, S), padx=5, pady=(5, 10))


if __name__ == "__main__":
  UnitConverter()