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
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

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

mainframe = ttk.Frame(root, padding='5 5 5 5')
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.columnconfigure(4, weight=1)
mainframe.columnconfigure(5, weight=1)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

homeBtn = ttk.Button(mainframe, text='Home', default='active').grid(column=0, row=1, sticky=(N, W, E))
lengthBtn = ttk.Button(mainframe, text='Length').grid(column=1, row=1, sticky=(N, W, E))
massBtn = ttk.Button(mainframe, text='Mass').grid(column=2, row=1, sticky=(N, W, E))
volumeBtn = ttk.Button(mainframe, text='Volume').grid(column=3, row=1, sticky=(N, W, E))
tempBtn = ttk.Button(mainframe, text='Temperature').grid(column=4, row=1, sticky=(N, W, E))
currencyBtn = ttk.Button(mainframe, text='Currency').grid(column=5, row=1, sticky=(N, W, E))

root.mainloop()