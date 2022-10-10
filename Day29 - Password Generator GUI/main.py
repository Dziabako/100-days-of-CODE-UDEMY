from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    password_letters = [random.choice(string.ascii_letters) for _ in range(random.randint(8, 10))]
    password_digits = [random.choice(string.digits) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(string.punctuation) for _ in range(random.randint(2, 4))]

    password = password_symbols + password_digits + password_letters
    random.shuffle(password)
    password = "".join(password)

    # ta linia kodu nie jest zbytnio potrzebna bo po dodaniu do pliku wszystkie pola sie resetuja
    if len(password_entry.get()) == 0:
        password_entry.insert(0, password)
    else:
        password_entry.delete(0, END)

    # modu; ktory pozwala automatycznie skopiowac to co znajduje sie w entry
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password_to_file():

    # jezeli to get bedzie poza funkcja to nie zadziala
    website_get = website_entry.get()
    email_get = email_entry.get()
    password_get = password_entry.get()

    # sprawdzanie czy pola sa puste / jak sa zapelnione to kontynuuje
    if len(website_get) == 0 or len(password_get) == 0:
        messagebox.showwarning(title="Oops", message="Do not leave empty fields!")
    else:
        # popup box ktory zwraca true lub false / przypisane do zmiennej by mozna bylo uzyc
        is_ok = messagebox.askokcancel(title=website_get, message=f"These are the details entered:\n "
                                                                  f"Email: {email_get}\n Password: {password_get}")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_get} | {email_get} | {password_get}\n")
                # w ten sposob po dodaniu pole entry sie usunie
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# columnspan pozwala na umieszczenie widgeta w dwoch kolumnach lub wiecej na raz
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=save_password_to_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
