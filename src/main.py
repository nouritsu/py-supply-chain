import sys
from printer import *
from command import Command
from customer import Customer
from retailer import Retailer
from team import Team


def main():
    if len(sys.argv) != 2:
        perror("Usage: make turns=<number>", -1)

    customer = Customer()
    retailer = Retailer()

    customer.set_next(retailer)
    customer.set_prev(None)

    retailer.set_next(None)
    retailer.set_prev(customer)

    turns = int(sys.argv[1])
    while True:
        if turns == 0:
            pinfo("Game Finished, Exiting...")
            break

        print(customer)
        handle_turn(customer)
        print(customer)
        print(retailer)
        handle_turn(retailer)
        print(retailer)

        turns -= 1


def handle_turn(player: Team):
    while True:
        cmd = command()
        if cmd.invalid == True:
            pwarning(f"Invalid Command")
        match cmd.name:
            case "order":
                if cmd.arg == -1:
                    pwarning(f"Invalid argument for {cmd.name} : {cmd.arg}")
                    continue
                # if isinstance(player, Company):
                #     pwarning("Cannot place orders as a company.")
                player.place_order(cmd.arg)
            case "fulfill":
                if cmd.arg == -1:
                    pwarning(f"Invalid argument for {cmd.name} : {cmd.arg}")
                    continue
                if isinstance(player, Customer):
                    pwarning(f"Cannot fulfill order as customer.")
                    continue
                player.fulfill_order(cmd.arg)
            case "produce":
                ...
            case "exit":
                pinfo("Exiting...")
                exit(0)
            case "next":
                return
            case "":
                pwarning(
                    "Cannot execute  command, use 'next' to end turn or use 'exit' to exit program."
                )
            case _:
                pwarning(f"Unknown command.")


def command():
    print(": ", end="")
    try:
        cmd = Command(input())
    except KeyboardInterrupt:
        pinfo("Exiting...")
        exit(0)
    return cmd


if __name__ == "__main__":
    main()
