import prompt
from random import randint
from .game import run_app

game_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def isEven(number):
    return number % 2 == 0


def flow():
    number = randint(0, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')

    correct_answer = 'yes' if isEven(int(number)) else 'no'
    return [answer, correct_answer]


def run_game(name):
    run_app(game_description, flow, name)
