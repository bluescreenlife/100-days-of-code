'''miles to km calculator app using tkinter'''
from tkinter import *

# function to call when calculate button is clicked
def button_clicked():
    miles = input.get()
    km = float(miles) * 1.609344
    label_calculation.config(text=f'{int(km)}')

# window setup
window = Tk()
window.title("Miles To KM")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

# miles input
input = Entry(width=10)
input.grid(column=1, row=0)

# miles label
label_miles = Label(text="miles", font=("Arial", 24, "bold"))
# my_label.config(text="New Text")
label_miles.grid(column=2, row=0)
label_miles.config(padx=10, pady=10)

# is equal to label
label_equal_to = Label(text="is equal to", font=("Arial", 24, "bold"))
label_equal_to.grid(column=0, row=1)
label_equal_to.config(padx=10, pady=10)

# calculated kilometers label
label_calculation = Label(text="0", font=("Arial", 24, "bold"))
# label_input.config(text="New Text")
label_calculation.grid(column=1, row=1)
label_calculation.config(padx=10, pady=10)

# kilometers label
label_km = Label(text="km", font=("Arial", 24, "bold"))
label_km.grid(column=2, row=1)
label_km.config(padx=10, pady=10)

# calculate button
button_calculate = Button(text="Calculate", command=button_clicked)
button_calculate.grid(column=1, row=2)

window.mainloop()