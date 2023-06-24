class Command:
    name: str
    arg: int
    invalid: bool

    def __init__(self, s: str):
        a = s.split(" ")
        self.invalid = False
        if len(a) == 1:
            self.name = a[0]
            self.arg = None
        elif len(a) == 2:
            self.name = a[0]
            try:
                self.arg = int(a[1])
            except ValueError:
                self.arg = None
                self.invalid = True
        else:
            self.name = ""
            self.arg = None
            self.invalid = True

    def __str__(self):
        return f"Name: {self.name}\nArg: {self.arg}\nInvalid: {self.invalid}"
