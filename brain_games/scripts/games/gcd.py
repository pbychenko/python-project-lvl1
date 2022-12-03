import prompt
from random import randint


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def run_game(name):
    print('Find the greatest common divisor of given numbers.')
    attempts = 3

    while attempts > 0:        
        number1 = randint(0, 100)
        number2 = randint(0, 100)
        print(f'Question: {number1} {number2}')
        answer = prompt.string('Your answer: ')

        correct_answer = gcd(number1, number2)

        if int(answer) == correct_answer:
            print('Correct!')
            attempts -= 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f'Let\'s try again, {name}!')
            break
    
    if attempts == 0:
        print(f'Congratulations, {name}!')
    