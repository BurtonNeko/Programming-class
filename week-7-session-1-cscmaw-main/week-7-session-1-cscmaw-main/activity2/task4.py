# Define an updated BankAccount class from activity1/task3
# that simulates a bank account with the following new methods:
# (1) deposit_funds - adding money to current balance
# (2) withdraw_funds - withdraw money from current balance. Should check if there is sufficient balance.
# If there is insufficient fund, should not be able to withdraw money. How would you define this method? 
# Should this method return something?
# (3) add_interest - add certain percentage of interest to the current balance
class BankAccount:
    def __init__(self, holder_name, account_no, current_balance):
        self.holder_name = holder_name 
        self.account_no = account_no
        self.current_balance = current_balance
        
    def display_details(self):
        print(f'Account Holder:{self.holder_name}')
        print(f'Acount Number:{self.account.no}')
        print(f'Current Balance:{self.current_balance}')


    def deposit_funds(self, amount):
        if amount <= 0:
            print('Deposit amount must be positive.')
            return False
        self.current_balance += amount
        print(f'${amount:.2f} deposited successfully')
        return True
    
    def withdraw_funds(self, amount):
        if amount <= 0:
            print('Withdraw amount must be positive')
            return False
        if amount > self.current_balance:
            print('Insufficient current balance, withdraw failed.')
            return False
        self.current_balance -= amount
        print(f'${amount:.2f} withdrawn successfully')
        return True
    
    def add_interest(self, rate_percent):
        if rate_percent < 0:
            print("Interest rate must be non-negative.")
            return False
        interest = self.current_balance * (rate_percent / 100)
        self.current_balance += interest
        print(f"Interest of ${interest:.2f} added at {rate_percent}% rate.")
        return True        
    





# Once completed, create an instance of BankAccount with your details and 
# make at least one call to each of the new methods, as well as a call
# to retrieve the current_balance at the end.



# In the deposit_funds method, is a negative number allowed? 
# If you did not include validation on the value, please update
# your code to include that. A simple solution is no money is added
# the current balance if a negative amount is deposited into a bank account.




# How about the add_interest method? Can the interest be 0 or a negative number?
# If you have not include validation for that, update your code to deal with it.
