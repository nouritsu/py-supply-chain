from team import Team
from random import randint
from printer import pwarning


class Wholesaler(Team):
    def __init__(self):
        super().__init__()
        self.production = -1

    def update(self):
        self.round += 1
        for k, v in self.fulfilled_orders.items():
            if v == self.round:
                del self.prev.placed_orders[k]

    def __str__(self):
        s = "WHOLESALER\n"
        s += f"Recieved Orders: {len(self.placed_orders)}\n"
        for k, v in self.recieved_orders.items():
            s += f"\tOrder {str(k).rjust(4, '0')} of {v} items\n"
        s += f"Placed Orders: {len(self.placed_orders)}\n"
        for k, v in self.placed_orders.items():
            s += f"\tOrder {str(k).rjust(4, '0')} of {v} items\n"
        return s
