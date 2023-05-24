from team import Team
from random import randint
from printer import pwarning


class Customer(Team):
    def __init__(self):
        super().__init__()
        self.recieved_orders = None
        self.stock = -1

    def fulfill_order(self, number):
        pwarning("Customers cannot fulfill orders.")

    def update(self):  # customers do not fulfill orders, hence dont need to be updated
        ...

    def __str__(self):
        s = "CUSTOMER\n"
        s += f"Placed Orders: {len(self.placed_orders)}\n"
        for k, v in self.placed_orders.items():
            s += f"\tOrder {str(k).rjust(4, '0')} of {v} items\n"
        return s
