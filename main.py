# Yashar Zafari
# GitHub: yasharez
# Date: 02/21/2023
# Main file for unit-converter program

# Import libraries
from tkinter import *
from tkinter import ttk

def calculate_length(*args):
    try:
        value = float(input_length.get())
        output_length.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        print(i_length_unit.get(), o_length_unit.get())
    except ValueError:
        pass


length_units        =   (' millimeters', 
                        ' meters', 
                        ' kilometers', 
                        ' inches', 
                        ' feet', 
                        ' miles')

mass_units          =   (' milligrams', 
                        ' grams', 
                        ' kilograms', 
                        ' ounces', 
                        ' pounds', 
                        ' tons')

volume_units        =   (' cubic millimeters', 
                        ' cubic centimeters', 
                        ' cubic meters', 
                        ' cubic kilometers', 
                        ' liters', 
                        ' fluid ounces',
                        ' cups',
                        ' pints',
                        ' quarts',
                        ' gallons')

temperature_units   =   (' Celsius', 
                        ' Fahrenheit', 
                        ' Kelvin')

currency_units      =   (' USD', 
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

root = Tk()
root.title("Unit Converter")

# # Create a mainframe to put widgets in
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.config(height=500, width=500)

# Create notebook widget to store all pages
pages = ttk.Notebook(root)
pages.grid(column=0, row=0, sticky=(N, W, E, S))

# Create widget frame for each unit type
main_page = ttk.Frame(pages)
main_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
length_page = ttk.Frame(pages)
length_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
mass_page = ttk.Frame(pages)
mass_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
volume_page = ttk.Frame(pages)
volume_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
temp_page = ttk.Frame(pages)
temp_page.columnconfigure((0, 1, 2, 3, 4), weight=1)
currency_page = ttk.Frame(pages)
currency_page.columnconfigure((0, 1, 2, 3, 4), weight=1)

# Add tabs for each unit to pages
pages.add(main_page, text='Main')
pages.add(length_page, text='Length')
pages.add(mass_page, text='Mass')
pages.add(volume_page, text='Volume')
pages.add(temp_page, text='Temperature')
pages.add(currency_page, text='Currency')

#########################################################
# Create widgets for main page
#########################################################

main_label_1 = '* Welcome to Unit-Converter! Your one stop shop for quick and easy unit conversions'
main_label_2 = '* Currently we support length, mass, volume, temperature, and currency conversions'
main_label_3 = '* Any new features we add in future updates will be featured on this page'
main_label_4 = '* For now, tap through the tabs at the top of this window to begin converting'

ttk.Label(main_page, text=main_label_1).grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=(10, 5))
ttk.Label(main_page, text=main_label_2).grid(column=0, row=1, sticky=(N, W, E, S), padx=5, pady=5)
ttk.Label(main_page, text=main_label_3).grid(column=0, row=2, sticky=(N, W, E, S), padx=5, pady=5)
ttk.Label(main_page, text=main_label_4).grid(column=0, row=3, sticky=(N, W, E, S), padx=5, pady=(5, 10))

#########################################################
# Create widgets for length page
#########################################################

# Display instructions for user
length_label = 'Enter the value and units you would like to convert from, then select the units you would like to convert to:'
ttk.Label(length_page, text=length_label).grid(column=0, row=0, columnspan=5, padx=10, pady=10)

# Create entry widget for length entry
input_length = StringVar()
input_lenght_entry = ttk.Entry(length_page, textvariable=input_length)
input_lenght_entry.grid(column=0, row=1, sticky=(W, E), padx=(10, 0))

# Create combobox widget for 'from' unit
i_length_unit = StringVar()
i_length_choices = ttk.Combobox(length_page, state='readonly', textvariable=i_length_unit)
i_length_choices['values'] = length_units
i_length_choices.grid(column=1, row=1, sticky=(W, E), padx=(10, 0))
i_length_choices.current(0)

# Create label with '='
ttk.Label(length_page, text= '=').grid(column=2, row=1, sticky=(W, E), padx=(15))

# Create label widget for converted output
output_length = StringVar()
ttk.Label(length_page, textvariable=output_length).grid(column=3, row=1, sticky=(W, E), padx=(0, 10))

# Create combobox widget for 'to' unit
o_length_unit = StringVar()
o_length_choices = ttk.Combobox(length_page, width=10, state='readonly', textvariable=o_length_unit)
o_length_choices['values'] = length_units
o_length_choices.grid(column=4, row=1, sticky=(W, E), padx=(0, 10))
o_length_choices.current(0)

# Create button widget to calculate conversion
ttk.Button(length_page, text='Convert', command=calculate_length).grid(column=1, row=2, columnspan=3, sticky=(E, W), pady=(20, 0))

#########################################################
# Create widgets for mass page
#########################################################

# Display instructions for user
mass_label = 'Enter the value and units you would like to convert from, then select the units you would like to convert to:'
ttk.Label(mass_page, text=mass_label).grid(column=0, row=0, columnspan=5, padx=10, pady=10)

# Create entry widget for mass entry
input_mass = StringVar()
input_mass_entry = ttk.Entry(mass_page, textvariable=input_mass)
input_mass_entry.grid(column=0, row=1, sticky=(W, E), padx=(10, 0))

# Create combobox widget for 'from' unit
i_mass_unit = StringVar()
i_mass_choices = ttk.Combobox(mass_page, state='readonly', textvariable=i_mass_unit)
i_mass_choices['values'] = mass_units
i_mass_choices.grid(column=1, row=1, sticky=(W, E), padx=(10, 0))
i_mass_choices.current(0)

# Create label with '='
ttk.Label(mass_page, text= '=').grid(column=2, row=1, sticky=(W, E), padx=(15))

# Create label widget for converted output
output_mass = StringVar()
ttk.Label(mass_page, textvariable=output_mass).grid(column=3, row=1, sticky=(W, E), padx=(0, 10))

# Create combobox widget for 'to' unit
o_mass_unit = StringVar()
o_mass_choices = ttk.Combobox(mass_page, width=10, state='readonly', textvariable=o_mass_unit)
o_mass_choices['values'] = mass_units
o_mass_choices.grid(column=4, row=1, sticky=(W, E), padx=(0, 10))
o_mass_choices.current(0)

# Create button widget to calculate conversion
ttk.Button(mass_page, text='Convert', command=calculate_length).grid(column=1, row=2, columnspan=3, sticky=(E, W), pady=(20, 0))

#########################################################
# Create widgets for volume page
#########################################################

# Display instructions for user
volume_label = 'Enter the value and units you would like to convert from, then select the units you would like to convert to:'
ttk.Label(volume_page, text=volume_label).grid(column=0, row=0, columnspan=5, padx=10, pady=10)

# Create entry widget for mass entry
input_volume = StringVar()
input_volume_entry = ttk.Entry(volume_page, textvariable=input_volume)
input_volume_entry.grid(column=0, row=1, sticky=(W, E), padx=(10, 0))

# Create combobox widget for 'from' unit
i_volume_unit = StringVar()
i_volume_choices = ttk.Combobox(volume_page, state='readonly', textvariable=i_volume_unit)
i_volume_choices['values'] = volume_units
i_volume_choices.grid(column=1, row=1, sticky=(W, E), padx=(10, 0))
i_volume_choices.current(0)

# Create label with '='
ttk.Label(volume_page, text= '=').grid(column=2, row=1, sticky=(W, E), padx=(15))

# Create label widget for converted output
output_volume = StringVar()
ttk.Label(volume_page, textvariable=output_volume).grid(column=3, row=1, sticky=(W, E), padx=(0, 10))

# Create combobox widget for 'to' unit
o_volume_unit = StringVar()
o_volume_choices = ttk.Combobox(volume_page, width=10, state='readonly', textvariable=o_volume_unit)
o_volume_choices['values'] = volume_units
o_volume_choices.grid(column=4, row=1, sticky=(W, E), padx=(0, 10))
o_volume_choices.current(0)

# Create button widget to calculate conversion
ttk.Button(volume_page, text='Convert', command=calculate_length).grid(column=1, row=2, columnspan=3, sticky=(E, W), pady=(20, 0))

#########################################################
# Create widgets for temperature page
#########################################################

# Display instructions for user
temp_label = 'Enter the value and units you would like to convert from, then select the units you would like to convert to:'
ttk.Label(temp_page, text=temp_label).grid(column=0, row=0, columnspan=5, padx=10, pady=10)

# Create entry widget for mass entry
input_temp = StringVar()
input_temp_entry = ttk.Entry(temp_page, textvariable=input_temp)
input_temp_entry.grid(column=0, row=1, sticky=(W, E), padx=(10, 0))

# Create combobox widget for 'from' unit
i_temp_unit = StringVar()
i_temp_choices = ttk.Combobox(temp_page, state='readonly', textvariable=i_temp_unit)
i_temp_choices['values'] = temperature_units
i_temp_choices.grid(column=1, row=1, sticky=(W, E), padx=(10, 0))
i_temp_choices.current(0)

# Create label with '='
ttk.Label(temp_page, text= '=').grid(column=2, row=1, sticky=(W, E), padx=(15))

# Create label widget for converted output
output_temp = StringVar()
ttk.Label(temp_page, textvariable=output_temp).grid(column=3, row=1, sticky=(W, E), padx=(0, 10))

# Create combobox widget for 'to' unit
o_temp_unit = StringVar()
o_temp_choices = ttk.Combobox(temp_page, width=10, state='readonly', textvariable=o_temp_unit)
o_temp_choices['values'] = temperature_units
o_temp_choices.grid(column=4, row=1, sticky=(W, E), padx=(0, 10))
o_temp_choices.current(0)

# Create button widget to calculate conversion
ttk.Button(temp_page, text='Convert', command=calculate_length).grid(column=1, row=2, columnspan=3, sticky=(E, W), pady=(20, 0))

#########################################################
# Create widgets for currency page
#########################################################

# Display instructions for user
currency_label = 'Enter the value and units you would like to convert from, then select the units you would like to convert to:'
ttk.Label(currency_page, text=currency_label).grid(column=0, row=0, columnspan=5, padx=10, pady=10)

# Create entry widget for mass entry
input_currency = StringVar()
input_currency_entry = ttk.Entry(currency_page, textvariable=input_currency)
input_currency_entry.grid(column=0, row=1, sticky=(W, E), padx=(10, 0))

# Create combobox widget for 'from' unit
i_currency_unit = StringVar()
i_currency_choices = ttk.Combobox(currency_page, state='readonly', textvariable=i_currency_unit)
i_currency_choices['values'] = currency_units
i_currency_choices.grid(column=1, row=1, sticky=(W, E), padx=(10, 0))
i_currency_choices.current(0)

# Create label with '='
ttk.Label(currency_page, text= '=').grid(column=2, row=1, sticky=(W, E), padx=(15))

# Create label widget for converted output
output_currency = StringVar()
ttk.Label(currency_page, textvariable=output_currency).grid(column=3, row=1, sticky=(W, E), padx=(0, 10))

# Create combobox widget for 'to' unit
o_currency_unit = StringVar()
o_currency_choices = ttk.Combobox(currency_page, width=10, state='readonly', textvariable=o_currency_unit)
o_currency_choices['values'] = currency_units
o_currency_choices.grid(column=4, row=1, sticky=(W, E), padx=(0, 10))
o_currency_choices.current(0)

# Create button widget to calculate conversion
ttk.Button(currency_page, text='Convert', command=calculate_length).grid(column=1, row=2, columnspan=3, sticky=(E, W), pady=(20, 0))

root.mainloop()