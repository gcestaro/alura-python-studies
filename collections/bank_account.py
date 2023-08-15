from abc import ABCMeta, abstractmethod


class BankAccount(metaclass=ABCMeta):
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    @abstractmethod
    def apply_taxes(self):
        pass

    def __str__(self):
        return f"[>>Code {self._code} Balance {self._balance}]"


class CheckingAccount(BankAccount):
    def apply_taxes(self):
        self._balance -= 2


class SavingAccount(BankAccount):
    def apply_taxes(self):
        self._balance *= 0.01
        self._balance -= 3
