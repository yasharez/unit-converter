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

mainframe = ttk.Frame(root, padding='5 5 5 5')
mainframe.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

homeBtn = ttk.Button(mainframe, text='Home', default='active').grid(column=0, row=0, sticky=(N, W, E))
lengthBtn = ttk.Button(mainframe, text='Length').grid(column=1, row=0, sticky=(N, W, E))
massBtn = ttk.Button(mainframe, text='Mass').grid(column=2, row=0, sticky=(N, W, E))
volumeBtn = ttk.Button(mainframe, text='Volume').grid(column=3, row=0, sticky=(N, W, E))
tempBtn = ttk.Button(mainframe, text='Temperature').grid(column=4, row=0, sticky=(N, W, E))
currencyBtn = ttk.Button(mainframe, text='Currency').grid(column=5, row=0, sticky=(N, W, E))

conversion_frame = ttk.Frame(mainframe)
conversion_frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
conversion_frame.grid(column=0, row=1, columnspan=6, sticky=(N, W, E, S))


#########################################################
# Create widgets for length page
#########################################################

# Display instructions for user
length_label = 'Enter the value and units you would like to convert from, then select the units you would like to convert to:'
ttk.Label(conversion_frame, text=length_label).grid(column=0, row=1, columnspan=5, padx=10, pady=10)

# Create entry widget for length entry
input_length = StringVar()
input_lenght_entry = ttk.Entry(conversion_frame, textvariable=input_length)
input_lenght_entry.grid(column=0, row=2, sticky=(W, E), padx=(10, 0))

# Create combobox widget for 'from' unit
i_length_unit = StringVar()
i_length_choices = ttk.Combobox(conversion_frame, state='readonly', textvariable=i_length_unit)
i_length_choices['values'] = (' millimeters', 
                              ' meters', 
                              ' kilometers', 
                              ' inches', 
                              ' feet', 
                              ' miles')
i_length_choices.grid(column=1, row=2, sticky=(W, E), padx=(10, 0))
i_length_choices.current(0)

# Create label with '='
ttk.Label(conversion_frame, text= '=').grid(column=2, row=2, sticky=(W, E), padx=(15))

# Create label widget for converted output
output_length = StringVar()
ttk.Label(conversion_frame, textvariable=output_length).grid(column=3, row=2, sticky=(W, E), padx=(0, 10))

# Create combobox widget for 'to' unit
o_length_unit = StringVar()
o_length_choices = ttk.Combobox(conversion_frame, width=10, state='readonly', textvariable=o_length_unit)
o_length_choices['values'] = (' millimeters', 
                              ' meters', 
                              ' kilometers', 
                              ' inches', 
                              ' feet', 
                              ' miles')
o_length_choices.grid(column=4, row=2, sticky=(W, E), padx=(0, 10))
o_length_choices.current(0)

# Create button widget to calculate conversion
ttk.Button(conversion_frame, text='Convert', command=calculate_length).grid(column=1, row=3, columnspan=3, sticky=(E, W), pady=(20, 0))

root.mainloop()