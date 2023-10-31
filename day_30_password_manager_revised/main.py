'''Single user password manager. Create, store, and search username/password data.'''
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    '''First checks to see if password already exists for website.
    Lets user know if password already exists, asks if user wants to replace.
    If no data for site yet, or if user says yes to replace, generates new password and fills password field.'''
    generate = True

    # check for existing site data
    try:
        with open('./data.json', "r") as data_file:
            data = json.load(data_file)
            website = entry_website.get()
            if website.lower() in list(data.keys()):
                generate = messagebox.askyesno(title="Exisitng Website", message=f"Username/password for {website.title()} already exists."
                                               "\nWould you like to replace it?")
    except FileNotFoundError:
        pass

    # generate new password if none exists for site or if user wants to replace
    if generate == True:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
                   'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
                   'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    '''Writes site name, email/username, and password to json data file.
    Creates new data file first if one does not exist.'''

    # collect field data
    website = entry_website.get()
    username = entry_email_username.get()
    password = entry_password.get()
    new_data = {
        website.lower(): {
        "email": username,
        "password": password
        }
    }

    # warn user if necessary fields are empty
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please complete all fields and try again.")
    # write field data to json file, delete fields afterwards
    else:
        try:
            with open('./data.json', "r") as data_file:
                # read old data
                data = json.load(data_file)
                # update old with new data
                data.update(new_data)
        except FileNotFoundError:
            with open('./data.json', "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('./data.json', "w") as data_file:
                # save updated data
                json.dump(data, data_file, indent=4)
        finally:
            messagebox.showinfo(title="Save Confirmation", message=f"{website.title()} info saved successfully."
                                "\nPassword has been copied to clipboard.")
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    '''Searches existing json data file for website in field.
    If match, copies password to the clipboard'''
    website = entry_website.get()

    # warn user if website field empty
    if len(website) == 0:
        messagebox.showwarning(title="Error", message="Please enter a website name to search and try again.")
    else:
        try:
            with open('./data.json', "r") as data_file:
                data = json.load(data_file)
                website_match = data[website.lower()]
                pyperclip.copy(website_match['password'])
                messagebox.showinfo(title=f"{website.title()}", message=f"Username: {website_match['email']}"
                                    f"\nPassword: {website_match['password']}\n\nPassword copied to clipboard.")
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No data file found. Please create one or more passwords and try again.")
        except KeyError:
            messagebox.showwarning(title="Error", message=f"No username/password found for {website.title()}.")
        

# ---------------------------- UI SETUP ------------------------------- #
FONT = 'Helvetica'
FONT_SIZE = 14
ENTRY_WIDTH = 35
BUTTON_WIDTH = 33
DEFAULT_USERNAME = 'user@domain.com'

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
entry_email_username.insert(0, DEFAULT_USERNAME)

entry_password = Entry(width=ENTRY_WIDTH)
entry_password.grid(column=1, row=3, columnspan=2, sticky=W)

# Buttons
button_generate_password = Button(text="Generate Password", width=BUTTON_WIDTH, command=generate_password)
button_generate_password.grid(column=1, row=5, columnspan=2)

button_add_password = Button(text="Add", width=BUTTON_WIDTH, command=save)
button_add_password.grid(column=1, row=6, columnspan=2)

button_search = Button(text="Search", width=BUTTON_WIDTH, command=search)
button_search.grid(column=1, row=4, columnspan=2)

window.mainloop()