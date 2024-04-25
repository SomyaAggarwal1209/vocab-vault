from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B0C5A4"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



#-----------------------------UI SETUP-------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=764, height=513)
card_front_img = PhotoImage(file="images/front.png")
card_back_img = PhotoImage(file="images/back.png")
card_bg = canvas.create_image(382, 256, image=card_front_img)
card_title = canvas.create_text(387, 150, text="", font=("Arial", 30, "italic"))
card_word = canvas.create_text(387, 256, text="", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Buttons
cross_image = PhotoImage(file="images/cross_button.png")
smaller_cross_image = cross_image.subsample(3, 3)
unknown_button = Button(window, image=smaller_cross_image, highlightthickness=0, borderwidth=0, relief="flat",
                        command=flip_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/check_button.png")
smaller_right_button = check_image.subsample(3, 3)
known_button = Button(window, image=smaller_right_button, highlightthickness=0, borderwidth=0, relief="flat",
                      command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
