from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip

# FONT = ("Courier", 7, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for sym in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)

    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_input.get()
    username_text = username_input.get()
    password_text = password_input.get()

    if len(website_text) == 0 or len(password_text) == 0:
        # messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
        # OR
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_text,
                                       message=f"These are the details entered: \nEmail: {username_text}"
                                               f"\nPassword: {password_text} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_text} | {username_text} | {password_text}\n")

            website_input.delete(0, END)
            password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
website.grid(column=0, row=1)
username = Label(text="Email/Username:")
username.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# Entries
website_input = Entry(width=50)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
username_input = Entry(width=50)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "ezershazam@gmail.com")
password_input = Entry(width=32)
password_input.grid(column=1, row=3)

gen_password = Button(text="Generate Password", width=14, command=generate_password)
gen_password.grid(column=2, row=3)

add = Button(text="Add", width=42, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
