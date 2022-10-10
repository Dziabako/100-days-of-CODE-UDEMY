# Sposob na uzyskanie koordynatow po kliknieciu znajduje sie w notatkach do tego dnia
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game!")
# turtle moze jako shape uzywac obrazow
image = "blank_states_img.gif"
# w ten sposob dodajemy nowy wyglad do naszego ekranu przez co mozemy go uzyc w turtle
screen.addshape(image)
turtle.shape(image)

answered_states = []
answers = 0
prompt = "What's another state's name?"
# answer_state = screen.textinput(title=f"Guess the State! {answers}/50", prompt=prompt).capitalize()

states = pandas.read_csv("50_states.csv")


def write_state(s, x, y):
    st = turtle.Turtle()
    st.penup()
    st.hideturtle()
    st.goto(x, y)
    st.write(s, True, align="center", font=("Courier", 10, "normal"))


while answered_states != 50:
    answer_state = screen.textinput(title=f"Guess the State! {answers}/50", prompt=prompt).capitalize()
    if answer_state == "Exit":
        break
    if answer_state in states.state.to_list():
        answer = states[states.state == answer_state]
        x_cor = int(answer.x)
        y_cor = int(answer.y)
        write_state(answer_state, x_cor, y_cor)
        answered_states.append(answer_state)
        answers = len(answered_states)

# zapisywanie nie odgadnietych stanow do pliku
# to_learn = []
# for state in states.state.to_list():
#     if state not in answered_states:
#         to_learn.append(state)

# List comprehension
to_learn = [state for state in states.state.to_list() if state not in answered_states]

states_to_learn = {"States": to_learn}
rest_of_states = pandas.DataFrame(states_to_learn)
rest_of_states.to_csv("states_to_learn.csv")

screen.exitonclick()
