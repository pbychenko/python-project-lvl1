import prompt
from random import randint
from math import sqrt

def isPrime(number):
    if number == 1:
        return True
    
    limit = sqrt(number)
    i = 2

    while i <= limit:
        if number % i == 0:
            return False
        
        i += 1

    return True

def run_game(name):
    print('Answer "yes" if the number is prime, otherwise answer "no".')
    attempts = 3

    while attempts > 0:        
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if isPrime(int(number)) else 'no'

        if answer == correct_answer:
            print('Correct!')
            attempts -= 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f'Let\'s try again, {name}!')
            break
    
    if attempts == 0:
        print(f'Congratulations, {name}!')
    