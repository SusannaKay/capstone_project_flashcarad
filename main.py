from tkinter import *
import pandas as pd

#constants

## -----------------UI----------------## 
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

window = Tk()
window.title("Flash Card Game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(height= 526, width= 800, bg=BACKGROUND_COLOR, highlightthickness=0)
card = PhotoImage(file="images/card_front.png")
# #back_img= PhotoImage(file="card_back.png")
canvas.create_image(400,280,image = card)
title = canvas.create_text(400,150,text="Title", font=(FONT,40,"italic"))
word = canvas.create_text(400,263,text="Word", font=(FONT,60,"bold"))
canvas.grid(column=0,row=0, columnspan=2)

right = PhotoImage(file="images/right.png")
yes = Button(image=right,highlightthickness=0)
yes.grid(column=0,row=1)

wrong = PhotoImage(file="images/wrong.png")
no = Button(image=wrong,highlightthickness=0)
no.grid(column=1,row=1)

## ------------ CSV ----------------- ##







window.mainloop()