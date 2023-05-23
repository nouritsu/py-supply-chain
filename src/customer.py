from team import Team
from random import randint


class Customer(Team):
    def __init__(self):
        self.recieved_orders = None
        self.placed_orders = {}
        self.stock = -1

    def place_order(self, count: int):
        id = randint(0, 1000)
        self.placed_orders[id] = count
        self.next.recieved_orders[id] = count

    def fulfill_order(self, number):
        raise Exception("Customers cannot fulfill orders.")

    def __str__(self):
        s = f"Placed Orders: {len(self.placed_orders)}\n"
        for k, v in self.placed_orders.items():
            s += f"\tOrder {str(k).rjust(4, '0')} of {v} items\n"
        return s
