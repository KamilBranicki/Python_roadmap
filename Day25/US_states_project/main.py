import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:\\Python\\Projects\\Day25\\US_states_project\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:\\Python\\Projects\\Day25\\US_states_project\\50_states.csv")
all_states = data.state.to_list()

state_text = turtle.Turtle(visible=False)
state_text.penup()

score = 0
answer_state_list = []
while score < 50:
    answer_state = turtle.textinput(title = f"{score}/50 States Correct", prompt = "What's another state name?").title()

    if answer_state in all_states and answer_state not in answer_state_list:
        score += 1
        state_text.goto(int(data.x[data.state == answer_state]),int(data.y[data.state == answer_state]))
        state_text.write(arg = answer_state, align="left", font=('Arial', 8, 'bold'))
        answer_state_list.append(answer_state)

    if answer_state == "Exit":
        break

# states_to_learn = []
# for state in all_states:
#     if state not in answer_state_list:
#         states_to_learn.append(state)

states_to_learn = [state for state in all_states if state not in answer_state_list]

states_to_learn = pandas.DataFrame(states_to_learn)
states_to_learn.to_csv("C:\\Python\\Projects\\Day25\\US_states_project\\states_to_learn.csv")
