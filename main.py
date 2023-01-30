# Yashar Zafari
# GitHub: yasharez
# Date: 01/25/2023
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


root = Tk()
root.title("Unit Converter")

# # Create a mainframe to put widgets in
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.config(height=500, width=500)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): 
#     child.grid_configure(padx=5, pady=5)
# feet_entry.focus()
# root.bind("<Return>", calculate)

# Create notebook widget to store all pages
pages = ttk.Notebook(root)
pages.grid(column=0, row=0, sticky=(N, W, E, S))

# Create widget frame for each unit type
main_page = ttk.Frame(pages)
length_page = ttk.Frame(pages)
mass_page = ttk.Frame(pages)
volume_page = ttk.Frame(pages)
temp_page = ttk.Frame(pages)
currency_page = ttk.Frame(pages)

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
i_length_choices['values'] = (' millimeters', 
                              ' meters', 
                              ' kilometers', 
                              ' inches', 
                              ' feet', 
                              ' miles')
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
o_length_choices['values'] = (' millimeters', 
                              ' meters', 
                              ' kilometers', 
                              ' inches', 
                              ' feet', 
                              ' miles')
o_length_choices.grid(column=4, row=1, sticky=(W, E), padx=(0, 10))
o_length_choices.current(0)

# Create button widget to calculate conversion
ttk.Button(length_page, text='Convert', command=calculate_length).grid(column=1, row=2, columnspan=3, sticky=(E, W), pady=(20, 0))

root.mainloop()