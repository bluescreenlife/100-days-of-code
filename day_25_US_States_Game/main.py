import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

class StatesGame:
    def __init__(self):
        self.states_df = pandas.read_csv('50_states.csv')
        self.states_list = self.states_df.to_dict('records')
        self.score = 0

        self.labeler = turtle.Turtle()
        self.labeler.hideturtle()
        self.labeler.penup()
        self.labeler.speed('fastest')

        self.game_on = True

    def get_state_data(self):
        state_entry = screen.textinput(title=f"Guess The State! Score: {self.score}", prompt= "Enter a state's name:").title()

        if state_entry == "exit":
            self.game_on = False
            return None
        
        for state_dict in self.states_list:
            if state_dict['state'] == state_entry:
                coordinates = (state_dict['x'], state_dict['y'])
                self.states_list.remove(state_dict)
                return state_entry, coordinates

    def label_state(self, state, coords):
        self.labeler.goto(coords)
        self.labeler.write(state)
        self.score += 1

    def run_game(self):
        while self.game_on == True:
            while len(self.states_list) > 0:
                state_to_write, coords_to_write = self.get_state_data()
                self.label_state(state_to_write, coords_to_write)

    def end_report(self):
        remaining_states = pandas.DataFrame.from_dict(self.states_list)
        remaining_states.to_csv('./states_to_study.csv')

game = StatesGame()
game.run_game()
game.end_report()

screen.exitonclick()