class BankAccount:
    def __init__(self, code):
        self.code = code
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"[>>Code {self.code} Balance {self.balance}]"
