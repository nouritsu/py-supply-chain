from team import Team
from constants import WHOLESALER_INIT_STOCK
from result import Result


class Wholesaler(Team):
    def __init__(self):
        super().__init__()
        self.production = -1
        self.stock = WHOLESALER_INIT_STOCK

    def update(self):
        self.round += 1
        for k, v in self.fulfilled_orders.items():
            if v == self.round:
                self.prev.stock += self.prev.placed_orders[k]
                del self.prev.placed_orders[k]

    def set_production(self, count: int) -> Result:
        r = Result()
        r._set_err("Cannot set production as a Retailer.")
        return r

    def stats(self) -> dict:
        d = super().stats()
        d["role"] = "Wholesaler"
        return d
