import turtle
from player import Player
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data['state'].to_list()

game_is_on = True
answer_count = 0
past_answers = []
missing_answers = []

while game_is_on:

    answer_state = screen.textinput(title=f"{answer_count}/50 States Correct", prompt="Name another state").title()
    if answer_state == "Exit":
        for state in states_list:
            if state not in past_answers:
                missing_answers.append(state)
        states_df = pandas.DataFrame(missing_answers, columns=["missed states"])
        states_df.to_csv('Missed Answers')
        break

    if answer_state not in past_answers:
        past_answers.append(answer_state)
        state_info = data[data["state"] == f"{answer_state.title()}"]
        state_info_x = state_info["x"].iloc[0]
        state_info_y = state_info["y"].iloc[0]
        Player(xcor=state_info_x, ycor=state_info_y, state=answer_state)
        answer_count += 1
    if answer_count == 50:
        Player.game_over()
        game_is_on = False
turtle.mainloop()
