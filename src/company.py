from team import Team
from printer import pwarning


class Company(Team):
    def __init__(self):
        super().__init__()

    def __str__(self):
        s = "Company\n"
        s += f"Recieved Orders: {len(self.placed_orders)}\n"
        for k, v in self.recieved_orders.items():
            s += f"\tOrder {str(k).rjust(4, '0')} of {v} items\n"
        s += f"Placed Orders: {len(self.placed_orders)}\n"
        for k, v in self.placed_orders.items():
            s += f"\tOrder {str(k).rjust(4, '0')} of {v} items\n"
        return s
