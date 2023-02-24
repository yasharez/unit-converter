# Yashar Zafari
# GitHub: yasharez
# Date: 02/22/2023
# Main file for unit-converter program

# Import libraries
from tkinter import *
from tkinter import ttk
from functools import partial
import client

class UnitConverter:
  """Class definition of unit conversion app"""

  def __init__(self):
    """Initialize the application"""

    self.__input_val = ''
    self.__output_val = ''
    self.__input_unit = ''
    self.__output_unit = ''

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

    length_conversions  =   {
                            'millimeters': {
                                    'millimeters': 1,
                                    'meters': 0.001,
                                    'kilometers': 0.000001,
                                    'inches': 0.0393701,
                                    'feet': 0.00328084,
                                    'miles': 0.0000006213688756
                                    },
                            'meters': {
                                    'millimeters': 1000,
                                    'meters': 1,
                                    'kilometers': 0.001,
                                    'inches': 39.3701,
                                    'feet': 3.28084,
                                    'miles': 0.0006213688756
                                    },
                            'kilometers': {
                                    'millimeters': 1000000,
                                    'meters': 1000,
                                    'kilometers': 1,
                                    'inches': 39370.1,
                                    'feet': 3280.84,
                                    'miles': 0.6213688756
                                    },
                            'inches': {
                                    'millimeters': 25.4,
                                    'meters': 0.0254,
                                    'kilometers': 0.0000254,
                                    'inches': 1,
                                    'feet': 0.083333333,
                                    'miles': 0.000015783
                                    },
                            'feet': {
                                    'millimeters': 304.8,
                                    'meters': 0.3048,
                                    'kilometers': 0.0003048,
                                    'inches': 12,
                                    'feet': 1,
                                    'miles': 0.000189394
                                    },
                            'miles': {
                                    'millimeters': 1609340,
                                    'meters': 1609.34,
                                    'kilometers': 1.60934,
                                    'inches': 63360,
                                    'feet': 5280,
                                    'miles': 1
                                    },
                            }

    volume_conversions  =   {
                            'cubic centimeters': {
                                    'cubic centimeters': 1, 
                                    'cubic meters': 0.000001, 
                                    'liters': 0.001, 
                                    'fluid ounces': 0.0338140386,
                                    'cups': 0.0042267548,
                                    'pints': 0.0021133774,
                                    'quarts': 0.0010566887,
                                    'gallons': 0.0002641722
                                    },
                            'cubic meters': {
                                    'cubic centimeters': 1000000, 
                                    'cubic meters': 1, 
                                    'liters': 1000, 
                                    'fluid ounces': 33814.038638,
                                    'cups': 4226.7548297,
                                    'pints': 2113.3774149,
                                    'quarts': 1056.6887074,
                                    'gallons': 264.17217686
                                    },
                            'liters': {
                                    'cubic centimeters': 1000, 
                                    'cubic meters': 0.001, 
                                    'liters': 1, 
                                    'fluid ounces': 33.814038638,
                                    'cups': 4.2267548297,
                                    'pints': 2.1133774149,
                                    'quarts': 1.0566887074,
                                    'gallons': 0.2641721769
                                    },
                            'fluid ounces': {
                                    'cubic centimeters': 29.573515625, 
                                    'cubic meters': 0.0000295735, 
                                    'liters': 0.0295735156, 
                                    'fluid ounces': 1,
                                    'cups': 0.125,
                                    'pints': 0.0625,
                                    'quarts': 0.03125,
                                    'gallons': 0.0078125
                                    },
                            'cups': {
                                    'cubic centimeters': 236.588125, 
                                    'cubic meters': 0.0002365881, 
                                    'liters': 0.236588125, 
                                    'fluid ounces': 8,
                                    'cups': 1,
                                    'pints': 0.5,
                                    'quarts': 0.25,
                                    'gallons': 0.0625
                                    },
                            'pints': {
                                    'cubic centimeters': 473.17625, 
                                    'cubic meters': 0.0004731763, 
                                    'liters': 0.47317625, 
                                    'fluid ounces': 16,
                                    'cups': 2,
                                    'pints': 1,
                                    'quarts': 0.5,
                                    'gallons': 0.125
                                    },
                            'quarts': {
                                    'cubic centimeters': 946.3525, 
                                    'cubic meters': 0.0009463525, 
                                    'liters': 0.9463525, 
                                    'fluid ounces': 32,
                                    'cups': 4,
                                    'pints': 2,
                                    'quarts': 1,
                                    'gallons': 0.25
                                    },
                            'gallons': {
                                    'cubic centimeters': 3785.41, 
                                    'cubic meters': 0.00378541, 
                                    'liters': 3.78541, 
                                    'fluid ounces': 128,
                                    'cups': 16,
                                    'pints': 8,
                                    'quarts': 4,
                                    'gallons': 1
                                    }
                            }

    root = Tk()
    root.title("Unit Converter")

    # # Create conversion_frame to put widgets in
    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)
    # root.config(height=500, width=500)

    mainframe = ttk.Frame(root, padding='5 5 5 5')
    mainframe.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    conversion_frame = ttk.Frame(mainframe)
    conversion_frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    conversion_frame.grid(column=0, row=1, columnspan=6, sticky=(N, W, E, S))

    homeBtn = ttk.Button(mainframe, text='Home', default='active', command=partial(self.__create_main_page, conversion_frame)).grid(column=0, row=0, sticky=(N, W, E))
    lengthBtn = ttk.Button(mainframe, text='Length', command=partial(self.__create_unit_page, conversion_frame, length_units, 'length')).grid(column=1, row=0, sticky=(N, W, E))
    massBtn = ttk.Button(mainframe, text='Mass', command=partial(self.__create_unit_page, conversion_frame, mass_units, 'mass')).grid(column=2, row=0, sticky=(N, W, E))
    volumeBtn = ttk.Button(mainframe, text='Volume', command=partial(self.__create_unit_page, conversion_frame, volume_units, 'volume')).grid(column=3, row=0, sticky=(N, W, E))
    tempBtn = ttk.Button(mainframe, text='Temperature', command=partial(self.__create_unit_page, conversion_frame, temperature_units, 'temperature')).grid(column=4, row=0, sticky=(N, W, E))
    currencyBtn = ttk.Button(mainframe, text='Currency', command=partial(self.__create_unit_page, conversion_frame, currency_units, 'currency')).grid(column=5, row=0, sticky=(N, W, E))

    # Populate each tab for units
    self.__create_main_page(conversion_frame)

    # Start the application mainloop
    root.mainloop()

  def __create_main_page(self, conversion_frame):
    """
    Create the widgets for the main page
    """

    for widget in conversion_frame.winfo_children():
      widget.destroy()

    main_label_1 = '* Welcome to Unit-Converter! Your one stop shop for quick and easy unit conversions'
    main_label_2 = '* Currently we support length, mass, volume, temperature, and currency conversions'
    main_label_3 = '* Any new features we add in future updates will be featured on this page'
    main_label_4 = '* For now, tap through the tabs at the top of this window to begin converting'

    ttk.Label(conversion_frame, text=main_label_1).grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=(10, 5))
    ttk.Label(conversion_frame, text=main_label_2).grid(column=0, row=1, sticky=(N, W, E, S), padx=5, pady=5)
    ttk.Label(conversion_frame, text=main_label_3).grid(column=0, row=2, sticky=(N, W, E, S), padx=5, pady=5)
    ttk.Label(conversion_frame, text=main_label_4).grid(column=0, row=3, sticky=(N, W, E, S), padx=5, pady=(5, 10))

  def __create_unit_page(self, conversion_frame, units, unit_type):
    """
    Create widgets for desired unit
    """

    for widget in conversion_frame.winfo_children():
      widget.destroy()

    # Display instructions
    instruction = "Enter the value and units you would like to convert from, then select the units you would like to convert to:"
    ttk.Label(conversion_frame, text=instruction).grid(column=0, row=0, columnspan=5, padx=10, pady=10)

    # Create entry widget for the unit we want converted from
    self.__input_val = StringVar()
    input_entry = ttk.Entry(conversion_frame, textvariable=self.__input_val)
    input_entry.grid(column=0, row=1, sticky=(W, E), padx=(10, 0))

    # Create combobox widget for the unit we want converted from
    self.__input_unit = StringVar()
    input_choices = ttk.Combobox(conversion_frame, state='readonly', textvariable=self.__input_unit)
    input_choices['values'] = units
    input_choices.grid(column=1, row=1, sticky=(W, E), padx=(10, 0))
    input_choices.current(0)

    # Create label for =
    ttk.Label(conversion_frame, text= '=').grid(column=2, row=1, sticky=(W, E), padx=(15))

    # Create label widget for output value
    self.__output_val = StringVar()
    ttk.Label(conversion_frame, textvariable=self.__output_val).grid(column=3, row=1, sticky=(W, E), padx=(0, 10))

    # Create combobox widget for the unit we want to convert to
    self.__output_unit = StringVar()
    output_choices = ttk.Combobox(conversion_frame, width=10, state='readonly', textvariable=self.__output_unit)
    output_choices['values'] = units
    output_choices.grid(column=4, row=1, sticky=(W, E), padx=(0, 10))
    output_choices.current(0)

    # Create button widget to calculate conversion
    ttk.Button(conversion_frame, text='Convert', command=self.__convert).grid(column=1, row=2, columnspan=3, sticky=(E, W), pady=(20, 0))

  def convert(self, *args):

      try:
          value = float(self.__input_val.get())
          from_unit = self.__input_unit.get().strip()
          to_unit = self.__output_unit.get().strip()
          self.__output_val.set(conversions[from_unit][to_unit] * value)
          print(from_unit, to_unit)
      except ValueError:
          pass

  def calculate_mass(*args):

      pass

  def calculate_volume(*args):



      pass

  def calculate_temperature(*args):

      pass

  def calculate_currency(*args):

      pass

  def randomize(*args):

      random = client.client()

if __name__ == "__main__":
  UnitConverter()