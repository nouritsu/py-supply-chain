from team import Team
from result import Result


class Customer(Team):
    def __init__(self):
        super().__init__()
        self.received_orders = None
        self.fulfilled_orders = None
        self.stock = -1

    def fulfill_order(self, number):
        r = Result()
        r._set_err("Cannot fulfill orders as Customer.")
        return r

    def update(self):  # Customers do not need to be updated
        self.round += 1

    def set_production(self, count: int) -> Result:
        r = Result()
        r._set_err("Cannot set production as a Customer.")
        return r

    def stats(self) -> dict:
        d = {}
        d["role"] = "Customer"
        d["placed-orders"] = self.placed_orders
        d["round"] = self.round
        return d
