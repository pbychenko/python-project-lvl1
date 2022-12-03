#!/usr/bin/env python3

from ..cli import welcome_user
from .games.brain_even import runGame


def main():
    print("Welcome to the Brain Games!?")
    user_name = welcome_user()

    runGame(user_name)

if __name__ == '__main__':
    main()