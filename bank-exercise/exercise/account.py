class BankAccount:
    def __init__(self, number, name, balance, db):
        self.number = number
        self.name = name
        self.balance = balance
        self.db = db
        db.insert(self)

    # add your implementation

    def deposit(self, amount):
        # add your implementation
        pass

    def withdraw(self, amount):
        # add your implementation
        pass

    def transfer(self, amount, to_account):
        # add your implementation
        pass

    def __repr__(self):
        # add your implementation
        pass
