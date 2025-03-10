class Bank:
    bank_balance = None

    def __init__(self, balance: List[int]):
        self.bank_balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.check_account_number(account1) or not self.check_account_number(account2):
            return False

        if not self.check_account_balance(account1, money):
            return False
        

        self.bank_balance[account1 - 1] -= money
        self.bank_balance[account2 - 1] += money

        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.check_account_number(account):
            return False
        
        self.bank_balance[account - 1] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if not self.check_account_number(account) or not self.check_account_balance(account, money):
            return False
        

        self.bank_balance[account - 1] -= money
        return True
    
    def check_account_number(self, a):
        n = len(self.bank_balance)
        return True if a >= 1 and a <= n else False
    
    def check_account_balance(self, a, amt):
        return self.check_account_number(a) and self.bank_balance[a - 1] >= amt


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)