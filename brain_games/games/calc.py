import prompt
from random import randint
from ..utils import MIN, MAX
from ..engine.game import run_app

game_description = 'What is the result of the expression?'


def calc(number1, op, number2):
    if op == '+':
        return int(number1) + int(number2)
    if op == '-':
        return int(number1) - int(number2)
    if op == '*':
        return int(number1) * int(number2)

    return 1


def flow():
    first_number = randint(MIN, MAX)
    second_number = randint(MIN, MAX)
    operations = ['+', '-', '*']
    operation = operations[randint(0, len(operations) - 1)]

    print(f'Question: {first_number} {operation} {second_number} ')
    answer = prompt.string('Your answer: ')

    correct_answer = calc(first_number, operation, second_number)
    return [int(answer), correct_answer]


def run_game(name):
    run_app(game_description, flow, name)
