#!/usr/bin/env python3

from ..cli import welcome_user
from .games.even import run_game


def main():
    print("Welcome to the Brain Games!?")
    user_name = welcome_user()

    run_game(user_name)

if __name__ == '__main__':
    main()