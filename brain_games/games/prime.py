import prompt
from random import randint
from math import sqrt
from ..engine.game import run_app

game_desc = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isPrime(number):
    if number < 2:
        return True

    limit = sqrt(number)
    i = 2

    while i <= limit:
        if number % i == 0:
            return False

        i += 1

    return True


def flow():
    number = randint(1, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    correct_answer = 'yes' if isPrime(int(number)) else 'no'

    return [answer, correct_answer]


def run_game(name):
    run_app(game_desc, flow, name)