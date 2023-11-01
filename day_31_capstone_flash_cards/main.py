'''Basic French-English flash card studying app
5 seconds by default to guess card correctly (green check mark)
Correct cards removed from pool, remainder stored in CSV for continued study
on next program launch'''

from tkinter import *
import pandas
from random import choice

# ------------------------------- FUNCTIONALITY ------------------------------- #
# open saved CSV from last run, otherwise open starter CSV
try:
    words_df = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    words_df = pandas.read_csv('./data/french_words.csv')
finally:
    french_words = words_df.to_dict(orient='records') # list of dicts, each dict contains french key and english key

current_card = {}

def next_card():
    '''Displays a new French word, reveals English translation after 3 sec.'''
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = choice(french_words) # random dict from above list

    canvas.itemconfigure(image_card, image=image_cardfront)
    canvas.itemconfigure(card_title, text="French", fill='black')
    canvas.itemconfigure(card_text, text=current_card['French'], fill='black')
    flip_timer = window.after(TIME, func=flip_card)

def flip_card():
    '''Reveals the back of the card with English translation.'''
    canvas.itemconfigure(image_card, image=image_cardback)
    canvas.itemconfigure(card_title, text="English", fill='white')
    canvas.itemconfigure(card_text, text=current_card['English'], fill='white')

def remove_card():
    '''Removes current word from French list, saves remaining words list to new CSV.'''
    french_words.remove(current_card)
    save_data = pandas.DataFrame(french_words)
    save_data.to_csv('./data/words_to_learn.csv', index=False)
    next_card()


# ------------------------------- UI ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
TIME = 5000 # time in milliseconds to respond to flash card

# window setup
window = Tk()
window.title("Flashy")
window.config(padx= 50, pady=50, background=BACKGROUND_COLOR)

# call function to flip to English translation after 3 sec
flip_timer = window.after(TIME, func=flip_card)

# canvas setup
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
image_cardfront = PhotoImage(file='./images/card_front.png')
image_cardback = PhotoImage(file='./images/card_back.png')
image_card = canvas.create_image(400, 263, image=image_cardfront)
card_title = canvas.create_text(400, 150, text="Title", font=FONT_LANGUAGE, fill='black')
card_text = canvas.create_text(400, 263, text="placeholder", font=FONT_WORD, fill='black')
canvas.grid(row=0, column=0, columnspan=2)

# buttons
image_known = PhotoImage(file='./images/right.png')
button_known = Button(image=image_known, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=remove_card)
button_known.grid(row=1, column=0)

image_unknown = PhotoImage(file='./images/wrong.png')
button_unknown = Button(image=image_unknown, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
button_unknown.grid(row=1, column=1)

# start flashcards
next_card()

# keep window running
window.mainloop()