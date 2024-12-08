from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 15
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    marks=0
    checkmark_label.config(text=marks)
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)

timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1, column=1)

#labels
timer_label = Label(text="Timer",font=(FONT_NAME,24,"bold"),bg=YELLOW,fg=GREEN)
timer_label.grid(row=0,column=1)

checkmark_label = Label(text="",font=(FONT_NAME,12,"normal"),bg=YELLOW,fg=GREEN)
checkmark_label.grid(row=4,column=1)

#buttons
start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=2,row=2)

window.mainloop()