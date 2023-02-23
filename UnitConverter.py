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

    self._input_val = ''
    self._output_val = ''
    self._input_unit = ''
    self._output_unit = ''

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

    # # Create self._conversion_frame to put widgets in
    # self._root.columnconfigure(0, weight=1)
    # self._root.rowconfigure(0, weight=1)
    # self._root.config(height=500, width=500)

    self._conversion_frame = ttk.Frame(self._root, padding='5 5 5 5')
    self._conversion_frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    self._conversion_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    self._root.columnconfigure(0, weight=1)
    self._root.rowconfigure(0, weight=1)

    homeBtn = ttk.Button(self._conversion_frame, text='Home', default='active').grid(column=0, row=0, sticky=(N, W, E))
    lengthBtn = ttk.Button(self._conversion_frame, text='Length').grid(column=1, row=0, sticky=(N, W, E))
    massBtn = ttk.Button(self._conversion_frame, text='Mass').grid(column=2, row=0, sticky=(N, W, E))
    volumeBtn = ttk.Button(self._conversion_frame, text='Volume').grid(column=3, row=0, sticky=(N, W, E))
    tempBtn = ttk.Button(self._conversion_frame, text='Temperature').grid(column=4, row=0, sticky=(N, W, E))
    currencyBtn = ttk.Button(self._conversion_frame, text='Currency').grid(column=5, row=0, sticky=(N, W, E))

    self._conversion_frame = ttk.Frame(self._conversion_frame)
    self._conversion_frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    self._conversion_frame.grid(column=0, row=1, columnspan=6, sticky=(N, W, E, S))

    # # Create notebook widget to store all pages
    # self._pages = ttk.Notebook(self._root)
    # self._pages.grid(column=0, row=0, sticky=(N, W, E, S))

    # # Create widget frame for each unit type
    # self._main_page = ttk.Frame(self._pages)
    # self._main_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
    # length_page = ttk.Frame(self._pages)
    # length_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
    # mass_page = ttk.Frame(self._pages)
    # mass_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
    # volume_page = ttk.Frame(self._pages)
    # volume_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
    # temperature_page = ttk.Frame(self._pages)
    # temperature_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
    # currency_page = ttk.Frame(self._pages)
    # currency_page.columnconfigure((0, 1, 2, 3, 4), weight=1)

    # # Add tabs for each unit to pages
    # self._pages.add(self._main_page, text='Main')
    # self._pages.add(length_page, text='Length')
    # self._pages.add(mass_page, text='Mass')
    # self._pages.add(volume_page, text='Volume')
    # self._pages.add(temperature_page, text='Temperature')
    # self._pages.add(currency_page, text='Currency')

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

    ttk.Label(self._conversion_frame, text=main_label_1).grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=(10, 5))
    ttk.Label(self._conversion_frame, text=main_label_2).grid(column=0, row=1, sticky=(N, W, E, S), padx=5, pady=5)
    ttk.Label(self._conversion_frame, text=main_label_3).grid(column=0, row=2, sticky=(N, W, E, S), padx=5, pady=5)
    ttk.Label(self._conversion_frame, text=main_label_4).grid(column=0, row=3, sticky=(N, W, E, S), padx=5, pady=(5, 10))

  def _create_unit_page(self, page, units):
    """
    Create widgets for desired unit
    """

    # Display instructions
    instruction = "Enter the value and units you would like to convert from, then select the units you would like to convert to:"
    ttk.Label(page, text=instruction).grid(column=0, row=0, columnspan=5, padx=10, pady=10)

    # Create entry widget for the unit we want converted from
    self._input_val = StringVar()
    input_entry = ttk.Entry(page, textvariable=self._input_val)
    input_entry.grid(column=0, row=1, sticky=(W, E), padx=(10, 0))

    # Create combobox widget for the unit we want converted from
    self._input_unit = StringVar()
    input_choices = ttk.Combobox(page, state='readonly', textvariable=self._input_unit)
    input_choices['values'] = units
    input_choices.grid(column=1, row=1, sticky=(W, E), padx=(10, 0))
    input_choices.current(0)

    # Create label for =
    ttk.Label(page, text= '=').grid(column=2, row=1, sticky=(W, E), padx=(15))

    # Create label widget for output value
    self._output_val = StringVar()
    ttk.Label(page, textvariable=self._output_val).grid(column=3, row=1, sticky=(W, E), padx=(0, 10))

    # Create combobox widget for the unit we want to convert to
    self._output_unit = StringVar()
    output_choices = ttk.Combobox(page, width=10, state='readonly', textvariable=self._output_unit)
    output_choices['values'] = units
    output_choices.grid(column=4, row=1, sticky=(W, E), padx=(0, 10))
    output_choices.current(0)

    # Create button widget to calculate conversion
    ttk.Button(page, text='Convert', command=self._calculate_length).grid(column=1, row=2, columnspan=3, sticky=(E, W), pady=(20, 0))

  def _calculate_length(*args):
    try:
        value = float(self._input_val.get())
        self._output_val.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        print(self._input_unit.get(), self._output_unit.get())
    except ValueError:
        pass

if __name__ == "__main__":
  UnitConverter()