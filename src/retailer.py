from team import Team
from constants import RETAILER_INIT_STOCK
from result import Result


class Retailer(Team):
    def __init__(self):
        super().__init__()
        self.stock = RETAILER_INIT_STOCK
        self.production = -1

    def update(self):
        self.round += 1
        for k, v in self.fulfilled_orders.items():
            if v["week"] == self.round:
                del self.prev.placed_orders[k]

    def set_production(self, count: int) -> Result:
        r = Result()
        r._set_err("Cannot set production as a Retailer.")
        return r

    def stats(self) -> dict:
        d = super().stats()
        d["role"] = "Retailer"
        return d
