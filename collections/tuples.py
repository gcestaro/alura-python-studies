from bank_account import BankAccount

"""
    Tuples:
    - immutable
    - index position represents something (e.g name, id)
"""

if __name__ == '__main__':
    gabriel_account = BankAccount(1)
    jessica_account = BankAccount(2)

    accounts = [(1, "Gabriel", 100.0), (2, "Jessica", 150.0)]  # List of tuples
    print(accounts)
    print(accounts[0][2])  # 100
    # accounts[0][2] = 200 # error, tuples are immutable

    accounts_report = (gabriel_account, jessica_account)  # Tuple of objects
    print(accounts_report)
    gabriel_account.deposit(100)  # Objects are mutable
    # accounts_report[0] = gabriel_account  # error, tuples are immutable
