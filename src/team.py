from random import randint
from constants import ORDER_ID_MIN, ORDER_ID_MAX, DELIVERY_TIME
from result import Result
from printer import perror, pwarning


class Team:
    def __init__(self):
        self.recieved_orders = {}
        self.placed_orders = {}
        self.fulfilled_orders = {}
        self.production = 1
        self.stock = 0
        self.round = 1

    def place_order(self, count: int) -> Result:
        r = Result()
        id = self.gen_id(self.placed_orders, self.next.recieved_orders)
        self.placed_orders[id] = count
        self.next.recieved_orders[id] = count
        r._set_ok(f"Placed order with number {id} for {count} items.")
        return r

    def fulfill_order(self, number: int) -> Result:
        r = Result()
        if number in self.recieved_orders:
            self.fulfilled_orders[number] = {
                "count": self.recieved_orders[number],
                "week": self.round + DELIVERY_TIME,
            }
            self.stock -= self.recieved_orders[number]
            del self.recieved_orders[number]
            r._set_ok(f"Fulfilled order number {number}")
        else:
            r._set_err(f"Cannot fulfill non existent order {number}")
        return r

    def set_production(self, count: int) -> Result:
        self.production = count
        r = Result()
        r._set_ok(f"Set production to {count}")
        return r

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def update(self):
        self.round += 1
        for k, v in self.fulfilled_orders.items():
            if v["week"] == self.round:
                self.prev.stock += self.prev.placed_orders[k]
                del self.prev.placed_orders[k]

    def gen_id(self, c1: dict, c2: dict):
        if (len(c1.keys()) == ORDER_ID_MAX) or (len(c2.keys()) == ORDER_ID_MAX):
            perror("Ran out of order IDs", 2)
        id = randint(ORDER_ID_MIN, ORDER_ID_MAX)
        while (id in c1.keys()) or (id in c2.keys()):
            id = randint(ORDER_ID_MIN, ORDER_ID_MAX)
        return id

    def stats(self) -> dict:
        d = {}
        d["role"] = "unset"
        d["recieved-orders"] = self.recieved_orders
        d["placed-orders"] = self.placed_orders
        d["fulfilled-orders"] = self.fulfilled_orders
        d["stock"] = self.stock
        d["round"] = self.round
        return d
