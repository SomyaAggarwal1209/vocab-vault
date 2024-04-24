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


# Buttons
cross_image = PhotoImage(file="images/cross_button.png")
smaller_cross_image = cross_image.subsample(3, 3)
unknown_button = Button(window, image=smaller_cross_image, highlightthickness=0, borderwidth=0, relief="flat")
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/check_button.png")
smaller_right_button = check_image.subsample(3, 3)
known_button = Button(window, image=smaller_right_button, highlightthickness=0, borderwidth=0, relief="flat")
known_button.grid(row=1, column=1)

window.mainloop()


