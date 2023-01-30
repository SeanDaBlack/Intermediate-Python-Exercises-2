class BankAccount:
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.starting_balance = starting_balance

    def deposit_money(self, dollar_amount):
        self.starting_balance += dollar_amount

    def withdraw_money(self, dollar_amount):
        self.starting_balance -= dollar_amount

    def get_balance(self):

        return f"{self.account_name} has a balance of ${self.starting_balance}"
