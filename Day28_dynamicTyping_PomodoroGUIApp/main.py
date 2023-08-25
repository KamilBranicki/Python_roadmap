from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
start_clicked = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global start_clicked
    global reps
    reps = 0
    start_clicked = 0
    window.after_cancel(timer)
    timer_label.config(text=" Timer \n", fg="#000000")
    canvas.itemconfig(time_text, text="00:00")
    check_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button_click_count():
    global start_clicked
    start_clicked += 1
    start()

def start():
    if start_clicked == 1:
        global reps
        reps +=1
        work_sec = WORK_MIN # * 60
        short_break_sec = SHORT_BREAK_MIN #* 60
        long_break_sec = LONG_BREAK_MIN #* 60
        if reps % 8 == 0:
            timer_label.config(text="Long\n Break ", fg=RED)
            count_down(long_break_sec)
        elif reps % 2 == 0:
            timer_label.config(text="Short\n Break ", fg=PINK)
            count_down(short_break_sec)
        else:
            timer_label.config(text="Work\nSession", fg=GREEN)       
            count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=70, pady=40, bg=YELLOW)

timer_label=Label(text=" Timer \n", fg="#000000", bg=YELLOW, font=(FONT_NAME, 54, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="C:\\Python\\Projects\\Day28\\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg=GREEN, fg="#FFFFFF", font=(8), highlightthickness=0, command=start_button_click_count)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=RED, fg="#FFFFFF", font=(8), highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
check_mark.grid(row=3, column=1)

window.mainloop()