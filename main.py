from tkinter import *
import pandas as pd
import random
import time
import csv


## FLIP THE CARD ##

def flip():
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(word, text=random_pair['English'], fill="white")
    

## RANDOM FUNCTION ##

def random_word():
    global flip_timer, random_pair
    window.after_cancel(flip_timer)

    canvas.itemconfig(card, image= front_card)
    random_pair = random.choice(dictionary)
    english = random_pair['English']
    french = random_pair['French']
    
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french, fill="black")

    flip_timer = window.after(3000,flip)

def remove():
    dictionary.remove(random_pair)
    data = pd.DataFrame(dictionary)
    data.to_csv("data/words_to_learn.csv",  index=False)
   
    random_word()


def add_word():
        data = pd.DataFrame(dictionary)
        data.to_csv("data/words_to_learn.csv",  index=False)

    
        random_word()

## -----------------UI----------------## 
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

window = Tk()
window.title("Flash Card Game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip)

canvas = Canvas(height= 526, width= 800, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400,280,image = front_card)

title = canvas.create_text(400,150,text="title", font=(FONT,40,"italic"))
word = canvas.create_text(400,263,text="Word", font=(FONT,60,"bold"))
canvas.grid(column=0,row=0, columnspan=2)

right = PhotoImage(file="images/right.png")
yes = Button(image=right,highlightthickness=0,command=remove)
yes.grid(column=0,row=1)

wrong = PhotoImage(file="images/wrong.png")
no = Button(image=wrong,highlightthickness=0,command=add_word)
no.grid(column=1,row=1)

## ----------------------------- ##

try:
    lista_parole= pd.read_csv("data/words_to_learn.csv")
    
except FileNotFoundError:
    lista_parole = pd.read_csv("data/french_words.csv")
    
    
finally:
    dictionary = lista_parole.to_dict('records')
    random_word()

window.mainloop()