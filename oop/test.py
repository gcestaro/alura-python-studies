def create_account(account_id, owner, balance, limit):
    return {
        "account_id": account_id,
        "owner": owner,
        "balance": balance,
        "limit": limit
    }


def deposit(account, amount):
    account["balance"] += amount


def withdraw(account, amount):
    account["balance"] -= amount


def get_balance(account):
    return account["balance"]
