from tkinter import *


def mile_to_kilometer():
    # w ten sposob uzyskujemy wartosc z wpisania w box / input z boxa to string wiec trzeba go zamienic na liczbe
    m = entry.get()
    value = round(float(m) * 1.6, 2)
    result_label.config(text=value)


window = Tk()
window.title("Mile to Km Converter")

entry = Entry()
entry.insert(END, "0")
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to:")
equal_label.grid(column=0, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=mile_to_kilometer)
calc_button.grid(column=1, row=3)

window.mainloop()
