import prompt
from random import randint


def isEven(number):
    return number % 2 == 0

def runGame(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempts = 3

    while attempts > 0:        
        number = randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if isEven(int(number)) else 'no'

        if answer == correct_answer:
            print('Correct!')
            attempts -= 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f'Let\'s try again, {name}!')
            break
    
    if attempts == 0:
        print(f'Congratulations, {name}!')
    