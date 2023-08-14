from decimal import Decimal


class BankAccount:

    def __init__(self, account_id, owner, balance=Decimal("0.0"), limit=Decimal("1500.0")):
        print(f"Building object: {self}")
        self.__account_id = account_id
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__is_able_to_withdraw(amount):
            self.__balance -= amount
            return True
        return False

    def __is_able_to_withdraw(self, amount):
        return self.__balance + self.__limit >= amount

    def transfer(self, amount, target):
        if self.withdraw(amount):
            target.deposit(amount)

    def statement(self):
        print(f"Owner: {self.__owner}")
        print(f"Current balance is ${self.__balance}")

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def account_id(self):
        return self.__account_id

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit


if __name__ == "__main__":
    account = BankAccount(123, "Gabriel")
    account.statement()
    account.deposit(100)
    account.withdraw(60)
    account.statement()

    account = None  # After this, the object is eligible to be picked up by Garbage Collector
