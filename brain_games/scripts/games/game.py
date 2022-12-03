def runGame(greetings, game, name):
    print(greetings)
    attempts = 3

    while attempts > 0:
        game(name)
    
    if attempts == 0:
        print(f'Congratulations, {name}!')