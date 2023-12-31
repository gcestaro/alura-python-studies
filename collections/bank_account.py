from abc import ABCMeta, abstractmethod
from functools import total_ordering


@total_ordering
class BankAccount(metaclass=ABCMeta):
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    @property
    def code(self):
        return self._code

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def apply_taxes(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False

        return self._code == other.code

    def __str__(self):
        return f"[>>Code {self._code} Balance {self._balance}<<]"

    def __lt__(self, other):
        if self._balance != other.balance:
            return self._balance < other.balance
        return self._code < other.code


class CheckingAccount(BankAccount):
    def apply_taxes(self):
        self._balance -= 2


class SavingAccount(BankAccount):
    def apply_taxes(self):
        self._balance *= 0.01
        self._balance -= 3
