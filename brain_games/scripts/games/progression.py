import prompt
from random import randint
from .game import run_app

game_description = 'What number is missing in the progression?'


def get_progression():
    progression = []
    start = randint(1, 10)
    step = randint(1, 5)
    length = randint(3, 10)

    for i in range(0, length):
        progression.append(str(start + i * step))

    return progression


def flow():
    progression = get_progression()
    hide_element_number = randint(0, len(progression) - 1)
    buf = progression[:]
    buf[hide_element_number] = '..'
    buf_to_str = ' '.join(buf)

    print(f'Question: {buf_to_str}')
    answer = prompt.string('Your answer: ')

    correct_answer = progression[hide_element_number]

    return [answer, correct_answer]


def run_game(name):
    run_app(game_description, flow, name)
