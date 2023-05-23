from team import Team


class Customer(Team):
    def __init__(self, prev: Team, next: Team):
        self.orders = None
        self.set_next(next)
        self.set_prev(prev)

    def add_order(self):
        raise Exception("Customers cannot accept orders.")

    def place_order(self, count: int):
        self.next.add_order(count)

    def fulfill_order(self, number):
        raise Exception("Customers cannot fulfill orders.")
