def run_app(greetings, flow, name):
    print(greetings)
    attempts = 3

    while attempts > 0:
        answer, correct_answer = flow()
        m = f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.'
        if answer == correct_answer:
            print('Correct!')
            attempts -= 1
        else:
            print(m)
            print(f'Let\'s try again, {name}!')
            break

    if attempts == 0:
        print(f'Congratulations, {name}!')
