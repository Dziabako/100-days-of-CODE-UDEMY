from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_TITLE = ("Ariel", 40, "italic")
CARD_WORD = ("Ariel", 60, "bold")
current_card = {}

# czytamy z tego pliku bo tych slowek nie znamy / jak nie ma tego pliku to wyskoczy blad
try:
    word = pandas.read_csv("./Data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./Data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # W ten sposob tworzymy liste slownikow z pliku csv
    to_learn = word.to_dict(orient="records")


# ---------------------------- CARDS FUNCTIONS ------------------------------- #
def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")
    canvas.itemconfig(canvas_image, image=card_image_back)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    random_index = to_learn.index(random.choice(to_learn))
    current_card = to_learn[random_index]

    # W ten sposob uzyskamy wartosc z slownika w liscie / Najpierw jest index z listy a potem klucz slownika
    french_word = current_card["French"]
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(canvas_image, image=card_image_front)

    flip_timer = window.after(3000, flip_card)


def is_known():
    # W ten sposob dodajemy slowka ktorych nie znamy do onnego pliku
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    # index=False sprawi ze w tworzonym pliku pandas nie bedzie za kazdym razem na poczatku tworzylo indexu
    data.to_csv("./Data/words_to_learn.csv", index=False)

    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
card_image_front = PhotoImage(file="./Images/card_front.png")
card_image_back = PhotoImage(file="./Images/card_back.png")
wrong_image = PhotoImage(file="./Images/wrong.png")
right_image = PhotoImage(file="./Images/right.png")


# Card Image
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(410, 263, image=card_image_front)

title_text = canvas.create_text(400, 150, text="Title", font=CARD_TITLE)
word_text = canvas.create_text(400, 263, text="Word", font=CARD_WORD)

canvas.grid(column=0, row=0, columnspan=2)


# Buttons
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

# W ten sposob usuniemy buga przez ktory jak bedziemy duzo klikac to nie bedzie resetowac czasu
flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
