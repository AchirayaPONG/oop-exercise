import json


class BankDB:
    def __init__(self, name):
        self.name = name

    def insert(self, bank_account):
        # add your implementation
        new_data = {
            bank_account.number: {
                "name": bank_account.name,
                "balance": bank_account.balance
            }
        }
        try:
            with open("accounts.json", "r") as ac_file:
                account = json.load(ac_file)

        except FileNotFoundError:
            with open("accounts.json", "w") as ac_file:
                json.dump(new_data, ac_file, indent=4)

        else:
            account.update(new_data)
            with open("accounts.json", "w") as ac_file:
                json.dump(account, ac_file, indent=4)

    def search(self, account_number):
        # add your implementation
        try:
            with open("accounts.json", "r") as ac_file:
                account = json.load(ac_file)
                print(f"Name={account[account_number]['name']}, Balance={account[account_number]['balance']}")
        except KeyError:
            print(f"No data for account number: {account_number}")
        # pass

    def delete(self, account_number):
        # add your implementation
        try:
            with open("accounts.json", "r") as ac_file:
                account = json.load(ac_file)
                del account[account_number]
        except KeyError:
            print(f"No data for account number: {account_number}")

        else:
            with open("accounts.json", "w") as ac_file:
                json.dump(account, ac_file, indent=4)
            print(f"DELETE account {account_number}")

    def record_transaction(self, account, amount):
        account.balance += amount
        with open("accounts.json", "r") as ac_file:
            ac = json.load(ac_file)
            ac[account.number]['balance'] = account.balance

        self.insert(account)

    def __repr__(self):
        # add your implementation
        return f'BankDB(name="{self.name}")'
