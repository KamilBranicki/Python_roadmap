BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
COUNT = 5
choice = 1
new_data_list = []
TIMER = None

# ---------------------------- WORD SLECTION--------------------------- #
try:
    data = pandas.read_csv("C:\Python\Projects\Day31\data\\word_to_learn.csv")
except:
    data = pandas.read_csv("C:\Python\Projects\Day31\data\\french_words.csv")
data_list = data.to_dict(orient="records")
word = random.choice(data_list)
word_f = word["French"]
word_e = word["English"]

def next_card():
    global COUNT, word_e, word_f, word
    word = random.choice(data_list)
    word_f = word["French"]
    word_e = word["English"]
    canvas.itemconfig(canvas_image, image = card_f_img)
    canvas.itemconfig(word_text, text=word_f, fill="#000000")
    canvas.itemconfig(lng_text, text="French", fill="#000000")
    canvas.itemconfig(timer_txt, text=COUNT, fill="#000000")
    canvas.itemconfig(points_text, text=f"Words to learn: {len(data_list)-1}", fill="#000000")
    COUNT = 5
    window.after_cancel(TIMER)
    count_down(COUNT)

def word_selection_ok():
    global word, COUNT, word_e, word_f
    data_list.remove(word)
    data = pandas.DataFrame(data_list)
    data.to_csv("C:\Python\Projects\Day31\data\\word_to_learn.csv", index=False)
    word = random.choice(data_list)
    word_f = word["French"]
    word_e = word["English"]
    canvas.itemconfig(canvas_image, image = card_f_img)
    canvas.itemconfig(word_text, text=word_f, fill="#000000")
    canvas.itemconfig(lng_text, text="French", fill="#000000")
    canvas.itemconfig(timer_txt, text=COUNT, fill="#000000")
    canvas.itemconfig(points_text, text=f"Words to learn: {len(data_list)-1}", fill="#000000")
    COUNT = 5
    window.after_cancel(TIMER)
    count_down(COUNT)

# ---------------------------- CARD FLIP ------------------------------- #
def count_down(COUNT):
    global TIMER
    if COUNT > 0:
        TIMER = window.after(1000, count_down, COUNT - 1)
        canvas.itemconfig(timer_txt, text=COUNT)
    else:
        canvas.itemconfig(canvas_image, image = card_b_img)
        canvas.itemconfig(word_text, text=word_e, fill="#ffffff")
        canvas.itemconfig(lng_text, text="English", fill="#ffffff")
        canvas.itemconfig(timer_txt, text="", fill="#ffffff")
        canvas.itemconfig(points_text, text=f"Words to learn: {len(data_list)-1}", fill="#ffffff")
        COUNT = 5
        window.after_cancel(TIMER)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR,highlightthickness=0)
card_f_img = PhotoImage(file="C:\Python\Projects\Day31\images\card_front.png")
card_b_img = PhotoImage(file="C:\Python\Projects\Day31\images\card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_f_img)
lng_text = canvas.create_text(400, 150, text="French", font=('Ariel', 40, "italic"))
word_text = canvas.create_text(400, 263, text=word_f, font=('Ariel', 60, "bold"))
timer_txt = canvas.create_text(700, 60, text=COUNT, font=('Ariel', 60, "bold"))
points_text = canvas.create_text(150, 450, text=f"Words to learn: {len(data_list)-1}", font=('Ariel', 20, "bold")) 
canvas.grid(row=0, column=0, columnspan=2)

x_button_png = PhotoImage(file="C:\Python\Projects\Day31\images\wrong.png")
x_button = Button(image=x_button_png, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

v_button_png = PhotoImage(file="C:\\Python\\Projects\\Day31\\images\\right.png")
v_button = Button(image=v_button_png, highlightthickness=1, command=word_selection_ok)
v_button.grid(row=1, column=1)

count_down(COUNT)

window.mainloop()