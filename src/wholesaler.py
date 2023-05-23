from team import Team
from random import randint
from printer import pwarning


class Wholesaler(Team):
    def __init__(self):
        self.recieved_orders = {}
        self.placed_orders = {}
        self.stock = -1

    def place_order(self, count: int):
        ...

    def fulfill_order(self, number: int):
        ...

    def __str__(self):
        ...
