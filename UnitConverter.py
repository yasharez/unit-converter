# Yashar Zafari
# GitHub: yasharez
# Date: 02/23/2023
# Main file for unit-converter program

# Import libraries
from tkinter import *
from tkinter import ttk
from functools import partial
import client
import json

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

    volume_units        = (' cubic centimeters', 
                                  ' cubic meters', 
                                  ' liters', 
                                  ' fluid ounces',
                                  ' cups',
                                  ' pints',
                                  ' quarts',
                                  ' gallons')

    temperature_units   = (' Celsius', 
                                  ' Fahrenheit', 
                                  ' Kelvin')

    currency_units      = (' United States Dollar', 
                                  ' Euro', 
                                  ' Japanese Yen', 
                                  ' Mexican Peso', 
                                  ' Chinese Yuan',
                                  ' Canadian Dollar')

    # Open JSON file and import conversion values
    f = open('conversions.json')
    self.__conversions = json.load(f)

    # Create Tkinter root
    root = Tk()
    root.title("Unit Converter")

    # Create mainframe to hold navigation buttons
    mainframe = ttk.Frame(root, padding='5 5 5 5')
    mainframe.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create frame to hold each unit conversion page
    conversion_frame = ttk.Frame(mainframe)
    conversion_frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    conversion_frame.grid(column=0, row=1, columnspan=6, sticky=(N, W, E, S))

    # Create navigation button for each unit
    homeBtn = ttk.Button(mainframe, text='Home', default='active', command=partial(self.__create_main_page, conversion_frame)).grid(column=0, row=0, sticky=(N, W, E))
    lengthBtn = ttk.Button(mainframe, text='Length', command=partial(self.__create_unit_page, conversion_frame, length_units, 'length')).grid(column=1, row=0, sticky=(N, W, E))
    massBtn = ttk.Button(mainframe, text='Mass', command=partial(self.__create_unit_page, conversion_frame, mass_units, 'mass')).grid(column=2, row=0, sticky=(N, W, E))
    volumeBtn = ttk.Button(mainframe, text='Volume', command=partial(self.__create_unit_page, conversion_frame, volume_units, 'volume')).grid(column=3, row=0, sticky=(N, W, E))
    tempBtn = ttk.Button(mainframe, text='Temperature', command=partial(self.__create_unit_page, conversion_frame, temperature_units, 'temperature')).grid(column=4, row=0, sticky=(N, W, E))
    currencyBtn = ttk.Button(mainframe, text='Currency', command=partial(self.__create_unit_page, conversion_frame, currency_units, 'currency')).grid(column=5, row=0, sticky=(N, W, E))

    # Populate the main application page
    self.__create_main_page(conversion_frame)

    # Start the application mainloop
    root.mainloop()

  def __create_main_page(self, conversion_frame):
    """
    Create the widgets for the main page
    """

    for widget in conversion_frame.winfo_children():
      widget.destroy()

    label_1_str = '* Welcome to Unit-Converter! Your one stop shop for quick and easy unit conversions'
    label_2_str = "* NEW FEATURE: Randomize button! On each page you will see a button labeled 'Random'\n"\
                    '   Press it to randomly generate a number for you to convert from!'
    label_3_str = '* Currently we support length, mass, volume, temperature, and currency conversions'
    label_4_str = '* For now, tap through the tabs at the top of this window to begin converting'

    label_1 = ttk.Label(conversion_frame, text=label_1_str).grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=(10, 5))
    label_2 = ttk.Label(conversion_frame, text=label_2_str).grid(column=0, row=1, sticky=(N, W, E, S), padx=5, pady=5)
    label_3 = ttk.Label(conversion_frame, text=label_3_str).grid(column=0, row=2, sticky=(N, W, E, S), padx=5, pady=5)
    label_4 = ttk.Label(conversion_frame, text=label_4_str).grid(column=0, row=3, sticky=(N, W, E, S), padx=5, pady=(5, 10))

  def __create_unit_page(self, conversion_frame, units, unit_type):
    """
    Create widgets for desired unit
    """

    for widget in conversion_frame.winfo_children():
      widget.destroy()

    self.__unit_type = unit_type

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
    output_choices = ttk.Combobox(conversion_frame, state='readonly', textvariable=self.__output_unit)
    output_choices['values'] = units
    output_choices.grid(column=4, row=1, sticky=(W, E), padx=(0, 10))
    output_choices.current(0)

    # Create button widget to insert random number for user
    ttk.Button(conversion_frame, text='Random', command=self.__randomize).grid(column=0, row=2, sticky=(E, W), pady=(20,0), padx=(10,5))

    # Create button widget to calculate conversion
    ttk.Button(conversion_frame, text='Convert', command=self.__convert).grid(column=1, row=2, columnspan=4, sticky=(E, W), pady=(20, 0), padx=(5, 10))

  def __convert(self, *args):
    """Convert the input value from the specified unit to the other specified unit"""
    try:
        value = float(self.__input_val.get())
        from_unit = self.__input_unit.get().strip()
        to_unit = self.__output_unit.get().strip()
        
        # Special equation conversions for temperature units
        if self.__unit_type == 'temperature':
          if from_unit == 'Celsius':
            output = self.__convert_c(value, to_unit)
          elif from_unit == 'Fahrenheit':
            output = self.__convert_f(value, to_unit)
          elif from_unit == 'Kelvin':
            output = self.__convert_k(value, to_unit)
          self.__output_val.set(output)
        else:
          self.__output_val.set(self.__conversions[self.__unit_type][from_unit][to_unit] * value)
    except ValueError:
        pass

  def __randomize(self, *args):
    """Returns a random value from partner's microservice"""
    random = client.client()
    self.__input_val.set(float(random))

  def __convert_c(self, value, to_unit):
    """Helper method to convert from Celsius"""
    if to_unit == 'Fahrenheit':
      return self.__c_to_f(value)
    elif to_unit == 'Kelvin':
      return self.__c_to_k(value)
    else:
      return value

  def __convert_f(self, value, to_unit):
    """Helper method to convert from Fahrenheit"""
    if to_unit == 'Celsius':
      return self.__f_to_c(value)
    elif to_unit == 'Kelvin':
      return self.__f_to_k(value)
    else:
      return value

  def __convert_k(self, value, to_unit):
    """Helper method to convert from Kelvin"""
    if to_unit == 'Celsius':
      return self.__k_to_c(value)
    elif to_unit == 'Fahrenheit':
      return self.__k_to_f(value)
    else:
      return value

  def __c_to_f(self, c):
    """Convert from Celsius to Fahrenheit"""
    return (c * 9 / 5) + 32

  def __f_to_c(self, f):
    """Convert from Fahrenheit to Celsius"""
    return (f - 32) * 5 / 9

  def __k_to_f(self, k):
    """Convert from Kelvin to Fahrenheit"""
    return self.__c_to_f(self.__k_to_c(k))

  def __f_to_k(self, f):
    """Convert from Fahrenheit to Kelvin"""
    return self.__c_to_k(self.__f_to_c(f))

  def __c_to_k(self, c):
    """Convert from Celsius to Kelvin"""
    return  c + 273.15

  def __k_to_c(self, k):
    """Convert from Kelvin to Celsius"""
    return k - 273.15

if __name__ == "__main__":
  UnitConverter()