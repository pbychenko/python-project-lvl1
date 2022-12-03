import prompt
from random import randint
from .game import run_app

game_description = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def flow():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    print(f'Question: {number1} {number2}')
    answer = prompt.string('Your answer: ')

    correct_answer = gcd(number1, number2)

    return [int(answer), correct_answer]


def run_game(name):
    run_app(game_description, flow, name)
