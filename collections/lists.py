"""
    Python Datastructures doc: https://docs.python.org/3/tutorial/datastructures.html
"""
from bank_account import BankAccount

"""
    Lists:
    - sequence of iterable elements
    - mutable
    - random access
    - able to add different types
"""


def default_value_keep_its_value_cache_in_memory(list=[]):
    print(len(list))
    list.append(1)


def default_value_as_none(list=None):
    if list is None:
        list = []
    print(len(list))
    list.append(1)


def begin_with_lists():
    ages = [39, 30, 27]
    print(ages)
    print(type(ages))
    print(len(ages))
    print(ages[1])
    ages.append(15)
    print(ages)
    for age in ages:
        print(age)
    ages.remove(15)
    print(ages)
    ages.clear()
    ages.append(15)
    ages.append(29)
    ages.append(30)
    ages.append(54)
    ages.append(89)
    print(15 in ages)
    ages.insert(2, 20)
    print(ages)
    ages.extend([37, 44])
    print(ages)
    # List comprehension
    print([age + 1 for age in ages])
    print([age for age in ages if age > 21])
    print(ages)
    default_value_keep_its_value_cache_in_memory()  # 0
    default_value_keep_its_value_cache_in_memory()  # 1
    default_value_keep_its_value_cache_in_memory()  # 2
    default_value_as_none()  # 0
    default_value_as_none()  # 0
    default_value_as_none()  # 0


if __name__ == '__main__':
    # begin_with_lists()
    gabriel_account = BankAccount(1)
    jessica_account = BankAccount(2)

    accounts = [gabriel_account, jessica_account]
    gabriel_account.deposit(100)
    jessica_account.deposit(200)

    for account in accounts:
        print(account)
