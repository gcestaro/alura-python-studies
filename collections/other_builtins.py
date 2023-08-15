from bank_account import CheckingAccount, SavingAccount
from operator import attrgetter


def _range():
    global i
    range_of_ages = range(len(ages))  # lazy
    print(range_of_ages)
    for i in range_of_ages:
        print(i, ages[i])


def _enumerate():
    global i
    ages_enum = enumerate(ages)  # lazy, list of tuples (index, value)
    print(ages_enum)
    for i, age in ages_enum:  # unpacking tuple
        print(i, age)


def _sorted():
    print(sorted(ages))
    print(sorted(ages, reverse=True))
    print(ages)

    jose_account = CheckingAccount(2)
    jose_account.deposit(200)

    alura_account = CheckingAccount(2)
    alura_account.deposit(400)

    gabriel_account = SavingAccount(1)
    gabriel_account.deposit(300)

    jessica_account = CheckingAccount(1)
    jessica_account.deposit(100)

    accounts = [gabriel_account, jessica_account, jose_account, alura_account]

    # by default, TypeError: '<' not supported between instances of 'CheckingAccount' and 'SavingAccount'
    # Need to implement __lt__ on BankAccount or use a key function
    for account in sorted(accounts):
        print(account)

    for account in sorted(accounts, key=attrgetter("_balance")):
        print(account)


if __name__ == '__main__':
    ages = [15, 21, 45, 30, 54, 78, 36, 90, 101]

    # _range()
    # _enumerate()
    _sorted()
