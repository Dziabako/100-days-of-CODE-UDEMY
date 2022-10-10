from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    # W ten sposob przekazujemy zmienna i podajemy jej typ jako obiekt klasy quiz brain
    # Nie musimy wtedy podawac danych wejsciowych
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, highlightthickness=0, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        # Dzieki width w text tekst bedzie sie automatycznie dopasowywal do obszaru
        self.q_text = self.canvas.create_text(150, 125,
                                              width=280,
                                              text="Test",
                                              font=("Arial", 20, "italic"),
                                              fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        correct_image = PhotoImage(file="./Images/true.png")
        self.correct_button = Button(image=correct_image, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)

        false_image = PhotoImage(file="./Images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        # W ten sposob przy kazdym nowym pytaniu i na koncu ekran bedzie bialy
        self.canvas.configure(bg="white")
        # W ten sposob sprawdzamy czy mamy dalej dostepne pytania
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            # Score aktualizuje sie juz w quiz brain i nie jest potrzebne tutaj to robic
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the quiz")
            # Wylaczanie przyciskow
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

# Powiadomienie gracza czy odpowiedzial dobrze czy zle
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

# Po tym czasie zmieni sie pytanie a kolor ekranu zmieni sie spowrotem na bialy
        self.window.after(1000, self.get_next_question)
