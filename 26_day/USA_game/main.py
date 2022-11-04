from operator import pos
import turtle
import pandas as pd

# define text parameters
FONT = ("Courier", 10, "normal")
ALIGN = 'center'

# setup screen
screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(750,550)
image = '26_day/USA_game/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

#read and prepare list of states
states_list = pd.DataFrame(pd.read_csv('26_day/USA_game/50_states.csv'))
set_states = set(states_list['state'])

# create object for names writting on the map
text = turtle.Turtle()
text.hideturtle()
text.penup()

states_guessed = set() # set of the guessed states
states_to_learn = set() # set of states to be learned

# loop to shop pop up window and write states names on the map
while len(states_guessed) < len(states_list['state']):
    answer_state = screen.textinput(title = f'{len(states_guessed)}/50 guessed states', prompt = 'Enter name of the state:')
    answer_state = str(answer_state).title()    

    if answer_state in set_states and answer_state not in states_guessed:
        position = states_list[states_list['state'] == answer_state][['x', 'y']]
        text.goto(int(position['x']), int(position['y']))
        text.write(answer_state.title(),align = ALIGN, font = FONT)
        states_guessed.add(answer_state)            
    if answer_state.title() == 'Exit': # command to exit program
        states_to_learn = [state for state in set_states if state not in states_guessed]

        break

# write states to learn to csv
with open('26_day/USA_game/states_to_learn.csv', mode = 'w') as states_list:
    for i in states_to_learn:
        states_list.write(i+'\n')

print('states to learn ', states_to_learn)











