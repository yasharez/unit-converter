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

    __input_val = ''
    __output_val = ''
    __input_unit = ''
    __output_unit = ''

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

    self.__root = Tk()
    self.__root.title("Unit Converter")

    # # Create self.__conversion_frame to put widgets in
    # self.__root.columnconfigure(0, weight=1)
    # self.__root.rowconfigure(0, weight=1)
    # self.__root.config(height=500, width=500)

    self.__mainframe = ttk.Frame(self.__root, padding='5 5 5 5')
    self.__mainframe.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    self.__mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    self.__root.columnconfigure(0, weight=1)
    self.__root.rowconfigure(0, weight=1)

    self.__conversion_frame = ttk.Frame(self.__mainframe)
    self.__conversion_frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    self.__conversion_frame.grid(column=0, row=1, columnspan=6, sticky=(N, W, E, S))

    homeBtn = ttk.Button(self.__mainframe, text='Home', default='active', command=self.__create_main_page()).grid(column=0, row=0, sticky=(N, W, E))
    lengthBtn = ttk.Button(self.__mainframe, text='Length', command=self.__create_unit_page(length_units)).grid(column=1, row=0, sticky=(N, W, E))
    massBtn = ttk.Button(self.__mainframe, text='Mass', command=self.__create_unit_page(mass_units)).grid(column=2, row=0, sticky=(N, W, E))
    volumeBtn = ttk.Button(self.__mainframe, text='Volume', command=self.__create_unit_page(volume_units)).grid(column=3, row=0, sticky=(N, W, E))
    tempBtn = ttk.Button(self.__mainframe, text='Temperature', command=self.__create_unit_page(temperature_units)).grid(column=4, row=0, sticky=(N, W, E))
    currencyBtn = ttk.Button(self.__mainframe, text='Currency', command=self.__create_unit_page(currency_units)).grid(column=5, row=0, sticky=(N, W, E))


    # # Create notebook widget to store all pages
    # self._pages = ttk.Notebook(self.__root)
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
    self.__create_main_page()



    # Start the application mainloop
    self.__root.mainloop()

  def __create_main_page(self):
    """
    Create the widgets for the main page
    """

    main_label_1 = '* Welcome to Unit-Converter! Your one stop shop for quick and easy unit conversions'
    main_label_2 = '* Currently we support length, mass, volume, temperature, and currency conversions'
    main_label_3 = '* Any new features we add in future updates will be featured on this page'
    main_label_4 = '* For now, tap through the tabs at the top of this window to begin converting'

    ttk.Label(self.__conversion_frame, text=main_label_1).grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=(10, 5))
    ttk.Label(self.__conversion_frame, text=main_label_2).grid(column=0, row=1, sticky=(N, W, E, S), padx=5, pady=5)
    ttk.Label(self.__conversion_frame, text=main_label_3).grid(column=0, row=2, sticky=(N, W, E, S), padx=5, pady=5)
    ttk.Label(self.__conversion_frame, text=main_label_4).grid(column=0, row=3, sticky=(N, W, E, S), padx=5, pady=(5, 10))

  def __create_unit_page(self, units):
    """
    Create widgets for desired unit
    """

    # Display instructions
    instruction = "Enter the value and units you would like to convert from, then select the units you would like to convert to:"
    ttk.Label(self.__conversion_frame, text=instruction).grid(column=0, row=0, columnspan=5, padx=10, pady=10)

    # Create entry widget for the unit we want converted from
    __input_val = StringVar()
    input_entry = ttk.Entry(self.__conversion_frame, textvariable=__input_val)
    input_entry.grid(column=0, row=1, sticky=(W, E), padx=(10, 0))

    # Create combobox widget for the unit we want converted from
    __input_unit = StringVar()
    input_choices = ttk.Combobox(self.__conversion_frame, state='readonly', textvariable=__input_unit)
    input_choices['values'] = units
    input_choices.grid(column=1, row=1, sticky=(W, E), padx=(10, 0))
    input_choices.current(0)

    # Create label for =
    ttk.Label(self.__conversion_frame, text= '=').grid(column=2, row=1, sticky=(W, E), padx=(15))

    # Create label widget for output value
    __output_val = StringVar()
    ttk.Label(self.__conversion_frame, textvariable=__output_val).grid(column=3, row=1, sticky=(W, E), padx=(0, 10))

    # Create combobox widget for the unit we want to convert to
    __output_unit = StringVar()
    output_choices = ttk.Combobox(self.__conversion_frame, width=10, state='readonly', textvariable=__output_unit)
    output_choices['values'] = units
    output_choices.grid(column=4, row=1, sticky=(W, E), padx=(0, 10))
    output_choices.current(0)

    # Create button widget to calculate conversion
    ttk.Button(self.__conversion_frame, text='Convert', command=self.__calculate_length).grid(column=1, row=2, columnspan=3, sticky=(E, W), pady=(20, 0))

  def __calculate_length(*args):
    try:
        value = float(__input_val.get())
        __output_val.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        print(__input_unit.get(), __output_unit.get())
    except ValueError:
        pass

if __name__ == "__main__":
  UnitConverter()