from team import Team
from customer import Customer
from retailer import Retailer
from wholesaler import Wholesaler
from company import Company
from result import Result
from command import Command


class Game:
    round: int
    turns: int
    current: Team
    customer: Customer
    retailer: Retailer
    wholesaler: Wholesaler
    company: Company
    weekly_stock: dict

    def __init__(self, turns: int):
        self.turns = turns
        self.round = 1
        self.customer = Customer()
        self.retailer = Retailer()
        self.wholesaler = Wholesaler()
        self.company = Company()

        self.customer.set_prev(None)
        self.customer.set_next(self.retailer)

        self.retailer.set_prev(self.customer)
        self.retailer.set_next(self.wholesaler)

        self.wholesaler.set_prev(self.retailer)
        self.wholesaler.set_next(self.company)

        self.company.set_prev(self.wholesaler)
        self.company.set_next(None)

        self.current = self.customer

        self.weekly_stock = {}
        self.weekly_stock["Retailer"] = []
        self.weekly_stock["Wholesaler"] = []
        self.weekly_stock["Company"] = []

    # Execute a command, returns an error message if unsucessful
    def execute(self, command: str) -> Result:
        r = Result()
        c = Command(command)

        if c.invalid and c.arg < 0:
            r._set_err(
                f"Invalid usage, usage of command '<name> [arg]' where arg is an integer."
            )
        else:
            match c.name:
                case "order":
                    r = self.current.place_order(c.arg)

                case "fulfill":
                    r = self.current.fulfill_order(c.arg)

                case "produce":
                    r = self.set_production(c.arg)

                case "next":
                    self.__update()
                    self.customer.update()
                    self.retailer.update()
                    self.wholesaler.update()
                    self.company.update()
                    if self.finished():
                        return Result()._set_err("Cannot end turn, game is over.")
                    if self.current.next:
                        self.current = self.current.next
                    else:
                        self.current = self.customer
                        self.round += 1

                case "exit":
                    r._set_err("Exit")
                    return r

                case "":
                    r._set_err("Cannot execute command, use 'next' to end turn.")

                case _:
                    r._set_err("Unknown Command.")

        if not r.is_err():
            r._set_ok = self.current.stats()
        return r

    # Returns true if game is over (use in main loop condition)
    def finished(self):
        return self.round == self.turns

    # Get week by week stock count of each team, use after game end
    def get_stats(self):
        return self.weekly_stock

    def __update(self):
        self.weekly_stock["Retailer"].append(self.retailer.stock)
        self.weekly_stock["Wholesaler"].append(self.wholesaler.stock)
        self.weekly_stock["Company"].append(self.company.stock)
