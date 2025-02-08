# Bank Account Class
from abc import ABC, abstractmethod
"""

Attr:
    account_holder
    balance
    transaction_hist = [{
        'transaction_type': 'deposit/withdrawl',
        'amount': float
        'date': 'YYYY-MM-DD',
    }]

"""

class BankAccountABC:
    # Let's build the essentail mehtods
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    # Getter method prob needs balance to be priv
    def get_balance(self):
        pass

    @abstractmethod
    def get_transaction_history(self):
        pass

    @abstractmethod
    def get_account_summary(self):
        pass


class BankAccount(BankAccountABC):
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = float(balance)
        self.__transaction_history = []

    # Building getter functions first
    def get_balance(self):
        return float(self.__balance)

    def deposit(self, amount):
        self.__balance += float(amount)
        # Adding to transaction history
        trans_history = {
            'transaction_type': 'deposit',
            'amount': float(amount)
            # 'date': How do I get the date here,
        }
        self.__transaction_history.append(trans_history)
        return self.get_balance()

    def withdraw(self, amount):
        if amount > self.__balance:
            return 'Insufficient funds'

        self.__balance -= float(amount)
        # Adding to transaction history
        trans_history = {
            'transaction_type': 'withdrawal',
            'amount': float(amount)
            # 'date': How do I get the date here,
        }
        self.__transaction_history.append(trans_history)
        return self.get_balance()

    def get_transaction_history(self):
        return self.__transaction_history

    def get_account_summary(self):
        # Returns account name. curr balance and total num of transactions
        summary = {
            'account_holder': self.account_holder,
            'balance': self.get_balance(),
            'total_transactions': len(self.__transaction_history),
        }
        return summary

    # String representation of account
    def __str__(self):
        return f'Account holder: {self.account_holder}, Balance: ${self.get_balance()}'


account = BankAccount('John Doe',5000.0)

# Deposits
account.deposit(2000)

# Withdrawals
result1 = account.withdraw(1500)    # True
result2 = account.withdraw(10000)   # "Insufficient Funds"
print(result1, result2)
print()
# Get Balance and History
print(account.get_balance())    # 6500.0 (on paper) but we deposited 2000 which means 7000-1500
print()
print(account.get_transaction_history())
print()
print(account.get_account_summary())
print()
print(account)