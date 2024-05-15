from tkinter import *
import pandas as pd
import random
import time


## FLIP THE CARD ##

def flip(english):
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(word, text=english, fill="white")
    

    



## RANDOM FUNCTION ##

def random_word():
    canvas.itemconfig(card, image=front_card)
    random_pair = random.choice(dictionary)
    english = random_pair['English']
    french = random_pair['French']

    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french, fill="black")

    window.after(3000,flip,english)


## -----------------UI----------------## 
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

window = Tk()
window.title("Flash Card Game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(height= 526, width= 800, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400,280,image = front_card)

title = canvas.create_text(400,150,text="title", font=(FONT,40,"italic"))
word = canvas.create_text(400,263,text="Word", font=(FONT,60,"bold"))
canvas.grid(column=0,row=0, columnspan=2)

right = PhotoImage(file="images/right.png")
yes = Button(image=right,highlightthickness=0,command=random_word)
yes.grid(column=0,row=1)

wrong = PhotoImage(file="images/wrong.png")
no = Button(image=wrong,highlightthickness=0,command=random_word)
no.grid(column=1,row=1)

## ----------------------------- ##

lista_parole= pd.read_csv("data/french_words.csv")
dictionary = lista_parole.to_dict('records')

random_word()



window.mainloop()