import random
from tkinter import *
from tkinter import Canvas
import pandas


BACKGROUND_COLOR = "#B1DDC6"
#_______________________Data_______________________________
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}
flip_timer = None

def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_label, text="French")
    canvas.itemconfig(word_label, text=current_card["French"])
    canvas.itemconfig(canvas_image, image=card_front_png)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_label,text="English")
    canvas.itemconfig(word_label,text=current_card["English"])
    canvas.itemconfig(canvas_image, image=card_back_png)


def user_knew_card():
    if current_card == {}:
        next_card()
    else:
        to_learn.remove(current_card)
        data = pandas.DataFrame(to_learn)
        data.to_csv("./data/words_to_learn.csv",index=False)
        next_card()
#________________________UI________________________________
#Background
window = Tk()
window.title("Flash Card App")
window.config(background=BACKGROUND_COLOR,padx=50,pady=50)

canvas = Canvas(width=800, height=526)
card_front_png = PhotoImage(file="./images/card_front.png")
card_back_png = PhotoImage(file="./images/card_back.png")
# canvas.create_image(400,263,image=card_front_png)
canvas_image = canvas.create_image(400, 263, image=card_front_png)
title_label = canvas.create_text(400, 150,text="Title",font=("Arial",40,"italic"))
word_label = canvas.create_text(400, 263,text="Word",font=("Arial",60,"bold"))
canvas.create_text(400,150)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)

#Buttons
ok_button_image = PhotoImage(file="./images/right.png")
ok_button = Button(image=ok_button_image, command=user_knew_card, highlightthickness=0)
ok_button.grid(row=1, column=1)

nok_button_image = PhotoImage(file="./images/wrong.png")
nok_button = Button(image=nok_button_image, command = next_card, highlightthickness=0)
nok_button.grid(row=1, column=0)


window.mainloop()