from BankAccount import BankAccount

if __name__ == "__main__":

    bk = BankAccount("Sean Wiggs", 15000)

    bk.deposit_money(1000)
    bk.withdraw_money(500)

    print(bk.get_balance())
