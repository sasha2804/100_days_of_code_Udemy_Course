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
image = '25_day/USA_quiz/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

#read and prepare list of states
states_list = pd.DataFrame(pd.read_csv('25_day/USA_quiz/50_states.csv'))
states_list['state'] =  states_list['state'].map(lambda x: x.lower())
print(states_list)

# create object for names writting on the map
text = turtle.Turtle()
text.hideturtle()
text.penup()

states_guessed = set() # set of the guessed states

# loop to shop pop up window and write states names on the map
while len(states_guessed) < len(states_list['state']):
    answer_state = screen.textinput(title = f'{len(states_guessed)}/50 guessed states', prompt = 'Enter name of the state:')\
        .lower()
    if answer_state in set(states_list['state']) and answer_state not in states_guessed:
        position = states_list[states_list['state'] == answer_state][['x', 'y']]
        text.goto(int(position['x']), int(position['y']))
        text.write(answer_state.title(),align = ALIGN, font = FONT)
        states_guessed.add(answer_state)
        print(answer_state)            
    if answer_state.lower() == 'exit': # command to exit program
        game_is_on = False
   










