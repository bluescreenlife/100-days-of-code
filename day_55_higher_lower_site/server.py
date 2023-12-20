'''Random number guessing Flask site. User enters /number to URL to guess.'''
from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def higher_lower():
    return "<h1>Guess a number between 0 and 9</h1>" \
    "<p>To guess, navigate to the URL of a number by adding \\number to the current url.</p>" \
    "<img src= 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

random_number = randint(0,9)

@app.route("/<int:number>")
def check_number(number):
    if number < random_number:
        return f"<h1 style='color: blue'>Too low!<h1>" \
        "<img src='https://media0.giphy.com/media/3oEjI80DSa1grNPTDq/giphy.gif?cid=ecf05e47amq3n874xs0f9p6vnhhu30bvpkv01qvu0pn3fzf9&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    elif number > random_number:
        return f"<h1 style='color: purple'>Too high!<h1>" \
        "<img src='https://media3.giphy.com/media/3o6Zt8zFqqIwQNQsj6/giphy.gif?cid=ecf05e47n54p5ixe7qiosrq0db9fhkf3epg50r9wmhwmgtsv&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    elif number == random_number:
        return f"<h1 style='color: green'>Correct!<h1>" \
        "<img src='https://media4.giphy.com/media/PS7d4tm1Hq6Sk/giphy.gif?cid=ecf05e47fz4pxo391vy1pq6chj0wlu9kaaxr0n3b4kb8nt1j&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    
if __name__ == "__main__":
    app.run(debug=True)