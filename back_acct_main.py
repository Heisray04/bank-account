from bank_acct_lib import *
import time


print("<<< WELCOME TO RAY BANK >>>")
time.sleep(2)
open_acct = input('\nWill you like to open an account with us? (y/n): ').strip().lower()
if open_acct == 'y': pass
else: exit()

while True:
    try:
        money = int(input("\nInitial deposit amount(without ',' or '.'):\n₦"))
        account = BankAccount(money)
        break
    
    except ValueError:
        print('--- Not A Number! ---')

actions()
while True:
    print(('-' * 100) + "\n=== NOTE: ONLY NUMBERS ARE REQUIRED IN ALL INPUT FIELDS WITHOUT (Y/N) OPTION! =====")
    print("What would you like to do? 1, 2, or 3")

    # Error handler. Detects non-positive integer input and outputs a custom error message.
    # Runs the remaining code if no errors are detected.
    try:
        select = int(input('Pick a number: '))

    except ValueError:
        print('--- Numbers Only! ---')
        continue

    else:
        if select == 1:
            try:
                depo_amt = int(input('How much are you depositing?: ₦'))
                if depo_amt < 0:
                    print('--- Unable to continue with the transaction ---')
                    continue
                dynam_disp(select)
                print(account.deposit(depo_amt))
                transaction()                
            except (ValueError, TypeError) as VT:
                print(f'ERROR! {VT}\n--- Numbers Only! ---')
                continue
        elif select == 2:
            try:
                with_amt = int(input('Withdrawal amount: ₦'))
                if with_amt < 0:
                    print('--- Unable to continue with the transaction ---')
                    continue
                dynam_disp(select)
                print(account.withdraw(with_amt))
                transaction()
            except (ValueError, TypeError) as VT:
                print(f'ERROR! {VT}\n--- Numbers Only! ---')
                continue
        elif select == 3:
            print("Here's your current account balance:")
            print(account.get_balance())
        elif select > 3 or select < 1:
            print("--- Out Of Given Range! ---")
            continue

        print("-" * 100)
        print(' ' * 100, end='\r')
        time.sleep(1)

        reply = input('Would you like to make another transaction? (y/n): ').strip().lower()
        if reply == 'y':
            reply2 = input('Want to see the action list? (y/n): ').strip().lower()
            if reply2 == 'y':
                actions()
            continue
        break
