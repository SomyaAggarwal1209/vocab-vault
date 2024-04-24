from tkinter import *

BACKGROUND_COLOR = "#B0C5A4"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=764, height=513)
card_front_img = PhotoImage(file="images/front.png")
canvas.create_image(382, 256, image=card_front_img)
canvas.create_text(387, 150, text="Title", font=("Arial", 30, "italic"))  # Corrected the font name
canvas.create_text(387, 256, text="word", font=("Arial", 50, "bold"))    # Corrected the font name
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
