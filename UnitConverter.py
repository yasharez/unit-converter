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

    length_units        = (' millimeters', 
                                  ' meters', 
                                  ' kilometers', 
                                  ' inches', 
                                  ' feet', 
                                  ' miles')

    mass_units          = (' milligrams', 
                                  ' grams', 
                                  ' kilograms', 
                                  ' ounces', 
                                  ' pounds', 
                                  ' tons')

    volume_units        = (' cubic millimeters', 
                                  ' cubic centimeters', 
                                  ' cubic meters', 
                                  ' cubic kilometers', 
                                  ' liters', 
                                  ' fluid ounces',
                                  ' cups',
                                  ' pints',
                                  ' quarts',
                                  ' gallons')

    temperature_units   = (' Celsius', 
                                  ' Fahrenheit', 
                                  ' Kelvin')

    currency_units      = (' USD', 
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

    # Populate each tab for units
    self._create_main_page()


    # Start the application mainloop
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

  def _create_unit_page(self, page, units):
    """
    Create widgets for desired unit
    """

    # Display instructions
    instruction = "Enter the value and units you would like to convert from, then select the units you would like to convert to:"
    ttk.Label(page, text=instruction).grid(column=0, row=0, columnspan=5, padx=10, pady=10)

    # Create entry widget for the unit we want converted from
    input_val = StringVar()
    input_entry = ttk.Entry(page, textvariable=input_val)
    input_entry.grid(column=0, row=1, sticky=(W, E), padx=(10, 0))

    # Create combobox widget for the unit we want converted from
    input_unit = StringVar()
    input_choices = ttk.Combobox(page, state='readonly', textvariable=input_unit)
    input_choices['values'] = units
    input_choices.grid(column=1, row=1, sticky=(W, E), padx=(10, 0))
    input_choices.current(0)

    # Create label for =
    ttk.Label(page, text= '=').grid(column=2, row=1, sticky=(W, E), padx=(15))

    # Create label widget for output value
    output_val = StringVar()
    ttk.Label(page, textvariable=output_val).grid(column=3, row=1, sticky=(W, E), padx=(0, 10))

    # Create combobox widget for the unit we want to convert to
    output_unit = StringVar()
    output_choices = ttk.Combobox(page, width=10, state='readonly', textvariable=output_unit)
    output_choices['values'] = units
    output_choices.grid(column=4, row=1, sticky=(W, E), padx=(0, 10))
    output_choices.current(0)

    # Create button widget to calculate conversion
    ttk.Button(page, text='Convert', command=self._calculate_length).grid(column=1, row=2, columnspan=3, sticky=(E, W), pady=(20, 0))

  def _calculate_length(*args):
    try:
        value = float(input_val.get())
        output_val.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        print(input_unit.get(), output_unit.get())
    except ValueError:
        pass

if __name__ == "__main__":
  UnitConverter()