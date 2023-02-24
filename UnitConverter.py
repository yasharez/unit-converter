# Yashar Zafari
# GitHub: yasharez
# Date: 02/22/2023
# Main file for unit-converter program

# Import libraries
from tkinter import *
from tkinter import ttk
from functools import partial

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
    lengthBtn = ttk.Button(mainframe, text='Length', command=partial(self.__create_unit_page, conversion_frame, length_units)).grid(column=1, row=0, sticky=(N, W, E))
    massBtn = ttk.Button(mainframe, text='Mass', command=partial(self.__create_unit_page, conversion_frame, mass_units)).grid(column=2, row=0, sticky=(N, W, E))
    volumeBtn = ttk.Button(mainframe, text='Volume', command=partial(self.__create_unit_page, conversion_frame, volume_units)).grid(column=3, row=0, sticky=(N, W, E))
    tempBtn = ttk.Button(mainframe, text='Temperature', command=partial(self.__create_unit_page, conversion_frame, temperature_units)).grid(column=4, row=0, sticky=(N, W, E))
    currencyBtn = ttk.Button(mainframe, text='Currency', command=partial(self.__create_unit_page, conversion_frame, currency_units)).grid(column=5, row=0, sticky=(N, W, E))

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

  def __create_unit_page(self, conversion_frame, units):
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
    ttk.Button(conversion_frame, text='Convert', command=self.__calculate_length).grid(column=1, row=2, columnspan=3, sticky=(E, W), pady=(20, 0))

  def __calculate_length(self, *args):
    try:
        value = float(self.__input_val.get())
        self.__output_val.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        print(self.__input_unit.get(), self.__output_unit.get())
    except ValueError:
        pass

if __name__ == "__main__":
  UnitConverter()