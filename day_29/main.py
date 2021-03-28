from tkinter import *
from tkinter import messagebox
import string
import random

all_char_list = string.ascii_lowercase
all_char_list += string.ascii_uppercase
all_char_list += string.digits
all_char_list += string.punctuation

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    random.shuffle(all_char_list)
    password = ""
    for _ in range(10):
        password += random.choice(all_char_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website.strip()) == 0 or len(username.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showerror("Oooops", "You have to complete all the fields")
    else:
        is_ok = messagebox.askokcancel(website,
                                       f"username: {username}\npassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", 'a') as file:
                file.write(f"{website} | {username} | {password}\n")

            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky='w')
website_input = Entry()
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, stick="ew")

username_label = Label(text="Email / Username:")
username_label.grid(row=2, column=0, sticky='w')
username_input = Entry()
username_input.grid(row=2, column=1, columnspan=2, stick="ew")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky='w')
password_input = Entry()
password_input.grid(row=3, column=1, stick="ew")

gen_password_btn = Button(text="Generate Password",
                          padx=10, highlightthickness=0, command=generate_password)
gen_password_btn.grid(row=3, column=2, stick="ew")

add_btn = Button(text="ADD", highlightthickness=0, command=add_password)
add_btn.grid(row=4, column=1, columnspan=2, stick="ew")

window.mainloop()
