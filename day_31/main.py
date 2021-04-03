from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    csv_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    csv_data = pandas.read_csv("data/french_words.csv")

cards_to_learn = pandas.DataFrame.to_dict(csv_data, orient="records")
current_card = {}
flip_timer = None


def reveal_answer():
    canvas.itemconfig(card_bg, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def next_card():
    global current_card, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    current_card = random.choice(cards_to_learn)
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, reveal_answer)


def known_card():
    cards_to_learn.remove(current_card)
    data = pandas.DataFrame(cards_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800,
                height=526,
                bg=BACKGROUND_COLOR,
                highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(
    400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_bnt_img = PhotoImage(file=r"./images/right.png")
right_btn = Button(image=right_bnt_img,
                   highlightthickness=0, command=known_card)
right_btn.grid(row=1, column=0)

wrong_btn_img = PhotoImage(file=r"./images/wrong.png")
wrong_btn = Button(image=wrong_btn_img,
                   highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=1)

next_card()

window.mainloop()
