from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    username = entry_email_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please complete all fields and try again.")
    else:
        user_confirm = messagebox.askokcancel(title=website, message=f"Confirm information:\nUsername: {username}\nPassword: {password}")

        if user_confirm == True:
            # write website, username, and password fields to text file
            with open('./data.txt', "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
            
            fields_to_clear = [entry_website, entry_password]
            for field in fields_to_clear:
                field.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
FONT = 'Helvetica'
FONT_SIZE = 14
ENTRY_WIDTH = 35
BUTTON_WIDTH = 33

window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:", font=(FONT, FONT_SIZE))
label_website.grid(column=0, row=1)

label_email_username = Label(text="Email/Username:", font=(FONT, FONT_SIZE))
label_email_username.grid(column=0, row=2)

label_password = Label(text="Password:", font=(FONT, FONT_SIZE))
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=ENTRY_WIDTH)
entry_website.grid(column=1, row=1, columnspan=2, sticky=W)
entry_website.focus()

entry_email_username = Entry(width=ENTRY_WIDTH)
entry_email_username.grid(column=1, row=2, columnspan=2, sticky=W)
entry_email_username.insert(0, 'andrewvanderleest@gmail.com')

entry_password = Entry(width=ENTRY_WIDTH)
entry_password.grid(column=1, row=3, columnspan=2, sticky=W)

# Buttons
button_generate_password = Button(text="Generate Password", width=BUTTON_WIDTH, command=generate_password)
button_generate_password.grid(column=1, row=4, columnspan=2)

button_add_password = Button(text="Add", width=BUTTON_WIDTH, command=save)
button_add_password.grid(column=1, row=5, columnspan=2)

window.mainloop()