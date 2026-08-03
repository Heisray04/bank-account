from datetime import datetime
import time

# A template for a bank account.
class BankAccount:
    '''Handles a user's bank account'''
    def __init__(self, balance):
        self.__balance = balance

    def _get_time(self):
        self._date_time = datetime.now()
        self._time = self._date_time.strftime("%I:%M")
        self._date = self._date_time.strftime("%a, %d %B, %Y")
        self._am_pm = 'AM' if (self._date_time.hour < 12) else 'PM'
        self._msg = f'at {self._time} {self._am_pm} on {self._date}'

    def deposit(self, amount):
        self._get_time()
        if amount > 0:
            self.__balance += amount
            return f">>> Successfully deposited ₦{amount:,} {self._msg}."

    def withdraw(self, amount):
        self._get_time()
        if self.__balance >= amount:
            self.__balance -= amount
            return f"You successfully withdrew ₦{amount:,} {self._msg}."
        else:
            return "--- Insufficient balance! ---"

    def get_balance(self):
        self._get_time()
        return f"₦{self.__balance:,}.\nThanks for banking with us."


# Functions available for the bank_account program
def actions():
    """ Displays 100 hyphens to indicate the start of a new transaction and...
    the available actions that can be performed for the transaction. """
    print('-' * 100)
    print("""
    Supported actions list
    1. Deposit
    2. Withdraw
    3. Show balance
    """)

def transaction():
    time.sleep(1)
    """ A countdown after each completed transaction. """
    for i in range(3, 0, -1):
        print('>>> Transaction Completed!', i, end="\r")
        time.sleep(1)
    print(' ' * 50, end="\r")
    print('Thanks for banking with us.')

def dynam_disp(sel):
    """ Creates a dynamic display while depositing or withdrawing. """
    for i in range(0, 6):
        if sel == 1:
            print("Depositing" + ('.'*i), end='\r')
        elif sel == 2:
            print("Withdrawing" + ('.'*i), end='\r')
        time.sleep(1)
