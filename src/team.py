from random import randint
from constants import ORDER_ID_MIN, ORDER_ID_MAX, DELIVERY_TIME
from printer import perror, pwarning


class Team:
    def __init__(self):
        self.recieved_orders = {}
        self.placed_orders = {}
        self.fulfilled_orders = {}
        self.stock = 0
        self.round = 1

    def update(self):
        self.round += 1
        for k, v in self.fulfilled_orders.items():
            if v == self.round:
                del self.prev.placed_orders[k]

    def place_order(self, count: int):
        id = self.gen_id(self.placed_orders, self.next.recieved_orders)
        self.placed_orders[id] = count
        self.next.recieved_orders[id] = count

    def fulfill_order(self, number: int):
        if number in self.recieved_orders:
            self.fulfilled_orders[number] = self.round + DELIVERY_TIME
            del self.recieved_orders[number]
        else:
            pwarning(f"Cannot fulfill nonexistent order: {number}")

    def produce(self, count: int):
        self.stock += count

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def gen_id(self, c1: dict, c2: dict):
        if (len(c1.keys()) == ORDER_ID_MAX) or (len(c2.keys()) == ORDER_ID_MAX):
            perror("Ran out of order IDs", 2)
        id = randint(ORDER_ID_MIN, ORDER_ID_MAX)
        while (id in c1.keys()) or (id in c2.keys()):
            id = randint(ORDER_ID_MIN, ORDER_ID_MAX)
        return id
