import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transactions = [(Account._current_time(), balance)]
        print(f"Account created for {self._name}")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append((Account._current_time(), amount))
        self.show_balance()

    def withdraw(self, amount):
        if 0 < amount < self._balance:
            self._balance -= amount
            self._transactions.append((Account._current_time(), -amount))
        else:
            print(f"The amount must be less than {self._balance}")
        self.show_balance()

    def show_balance(self):
        print(f"Balance: {self._balance}")

    def show_transactions(self):
        for date, amount in self._transactions:
            if amount > 0:
                type = "deposited"
            else:
                type = "withdraw"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, type,
                    date, date.astimezone()))


if __name__ == "__main__":
    tim = Account("Tim", 0)

    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(2000)

    tim.show_transactions()
    print("-" * 80)

    steph = Account("steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
