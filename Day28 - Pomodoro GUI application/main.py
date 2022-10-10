from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
# hex kody na kolory mozliwe do uzycia do zmiany koloru tla
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # stopowanie wczesniej ustawionego timera / jako dane wejsciowa podajemy zmienna z przypisana funkcja
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Moje
    # if reps == 1 or reps == 3 or reps == 5 or reps == 7:
    #     countdown(work_sec)
    # elif reps == 2 or reps == 4 or reps == 6:
    #     countdown(short_break_sec)
    # elif reps == 8:
    #     countdown(long_break_sec)

    # Z kursu
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    # zamiana sekund na minuty i sekundy / floor() daje nam tylko pelne liczby bez przecinka i nie zaokrogla
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # w ten sposob jak bedzie 0 pojawi sie 00
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # konfigurowanie canvas / uzywamy tutaj wczesniej przypisanej zmiennej
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # after() bierze czas (w milisekundach) i funkcje ktora wykona po okreslonym czasie, oraz argument wejsciowy
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        # bez tego kod sie nie wykona i sie nie zresetuje
        start_timer()
        # moje dodawanie check mark
        if reps % 2 == 0:
            check_label.config(text=f""+CHECK_MARK)

        # Dodawanie check mark z kursu / idea tego kodu jest taka ze marks resetuje sie przy kazdym wywolaniu
        # przez to ze jak sie zwieksza reps marks sie zmienia
        # marks = ""
        # work_sessions = math.floor(reps / 2)
        # for _ in range(work_sessions):
        #     marks += CHECK_MARK
        # check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# powiekszenie wielkosci okna okreslonego ponizej
window.config(padx=100, pady=50, bg=YELLOW)


# widget do operacji na obrazach
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
# w image jest jaki ma byc rodzaj pliku wiec musimy do tego uzyc innej klasy by to okreslic / dpdatkowo polozenie x i y
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
# dzieki przypisaniu tego do zmiennej mamy do tego dostep w funkcjach
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


# tkinter jest event driven wiec przez to czeka na to az cos sie wydarzy i aktualizuje sie
# oznacza to ze inne funkcje poza nie wykonaja sie a program nawet nie zastartuje
window.mainloop()
