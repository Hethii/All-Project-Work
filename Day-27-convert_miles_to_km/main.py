# my code for day 27
from tkinter import *


def miles_to_km():
    """for converting miles to km when calculate is clicked"""
    miles_value = int(miles_input.get())
    # print(miles_value * 2)
    # result = round(miles_value * 1.609344)
    km_result_label.config(text=f"{round(miles_value * 1.609644)}")


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(200, 100)
window.config(pady=20, padx=20)

# takes in input values
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# takes in label values
equal_label = Label(text="is equal to", font=("Arial", 15, "bold"))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10)

miles_label = Label(text="Miles", font=("Arial", 15, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10)

km_label = Label(text="Km", font=("Arial", 15, "bold"))
km_label.grid(column=2, row=1)

km_result_label = Label(text=0, font=("Arial", 15, "bold"))
km_result_label.grid(column=1, row=1)

# takes in click button operations and is changes the values in km_result_label when chnaged
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)


window.mainloop()
