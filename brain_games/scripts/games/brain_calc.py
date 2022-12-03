import prompt
from random import randint


def calc(number1, op, number2):
    if op == '+':
        return int(number1) + int(number2)
    if op == '-':
        return int(number1) - int(number2)
    if op == '*':
        return int(number1) * int(number2)

    return 1

def runGame(name):
    print('What is the result of the expression?')
    attempts = 3

    while attempts > 0:        
        first_number = randint(0, 100)
        second_number = randint(0, 100)
        operations = ['+', '-', '*' ]
        operation = operations[randint(0, 2)]

        print(f'Question: {first_number} {operation} {second_number} ')
        answer = prompt.string('Your answer: ')

        correct_answer = calc(first_number, operation, second_number)

        if int(answer) == correct_answer:
            print('Correct!')
            attempts -= 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f'Let\'s try again, {name}!')
            
            break
    
    if attempts == 0:
        print(f'Congratulations, {name}!')
    