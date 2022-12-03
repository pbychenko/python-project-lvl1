import prompt
from random import randint


def get_progression():
    progression = []
    start = randint(1, 10)
    step = randint(1, 5)
    length = randint(3, 10)

    for i in range(0, length):
        progression.append(start + i * step)

    return progression

def run_game(name):
    print('What number is missing in the progression?')
    attempts = 3

    while attempts > 0: 
        progression = get_progression()
        hide_element_number = randint(0, len(progression) - 1)
        buf = progression[:]
        buf[hide_element_number] = '..'
        # dev = ''
        # t = dev.join(buf)

        print(f'Question: {buf}')
        answer = prompt.string('Your answer: ')

        correct_answer = progression[hide_element_number]

        if int(answer) == correct_answer:
            print('Correct!')
            attempts -= 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f'Let\'s try again, {name}!')
            break
    
    if attempts == 0:
        print(f'Congratulations, {name}!')
    