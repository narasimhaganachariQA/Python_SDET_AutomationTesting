class bank:
    def __init__(self, name,balance):
        self.account_holder_name=name
        self.account_balance=balance

    def deposit(self,amount):
        self.balance=+self.balance+amount
        print("")
