class BankAccount:
    def __init__(self, number, name, balance, db):
        self.number = number
        self.name = name
        self.balance = balance
        self.db = db
        db.insert(self)

    # add your implementation

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        if isinstance(new_number, str):
            self.__number = new_number
        else:
            raise TypeError("account number must be a string")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_bal):
        if isinstance(new_bal, (int, float)):
            if new_bal > 0:
                self.__balance = new_bal
            else:
                raise ValueError("balance must be greater than zero")
        else:
            raise TypeError("balance must be a number")

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, new_db):
        from database import BankDB
        if isinstance(new_db, BankDB):
            self.__db = new_db

    def deposit(self, amount):
        self.db.record_transaction(self, amount)
        print(f"UPDATE account {self.__number} balance = {self.__balance}")

    def withdraw(self, amount):
        # add your implementation
        if self.__balance >= amount:
            self.db.record_transaction(self, -amount)
            print(f"UPDATE account {self.__number} balance = {self.__balance}")
        else:
            print("Not enough money")

    def transfer(self, amount, to_account):  # to_account is class bank_account but another value
        # add your implementation

        if self.__balance >= amount:
            self.db.record_transaction(to_account, amount)
            self.db.record_transaction(self, -amount)
            print(f"UPDATE account {self.__number} balance = {self.__balance}")
            print(f"UPDATE account {to_account.number} balance = {to_account.balance}")
        else:
            print("Not enough money")

    def __repr__(self):
        # add your implementation
        return f'Account(number="{self.__number}", name="{self.__name}", ' \
               f'balance={self.__balance}, db="{self.__db.name}")'
