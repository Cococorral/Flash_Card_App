from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pandas.read_csv("words_to_learn.csv")
    df_dict = df.to_dict(orient="records")
    CHOICE = [df_dict[randint(0, len(df_dict) - 1)]]
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    df_dict = df.to_dict(orient="records")
    CHOICE = [df_dict[randint(0, len(df_dict) - 1)]]


def combined_commands():
    save_data()
    new_card()


def save_data():
    df_dict.remove(CHOICE[len(CHOICE) - 1])
    dataframe = pandas.DataFrame(df_dict)
    dataframe.to_csv("words_to_learn.csv", index=False)


def new_card():
    CHOICE.append(df_dict[randint(0, len(df_dict) - 1)])
    choice_index_fr = CHOICE[len(CHOICE) - 1]
    french_word = choice_index_fr["French"]
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(default_title, text="French", fill="black")
    canvas.itemconfig(default_word, text=f"{french_word}", fill="black")
    window.after(3000, translated_card)


def translated_card():
    choice_index_eng = CHOICE[len(CHOICE) - 1]
    english_word = choice_index_eng["English"]
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(default_title, text="English", fill="white")
    canvas.itemconfig(default_word, text=f"{english_word}", fill="white")


#UI


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)
default_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
default_word = canvas.create_text(400, 263, text=f"{CHOICE[len(CHOICE) - 1]["French"]}", font=("Ariel", 60, "bold"))

right_button = Button(image=right_img, borderwidth=0, highlightthickness=0, command=combined_commands)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_img, borderwidth=0, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

window.after(3000, translated_card)

window.mainloop()
