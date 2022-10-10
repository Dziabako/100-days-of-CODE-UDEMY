# importowanie wszystkich metod z modulu / troche moze mylic bo nie wiadomo dokladnie skad to jest jak jest duzo
from tkinter import *

# Tworzenie nowego okna / z tego obiektu mozemy wywolac metody do stworzenia okna
window = Tk()

# Metody edytujace okno
window.title("First GUI program!")
window.minsize(width=500, height=300)

# Komponenty do umieszczenia w oknie
# Label i metody / .pack() to metoda do umieszczania komponentow w oknie (jest dodatkowa dokumentacja do tego)
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# Zmiana wartosci w Label
my_label["text"] = "New Text"
my_label.config(text="New New Text")


def button_clicked():
    value = entry.get()
    my_label.config(text=value)


# Przyciski
btn = Button(text="Click Me!", command=button_clicked)
btn.pack()


# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()


# Text
text = Text(height=5, width=30)
# Puts cursor in textbox. / Doslownie umieszcza mygajacy kursor pisania w oknie tekstowym
text.focus()
# Adds some text to begin with.
# END oznacza ze mozemy pisac dalej na koncu tekstu
text.insert(END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# Spinbox


def spinbox_used():
    # Gets the current value in spinbox.
    print(spinbox.get())


# tak samo jak prz przyciskach mozna dodawac komendy
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# Variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
# W ten sposob jak klikniemy na element to zostanie on wyswietlony
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Podobne jak screen.exitonclic() / utrzymuje otwarte okno / ustawiany na koncu
window.mainloop()
