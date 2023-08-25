from tkinter import *

def convert():
    miles = float(entry.get())
    result = round(miles * 1.609,2)
    result_label.config(text=result)

window = Tk()
window.minsize(width=280, height=100)
window.title("Miles to Km App")
window.config(padx= 40, pady=10)

entry = Entry(width=10)
entry.insert(END, "0")
entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)
equal_label.config(padx=10, pady=10)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calc_button = Button(text="Calculate", command=convert)
calc_button.grid(row=2, column=1)

window.mainloop()