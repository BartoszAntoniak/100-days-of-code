from random import randint
from tkinter import *
from tkinter import Canvas
import pandas

BACKGROUND_COLOR = "#B1DDC6"
#_______________________Timer______________________________


#_______________________Data_______________________________
data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict()
key_count=0
for each_key in to_learn["French"]:
    key_count+=1

def next_card():
    canvas.itemconfig(title_label,text="French")
    canvas.itemconfig(word_label, text=to_learn["French"][randint(0,key_count-1)])

#________________________UI________________________________
#Background
window = Tk()
window.title("Flash Card App")
window.config(background=BACKGROUND_COLOR,padx=50,pady=50)


canvas = Canvas(width=800, height=526)
card_front_png = PhotoImage(file="./images/card_front.png")
canvas.create_image(400,263,image=card_front_png)
title_label = canvas.create_text(400, 150,text="Title",font=("Arial",40,"italic"))
word_label = canvas.create_text(400, 263,text="Word",font=("Arial",60,"bold"))
canvas.create_text(400,150)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)

#Buttons
ok_button_image = PhotoImage(file="./images/right.png")
ok_button = Button(image=ok_button_image, command=next_card, highlightthickness=0)
ok_button.grid(row=1, column=1)

nok_button_image = PhotoImage(file="./images/wrong.png")
nok_button = Button(image=nok_button_image, command = next_card, highlightthickness=0)
nok_button.grid(row=1, column=0)


window.mainloop()