import prompt
from random import randint
from ..utils import MIN, MAX
from ..engine.game import run_app

game_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def flow():
    number = randint(MIN, MAX)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')

    correct_answer = 'yes' if is_even(int(number)) else 'no'
    return [answer, correct_answer]


def run_game(name):
    run_app(game_description, flow, name)
