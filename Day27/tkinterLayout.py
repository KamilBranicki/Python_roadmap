from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Labels
label = Label(text="This is text")
# label.pack(side="left")
# label.place(x = 100, y = 200)
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

#Buttons
button = Button(text="Click Me")
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="Click Me 2")
# button.pack()
new_button.grid(column=2, row=0)

#Entries
entry = Entry(width=30)
# entry.pack()
entry.grid(column=3, row=2)


window.mainloop()
