# Yashar Zafari
# GitHub: yasharez
# Date: 01/25/2023
# Main file for unit-converter program

# Import libraries
from tkinter import *
from tkinter import ttk

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass


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

introduction_1 =  '\n* Welcome to Unit-Converter! Your one stop shop for quick and easy unit conversions\n\n'\
                  '* Currently we support length, mass, volume, temperature, and currency conversions\n\n'\
                  '* Any new features we add in future updates will be featured on this page\n\n'\
                  '* For now, tap through the tabs at the top of this window to begin converting\n\n'

ttk.Label(main_page, text=introduction_1).grid(column=0, row=0, sticky=(N, W, E, S))#pack(expand=True, fill=BOTH)#place(relx=0.5, rely=0.5, anchor=CENTER)#.grid(column=0, row=0, sticky=(N, W, E, S))

#########################################################
# Create widgets for length page
#########################################################

input_length = StringVar()
input_lenght_entry = ttk.Entry(length_page, width=10, textvariable=input_length)
input_lenght_entry.grid(column=0, row=0, sticky=(W, E))

i_length_units = ['millimeters', 'meters', 'kilometers', 'inches', 'feet', 'miles']
i_length_option = StringVar(value=i_length_units)
i_length_choices = Listbox(length_page, listvariable=i_length_option)
i_length_choices.grid(column=1, row=0, sticky=(W, E))

ttk.Label(length_page, text= ' = ').grid(column=2, row=0, sticky=(W, E))

output_length = StringVar()
ttk.Label(length_page, text=output_length).grid(column=3, row=0, sticky=(W, E))

root.mainloop()