class User:
    def __init__(self, name, amount, now):
        self.name = name
        self.amount = amount
        self.now = now
        self.left = self.amount - self.now