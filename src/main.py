import sys
from printer import *
from command import Command


def main():
    if len(sys.argv) != 2:
        perror("Usage: make turns=<number>", -1)

    customer = Customer()
    retailer = Retailer()
    wholesaler = Wholesaler()
    company = Company()


    turns = sys.argv[1]
    while True:
        if turns == 0:
            pinfo("Game Finished, Exiting...")
            break

        current = customer
        next = 
        cmd = command()
        print(cmd)
        turns -= 1

def command():
    print(": ", end="")
    cmd = Command(input())
    return cmd

if __name__ == "__main__":
    main()
