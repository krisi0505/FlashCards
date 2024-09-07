from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "white"
FRONT_COLOR = "#ff6f69"
BACK_COLOR = "#96ceb4"
BUTTON_COLOR = "#c83349"
card = dict()
lg = "Италиански"


def flip_card():
    # canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.config(bg=BACK_COLOR)
    global card
    canvas.itemconfig(word_label, text=card["Bulgarian"], fill="white")
    canvas.itemconfig(lg_label, text="Български", fill="white")


def new_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    # canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.config(bg=FRONT_COLOR)
    card = random.choice(italian_words)
    canvas.itemconfig(word_label, text=card["Italian"], fill="white")
    canvas.itemconfig(lg_label, text=lg, fill="white")

    flip_timer = window.after(3000, func=flip_card)


def correct_answer():
    italian_words.remove(card)
    unknown_words = pandas.DataFrame(italian_words)
    unknown_words.to_csv("data/words_to_learn.csv", index=False)
    new_card()


def wrong_answer():
    new_card()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

# card_front_img = PhotoImage(file="images/card_front.png")
# card_back_img = PhotoImage(file="images/card_back.png")
# canvas_img = canvas.create_image(400, 263, image=card_front_img)


lg_label = canvas.create_text(400, 150, text=lg, font=("Arial", 40, "italic"))

word_label = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

right_button = Button(text="Знам", command=correct_answer, bg="#008040", width=12, height=2, fg="white", font=("Arial", 12, "bold"))
right_button.grid(column=1, row=1)

wrong_button = Button(text="Не знам", command=wrong_answer, bg=BUTTON_COLOR, width=12, height=2, fg="white", font=("Arial", 12, "bold"))
wrong_button.grid(column=0, row=1)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/italian_words.csv")

italian_words = data.to_dict(orient="records")

new_card()

window.mainloop()