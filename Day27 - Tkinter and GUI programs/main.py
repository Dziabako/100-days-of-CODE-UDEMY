# importowanie wszystkich metod z modulu / troche moze mylic bo nie wiadomo dokladnie skad to jest jak jest duzo
from tkinter import *


def button_clicked():
    value = inp.get()
    my_label.config(text=value)


# Tworzenie nowego okna / z tego obiektu mozemy wywolac metody do stworzenia okna
window = Tk()

# Metody edytujace okno
window.title("First GUI program!")
window.minsize(width=500, height=300)

# Komponenty do umieszczenia w oknie
# Label i metody / .pack() to metoda do umieszczania komponentow w oknie (jest dodatkowa dokumentacja do tego)
# Malo precyzyjny i pozycje mozna tylko zmienic jako side="left""bottom""right"
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# Zmiana wartosci w Label
my_label["text"] = "New Text"
my_label.config(text="New New Text")


# Przyciski
# .place() - dziala tak samo jak pack ale mozna podac dokladna pozycje gdzie ma byc widget
# Trzeba jednak wykombinowac gdzie dokladnie on ma byc
btn = Button(text="Click Me!", command=button_clicked)
btn.place(x=220, y=150)


# Entry
# .grid() - dzieli okno na rzedy i kolumny i podajac kolumne i rzad okreslamy pozycje widgeta
# Bardziej wygodne niz .place() / najlatwiej to zaczac od pierwszego widgetu i kolejna dostawiac nastepne
# grid() oraz pack() nie moga byc w tym samym programie poniewaz sa niekompatybilne
inp = Entry(width=10)
inp.grid(column=0, row=0)
# Zapisywanie podanej wartosci
val = inp.get()


# Podobne jak screen.exitonclic() / utrzymuje otwarte okno / ustawiany na koncu
window.mainloop()
