from team import Team
from random import randint
from printer import pwarning


class Retailer(Team):
    def __init__(self):
        self.recieved_orders = {}
        self.placed_orders = {}
        self.stock = -1

    def place_order(self, count: int):
        id = randint(0, 1000)
        self.placed_orders[id] = count
        self.next.recieved_orders[id] = count

    def fulfill_order(self, number: int):
        if number in self.recieved_orders:
            del self.prev.placed_orders[id]
            del self.recieved_orders[id]
        else:
            pwarning(f"Cannot fulfill nonexistent order: {number}")

    def __str__(self):
        s = "RETAILER"
        s += f"Recieved Orders: {len(self.placed_orders)}\n"
        for k, v in self.recieved_orders.items():
            s += f"\tOrder {str(k).rjust(4, '0')} of {v} items\n"
        s += f"Placed Orders: {len(self.placed_orders)}\n"
        for k, v in self.placed_orders.items():
            s += f"\tOrder {str(k).rjust(4, '0')} of {v} items\n"
        return s
