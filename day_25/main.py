import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title = "U.S. States Game"

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")


def get_coordinates(state):
    state_data = data[data.state == state]
    x = float(state_data.x)
    y = float(state_data.y)
    return (x, y)


def get_unanswered_states():
    states = []
    for state in states_list:
        if state not in guessed_states:
            states.append(state)

    data = pandas.DataFrame(states)
    data.to_csv("unanswered_states.csv")


guessed_states = []
states_list = data.state.to_list()
while len(guessed_states) < 50:
    user_answer = screen.textinput(
        f"{len(guessed_states)}/50 Guess the state", "What's another state name?")
    user_answer = user_answer.strip()
    user_answer = user_answer.title()

    if user_answer == "Exit":
        unanswered_states = get_unanswered_states()
        break

    if user_answer in states_list:
        guessed_states.append(user_answer)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(get_coordinates(user_answer))
        state.write(user_answer, align='center', font=('Courier', 12))


screen.exitonclick()
