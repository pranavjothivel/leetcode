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
        return 1 <= a <= len(self.bank_balance)
    
    def check_account_balance(self, a, amt):
        return self.check_account_number(a) and self.bank_balance[a - 1] >= amt