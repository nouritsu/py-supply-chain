class Team:
    def add_order(self, count: int):
        ...

    def place_order(self, count: int):
        ...

    def fulfill_order(self, number: int):
        ...

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev
