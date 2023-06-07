from result import Result
from team import Team
from constants import COMPANY_INIT_STOCK, COMPANY_INIT_PRODUCTION


class Company(Team):
    def __init__(self):
        super().__init__()
        self.stock = COMPANY_INIT_STOCK
        self.production = COMPANY_INIT_PRODUCTION

    def place_order(self, count: int) -> Result:
        r = Result()
        r._set_err("Cannot order items as company.")
        return r

    def update(self):
        self.round += 1
        self.stock += self.production  # Company only
        for k, v in self.fulfilled_orders.items():
            if v == self.round:
                self.prev.stock += self.prev.placed_orders[k]
                del self.prev.placed_orders[k]

    def stats(self) -> dict:
        d = super().stats()
        d["production"] = self.production
        d["role"] = "Company"
        del d["placed-orders"]
        return d
