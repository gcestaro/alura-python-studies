class BankAccount:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def __str__(self):
        return f"[>>Code {self._code} Balance {self._balance}]"


class CheckingAccount(BankAccount):
    def apply_taxes(self):
        self._balance -= 2


class SavingAccount(BankAccount):
    def apply_taxes(self):
        self._balance *= 0.01
        self._balance -= 3
