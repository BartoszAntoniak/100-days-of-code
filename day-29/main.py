from tkinter import *
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

password_input = Entry(width=35)
password_input.grid(row=3, column=1, sticky="w")

# Buttons
generate_password_button = Button(text="Generate Password", command="test", padx=0, pady=0,width=15)
generate_password_button.grid(row=3, column=2, sticky="w", padx=5)

add_button = Button(text="Add", command="test", width=15)
add_button.grid(row=4, column=1)

window.mainloop()
