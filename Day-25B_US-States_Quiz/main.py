import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)
turtle.shape(image)

avia = turtle.Turtle()
avia.penup()
avia.hideturtle()

data = pandas.read_csv("50_states.csv")

guessed_state = []

state_data = data["state"].to_list()

while len(guessed_state) < 50:
    x_data = data["x"].to_list()
    y_data = data["y"].to_list()
    y_index = ""
    x_index = ""
    total_state = len(state_data)
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the State",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in state_data if state not in guessed_state]
        dict_missing_state = {
            "Missing_states": missing_state
        }
        missing_data_states = pandas.DataFrame(dict_missing_state)
        # print(missing_data_states)
        missing_data_states.to_csv("missing_states.csv")
        break
    if answer_state in state_data:
        if answer_state in guessed_state:
            pass
        else:
            guessed_state.append(answer_state)
            x_index = state_data.index(answer_state)
            y_index = state_data.index(answer_state)
            x_position = x_data[x_index]
            y_position = y_data[y_index]
            avia.goto(x_position, y_position)
            avia.write(f"{answer_state}", False, "center", ("Courier", 8, "normal"))



# print(missing_state)



# all_states = data.state.to_list()
# guessed_state = []
#
# while len(guessed_state) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the State",
#                                     prompt="What's another state's name?").title()
#
#     if answer_state in all_states:
#         guessed_state.append(answer_state)
#         state_data = data[data.state == answer_state]
#         avia.goto(int(state_data.x), int(state_data.y))
#         avia.write(answer_state)
