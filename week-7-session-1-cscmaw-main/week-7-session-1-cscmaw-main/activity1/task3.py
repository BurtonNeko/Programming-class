# Define a BankAccount class with the following fields:
# (1) holder_name
# (2) account_no
# (3) current_balance

# The value to each field needs to be provided when an instance of BankAccount is created.
# Write code to create an instance of BankAccount
class BankAccount:
    def __init__(self, holder_name, account_no, current_balance):
        self.holder_name = holder_name 
        self.account_no = account_no
        self.current_balance = current_balance
        
    def display_details(self):
        print(f'Account Holder:{self.holder_name}')
        print(f'Acount Number:{self.account.no}')
        print(f'Current Balance:{self.current_balance}')
        
account1 = BankAccount('Mr.Beast', '114', 514)
# Write code to print the details of the bank account

account1.dispaly_details()

# How would you change the __init__ method so that by the current_balance is an
# optional argument with a default value of 10 indicating that amount is needed to create
# a bank account? Recall optional argument in function definition?

# Once done, create another instance of BankAccount with only holder's name and 
# account number, and then print the all details of the new instance.
