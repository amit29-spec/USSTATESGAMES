from turtle import Turtle, Screen
import pandas


tim = Turtle()
screen = Screen()
screen.title("GAMES")
image = "blank_states_img.gif"
screen.addshape(image)
tim.shape(image)
data = pandas.read_csv("states.csv")
guessed_state = []
new_data = data["state"].to_list()

while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 correct", prompt="What's the another state? press exit "
                                                                               "if you dont know more states").title()
    if answer == "Exit":
        missing_states = [state for state in new_data if state not in guessed_state]
        right_guessed = pandas.DataFrame(missing_states)
        right_guessed.to_csv("missing_states.csv")
        break

    if answer in new_data:
        guessed_state.append(answer)
        rows = data[data.state == answer]
        row_x = rows["x"]
        row_y = rows["y"]
        timmi = Turtle()
        timmi.hideturtle()
        timmi.penup()
        timmi.goto(x=int(row_x), y=int(row_y))
        timmi.write(answer)

