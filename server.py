from flask import Flask
from random import randint

app = Flask(__name__)

right_number = randint(0, 9)


def correct_answer():
    return "<h1 style='color:green'>You found me!</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


def too_low():
    return "<h1 style='color:red'>Too low, try again</h1><img src ='https://media.giphy.com/media/jD4DwBtqPXRXa/" \
           "giphy.gif'>"


def too_high():
    return "<h1 style='color:purple'>Too high, try again</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHc" \
           "OjmErm/giphy.gif'>"


def h1(function):
    def wrap():
        return f"<h1>{function()}</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    return wrap


@app.route('/')
@h1
def home():
    return "Guess a number between 0 and 9"


@app.route('/<number>')
def guess(number):
    number = int(number)
    if number == right_number:
        return correct_answer()
    elif number > right_number:
        return too_high()
    elif number < right_number:
        return too_low()


app.run(debug=True)
