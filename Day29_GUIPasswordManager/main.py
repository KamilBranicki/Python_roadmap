from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
FONT_NAME = "Courier"
count = 2
timer = None
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pass_generator():
    pass_insert.delete(0, END)

    pass_letters = [random.choice(letters) for n in range(random.randint(8, 10))]

    pass_symbols = [random.choice(symbols) for n in range(random.randint(2, 4))]

    pass_numbers = [random.choice(numbers) for n in range(random.randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    
    pass_insert.insert(END, password)
    pyperclip.copy(password)

    copy_label.config(text="Your password was\ncopied to clipboard")
    count_down(count)

def count_down(count):
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        copy_label.config(text="")
        count = 2
        window.after_cancel(timer)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_insert.get()
    email = user_mail_insert.get()
    password = pass_insert.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("C:\\Python\\Projects\\Day29\\data.text", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            web_insert.delete(0, END)
            pass_insert.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=30 )

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="C:\Python\Projects\Day29\\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:" )
web_label.grid(row=1, column=0)
web_label.config(padx=8)

user_mail_label = Label(text="Email/Username:" )
user_mail_label.grid(row=2, column=0)
user_mail_label.config(padx=8)

pass_label = Label(text="Password:" )
pass_label.grid(row=3, column=0)
pass_label.config(padx=8)

copy_label = Label(text=" \n ")
copy_label.grid(row=5, column=1)
copy_label.config(padx=8)

add_buttton = Button(text="Add", width=43, highlightthickness=0, command=save_data)
add_buttton.grid(row=4, column=1, columnspan=2)

generate_button = Button(text="Generate Password", width=14, highlightthickness=0, command=pass_generator)
generate_button.grid(row=3, column=2)

web_insert = Entry(width=50)
web_insert.grid(row=1, column=1, columnspan=2)
web_insert.focus()

user_mail_insert = Entry(width=50)
user_mail_insert.grid(row=2, column=1, columnspan=2)
user_mail_insert.insert(END, "kamil.branicki17@gmail.com")

pass_insert = Entry(width=31)
pass_insert.grid(row=3, column=1)

















window.mainloop()