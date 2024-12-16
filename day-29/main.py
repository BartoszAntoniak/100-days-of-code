from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = user_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password":password
        }
    }

    if email == "" or password == "" or website == "":
        messagebox.showinfo(title="Wrong input",message="Please input data in all 3 rows")

    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        except JSONDecodeError:
            data={}

        data.update(new_data)
        with open("data.json","w") as data_file:
            json.dump(data,data_file,indent=4)

        website_input.delete(0, 'end')
        user_input.delete(0,"end")
        password_input.delete(0,"end")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_input.delete(0, "end")

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(0,nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(0,nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(0,nr_symbols)]

    password_list = password_letters+password_numbers+password_symbols
    random.shuffle(password_list)
    password="".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=f"{website} data", message=f"Your {website} email is: {data[website]["email"]}\nYour {website} password is: {data[website]["password"]}")
    except KeyError:
            messagebox.showinfo(title="Error",message="This website doesn't appear in registry, try again")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=10)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w")

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0, sticky="w")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w")

# Input fields
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="w")
website_input.focus()

user_input = Entry(width=35)
user_input.grid(row=2, column=1, columnspan=2, sticky="w")
user_input.insert(0, "dummy@gmail.com")

password_input = Entry(width=35)
password_input.grid(row=3, column=1, sticky="w")

# Buttons
generate_password_button = Button(text="Generate Password", command=password_generator, padx=0, pady=0,width=15)
generate_password_button.grid(row=3, column=2, sticky="w", padx=5)

add_button = Button(text="Add", command=save, width=15)
add_button.grid(row=4, column=1)

search_button = Button(text="Search", command = search, width=15)
search_button.grid(row=1, column=2)

window.mainloop()
