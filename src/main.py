import sys
from printer import *
from command import Command
from game import Game


def main():
    if len(sys.argv) != 2:
        perror("Usage: make turns=<number>", -1)

    game = Game(int(sys.argv[1]))
    while not game.finished():
        print(": ", end="")
        x = game.execute(input())
        if x.err() == "Exit":
            break
        if x.is_err():
            print(x.err())

        print(game.current.stats())
    print(game.weekly_stock)


if __name__ == "__main__":
    main()
